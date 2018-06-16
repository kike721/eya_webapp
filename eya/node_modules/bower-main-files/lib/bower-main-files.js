/*!
 * bower-main-files - lib/bower-main-files.js
 *
 * Copyright(c) 2014 Liucw <liucw.mail@gmail.com>
 * MIT Licensed
 */

"use strict";

var fs = require('fs');
var path = require('path');

var mkdirp = require('mkdirp');

var BOWER_PATH = 'bower_components';
var MAIN_PATH = 'bower_main_files';


function bmf(bowerPath, outPath) {
  bowerPath = path.resolve(bowerPath);
  outPath = path.resolve(outPath);

  if (!isDir(bowerPath))
    return console.error('Please input exists path!');

  // bowerPath like './xx/xx/bower_components'
  if (path.basename(bowerPath) === BOWER_PATH) {
    fs.readdirSync(bowerPath).forEach(function(component) {
      handleComponentPath(bowerPath, component, outPath);
    });

  // bowerPath like 'moment'
  } else {
    var component = path.basename(bowerPath);
    bowerPath = path.dirname(bowerPath);
    handleComponentPath(bowerPath, component, outPath);
  }

}

function handleComponentPath(bowerPath, component, outPath) {
  try {
    var bowerJsonPath = addPath(bowerPath, component, 'bower.json');
    var found = fs.existsSync(bowerJsonPath);
    if(!found){
      bowerJsonPath = addPath(bowerPath, component, '.bower.json');
      found = fs.existsSync(bowerJsonPath);
      if(!found){
        return console.error('\''+component+'\' component directory no bower.json or .bower.json');
      }
    }
    var bowerJson = require(bowerJsonPath);
  } catch (e) {
    return console.error('require bower.json error:', e);
  }

  var mainValue = bowerJson['main'];

  if (typeof mainValue === 'string') {
    var bower = addPath(bowerPath, component, mainValue);
    var out = addPath(outPath, component, mainValue);

    var found = fs.existsSync(bower);
    if(!found){
      return console.error('\''+component+'\' component have no found file :', file);
    }

    mkdirp.sync(path.dirname(out));

    copySync(bower, out);
  } else if (Array.isArray(mainValue)) {
    mainValue.forEach(function(file) {
      var bower = addPath(bowerPath, component, file);
      var out = addPath(outPath, component, file);


      var found = fs.existsSync(bower);
      if(!found){
        return console.error('\''+component+'\' component have no found file :', file);
      }

      mkdirp.sync(path.dirname(out));

      copySync(bower, out);
    })
  } else {
    return console.error('bower.json \'main\' value must be string or array');
  }
}


function isDir(path) {
  return fs.existsSync(path) && fs.statSync(path).isDirectory();
}

function addPath() {
  return path.resolve(path.join.apply(null, arguments))
}

// function copy(sourceFile, targetFile) {
//   fs.createReadStream(sourceFile).pipe(fs.createWriteStream(targetFile));
// }

function copySync(sourceFile, targetFile) {
  fs.writeFileSync(targetFile, fs.readFileSync(sourceFile));
}

module.exports = bmf;
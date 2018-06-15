/*
*   Gulp config params
*/
module.exports = {
    buildDir: 'static/',
    jsBuildDir: 'static/site/js/min',
    jsSrcInitFile: 'src/js/initApp.js',
    jsSrcScriptDir: 'src/js/**/*.js',
    jsBuildBundleFile: 'nadro.build.js',
    libDir: 'bower_components/',
    sassSrcInitFile: 'src/sass/style.scss',
    sassBuildDir: 'static/site/css/',
    sassWatchDir: 'src/sass/**/*.scss',
    sassAmpBuildDir: 'templates/amp/',
    sassConfig: {
        compass: true,
        //sourcemap: false,
        //sourcemap: true,
        lineNumbers: true,
        //style: "expanded",
        style: "compressed",
        require: ["compass"]
    },
    imgBuildDir: 'static/site/img/',
    imgSrcDir: 'src/img/**/*',
    imgWatchDir: 'src/img/**/*'
};

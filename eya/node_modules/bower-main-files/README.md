# Bower main files


[![Build Status](https://travis-ci.org/booxood/bower-main-files.png?branch=master)](https://travis-ci.org/booxood/bower-main-files)

A command line for get main files from installed bower packages

## Install

```
npm install -g bower-main-files
```

## Example

```
$ bower-main-files --help

  Usage: bower-main-files  

  Options:

    -h, --help          output usage information
    -V, --version       output the version number
    -b, --bower <path>  bower components path
    -o, --out <path>    out path

  Examples:

    $ bower-main-files -b ./bower_components  -o ./bower_main_files
    $ bower-main-files -b ./bower_components/moment  -o ./bower_main_files

  if not specify parameters, default first argv is bower components path, second argv is out path

    $ bower-main-files ./bower_components  ./bower_main_files

  if in 'bower_components' directory

    $ bower-main-files ./bower_main_files
    $ bower-main-files moment ./bower_main_files

```

## License

The MIT License (MIT)

Copyright (c) 2013 Liucw

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

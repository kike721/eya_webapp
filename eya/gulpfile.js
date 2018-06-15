/**
 * Load NPM dependencies
*/
var gulp = require('gulp');
var gutil = require("gulp-util");
var babelify = require('babelify');
var sass = require('gulp-ruby-sass');
var plumber = require('gulp-plumber');
var browserify = require('browserify');
var source = require('vinyl-source-stream');
var sourcemaps = require("gulp-sourcemaps");
var browserSync = require('browser-sync').create();
var image = require('gulp-image');
var uglify = require('gulp-uglifyjs');

/**
 * Load gulp config file
 */
var gulpConfig = require('./gulpConfig');

/**
 * Static server
 */
gulp.task('watcher', ['sass','minJS'], function() {
	// Watch files
	gulp.watch(gulpConfig.jsSrcScriptDir, ['minJS'], browserSync.reload);
	gulp.watch(gulpConfig.sassWatchDir, ['sass'], browserSync.reload);
});

/**
 * Image compressed
 */
gulp.task('image', function () {
  return gulp.src(gulpConfig.imgSrcDir)
    		.pipe(image())
    		.pipe(gulp.dest(gulpConfig.imgBuildDir))
				.pipe(browserSync.stream({once: true}));
});

/**
 * Sass
*/
gulp.task('sass', function () {
	return sass(gulpConfig.sassSrcInitFile, gulpConfig.sassConfig)
	.pipe(sourcemaps.write())
	.on('error', function () {
		gutil.log( gutil.colors.red('ERROR', 'Compiling Sass Error'));
		gutil.log( gutil.colors.red(err.message));
		gutil.beep();
		browserSync.notify("<span style='color: red;'>Compiling Sass Error</>");
		this.emit('end');
	})
	.pipe(gulp.dest(gulpConfig.sassBuildDir))
	.pipe(browserSync.stream({once: true}));
});

/**
 * js
*/

gulp.task('basejs', function() {
	return gulp.src([
		'src/js/jquery-2.1.4.min.js',
		'src/js/base.js',
		'src/js/search.js',
		'src/js/formValidator.js',
	])
	.pipe(uglify('base.min.js', {
		outSourceMap: false
	}))
	.pipe(gulp.dest(gulpConfig.jsBuildDir));
});

gulp.task('orderjs', function() {
	return gulp.src([
		'src/js/formValidator.js',
		'src/js/order.js',
	])
	.pipe(uglify('order.min.js', {
		outSourceMap: false
	}))
	.pipe(gulp.dest(gulpConfig.jsBuildDir));
});

gulp.task('minJS', ['basejs','orderjs']);

/**
 * Main tasks
*/
gulp.task('live', ['watcher']);

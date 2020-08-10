const gulp = require('gulp');
const stylus = require('gulp-stylus');
const imagemin = require('gulp-imagemin');
const merge = require('merge-stream');
const concat = require('gulp-concat');

const gcmq = require('gulp-group-css-media-queries');
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const svgstore = require('gulp-svgstore');
const svgmin = require('gulp-svgmin');
const cheerio = require('gulp-cheerio');
const replace = require('gulp-replace');
const svgSprite = require('gulp-svg-sprite');

const uglify = require('gulp-uglify');

const webpack = require('webpack-stream');

gulp.task('stylus', function(){

    return gulp.src('stylus/style.styl')
        .pipe(stylus({
            compress: true
        }))
        .pipe(gcmq())
        .pipe(concat('style.css'))
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(gulp.dest('../static/css'));


});

gulp.task('js', function(){
    return gulp.src('js/**.js')
        .pipe(webpack( require('./webpack.config.js') ))
        .pipe(gulp.dest('../static/js'));
});

gulp.task('imagemin', function(){
    return gulp.src('../media/images/**/**.**')
        .pipe(imagemin())
        .pipe(gulp.dest('../static/images'));
});

gulp.task('svgsprite', function(){
    return gulp.src('./images/sprite/*.svg')
        .pipe(svgmin())
        // remove all fill, style and stroke declarations in out shapes
        .pipe(cheerio({
            run: function ($) {
                $('title').remove();
            },
            parserOptions: {xmlMode: true}
        }))
        // cheerio plugin create unnecessary string '&gt;', so replace it.
        .pipe(replace('&gt;', '>'))
        .pipe(svgSprite({
            mode: {
                symbol: {
                    dest: '.',
                    sprite: 'sprite.svg',
                    prefix: '.icon-',
                    dimensions: '%s',
                    render: {
                        styl: {
                            dest: '../../src/stylus/sprite.styl'
                        },
                    }
                }
            }
        }))
        .pipe(gulp.dest('../static/i/'));
});

gulp.task('watch', function(){
    gulp.watch('stylus/**/**.styl', ['stylus']);
    gulp.watch('js/**.js', ['js']);
});

gulp.task('default', ['stylus']);

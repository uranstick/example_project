'use strict';

const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: {
        // index: './js/index.js',
        // main: './js/main.js',
        // documents: './js/documents.js',
        // search: './js/search.js',
    },
    output: {
        filename: '[name].js',
        path: path.resolve(__dirname, '../static/js'),
    },
    watch: true,
    watchOptions: {
        poll: true
    },

    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader?optional[]=runtime',
                exclude: '/node_modules',
                query: {
                    presets: ['es2015']
                },
            },
            {
                test: /\.html$/,
                loader: 'handlebars-loader',
                exclude: '/node_modules',
            }
        ]
    },
    plugins: [
        new webpack.optimize.UglifyJsPlugin({
            minimize: true
        })
    ]
}

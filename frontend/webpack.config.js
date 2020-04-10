const path = require('path')
const { readdirSync } = require('fs')
const HtmlWebPackPlugin = require('html-webpack-plugin');

const createHtmlWebPackPlugins = source =>
  readdirSync(source, { withFileTypes: true })
    .filter(entry => entry.isDirectory())
    .map(entry => 
      new HtmlWebPackPlugin({
        template: path.resolve(__dirname, `${source}/${entry.name}/${entry.name}.html`),
        filename: `${entry.name}.html`})
      )

const componentsPlugins = createHtmlWebPackPlugins(path.join(__dirname, 'components'))

module.exports = {
  entry: [
    './main.js'
  ],
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js',
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            "presets": [
              [
                "@babel/preset-env", {
                  "useBuiltIns": "usage",
                  "corejs": 3
                }
              ]
            ]
          }
        },
      }
    ]
  },

  plugins: [
    ...componentsPlugins,
    new HtmlWebPackPlugin({
      template: path.resolve(__dirname, 'index.html'),
      filename: 'index.html'
    })
  ],

  resolve: {
    alias: {
      '@core': path.resolve(__dirname, 'core/'),
      '@components': path.resolve(__dirname, 'components/')
    }
    //modulesDirectories: ['node_modules'],
    //extensions: ['', '.js', '.css']
  },
};

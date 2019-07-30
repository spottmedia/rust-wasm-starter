const path = require('path');

module.exports = {
  entry: "./index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "index.js",
  },
  mode: "development",
  devServer: {
    disableHostCheck: true,
    host: '0.0.0.0',
    port: 8080
  }
};
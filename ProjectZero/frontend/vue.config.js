const { defineConfig } = require('@vue/cli-service')
const static_dir = 'C:/Repositories/ProjectZero/ProjectZero/static/TaskManager'
const template_path = 'C:/Repositories/ProjectZero/ProjectZero/templates/TaskManager/index.html'
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: process.env.NODE_ENV === 'production' ? static_dir : 'dist/', 
  indexPath: process.env.NODE_ENV === 'production' ? template_path : 'index.html',
  assetsDir: '',
  publicPath: process.env.NODE_ENV === 'production' ? 'static' : '/',
})

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // ... другие настройки
  css: {
    loaderOptions: {
      // Удаляем настройки, которые уже есть в postcss.config.js
      // postcss: {
      //   plugins: [
      //     require('tailwindcss'),
      //     require('autoprefixer'),
      //   ],
      // },
    },
  },
});


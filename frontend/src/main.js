import { createApp } from 'vue';
import App from './App.vue';
import './assets/css/tailwind.css';
import router from './router/router';
import store from './store/index'; // Убедитесь, что используется правильный store

createApp(App)
  .use(store)
  .use(router)
  .mount('#app');

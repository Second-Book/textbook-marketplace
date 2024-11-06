import { createApp } from 'vue';
import App from './App.vue';
import './assets/css/tailwind.css';
import router from "./router/router.js";

createApp(App).use(router).mount("#app");

import { createRouter, createWebHistory } from 'vue-router';
import TextbookSearch from '../pages/TextbookSearch.vue';
import Textbook from '../pages/Textbook.vue';


const routes = [
  {
    path: '/textbook/:id',
    name: 'Textbook',
    component: Textbook,
    // props: true
  },
  {
    path: '/',
    name: 'TextbookSearch',
    component: TextbookSearch,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

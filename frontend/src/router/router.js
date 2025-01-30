import { createRouter, createWebHistory } from 'vue-router';
import TextbookSearch from '../pages/TextbookSearch.vue';
import Textbook from '../pages/Textbook.vue';
import Login from '../components/login.vue';
import Signup from '../components/signup.vue';
import NewTextbook from '@/pages/NewTextbook.vue';


const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/textbook/:id',
    name: 'Textbook',
    component: Textbook,
  },
  {
    path: '/newtextbook',
    name: 'NewTextbook',
    component: NewTextbook,
  },
  {
    path: '/textbooks',
    name: 'TextbooksSearch',
    component: TextbookSearch,
  },
  {
    path: '/',
    redirect: '/textbooks',
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

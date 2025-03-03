import { createRouter, createWebHistory } from 'vue-router';
import TextbookSearch from '../pages/TextbookSearch.vue';
import Textbook from '../pages/Textbook.vue';
import Login from '../components/login.vue';
import Signup from '../components/signup.vue';
import NewTextbook from '@/pages/NewTextbook.vue';
import store from '../store/index'; 
import UserProfile from '@/pages/Profile.vue';

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
    path: '/textbooks',
    name: 'TextbooksSearch',
    component: TextbookSearch,
  },
  {
    path: '/new-textbook',
    name: 'NewTextbook',
    component: NewTextbook
  },
  {
    path: '/profile',
    name: 'UserProfile',
    component: UserProfile,
    meta: { requiresAuth: true }
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

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.state.isAuthenticated) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;

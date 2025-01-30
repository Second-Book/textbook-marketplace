import Vue from 'vue';
import Router from 'vue-router';
import Home from '../pages/Home.vue';
import TextbookSearch from '../pages/TextbookSearch.vue';
import Textbook from '../pages/Textbook.vue';
import NewTextbook from '../pages/NewTextbook.vue';
import Profile from '../pages/Profile.vue';
import store from '../store'; // Assuming you have a Vuex store

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/textbooks',
      name: 'TextbookSearch',
      component: TextbookSearch
    },
    {
      path: '/textbook/:id',
      name: 'Textbook',
      component: Textbook
    },
    {
      path: '/new-textbook',
      name: 'NewTextbook',
      component: NewTextbook
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      meta: { requiresAuth: true }
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.state.isAuthenticated) {
      next({ name: 'Home' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;

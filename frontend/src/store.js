import { createStore } from 'vuex';

const store = createStore({
  state: {
    isAuthenticated: false,
  },
  mutations: {
    SET_AUTHENTICATED(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
  },
});

export default store;

import { createStore } from 'vuex';


const store = createStore({
  state: {
    isAuthenticated: !!localStorage.getItem('access_token'),
    user: localStorage.getItem('user_data') ? JSON.parse(localStorage.getItem('user_data')) : null,
  },
  mutations: {
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    setUser(state, user) {
      state.user = user;
      localStorage.setItem('user_data', JSON.stringify(user));
    },
    clearUser(state) {
      state.user = null;
      localStorage.removeItem('user_data');
    },
  },

  actions: {
    logout({ commit }) {
      commit('setAuthentication', false);
      commit('clearUser');
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    },
  },
});

export default store;

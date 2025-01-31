import { createStore } from 'vuex';

const store = createStore({
  state: {
    isAuthenticated: !!localStorage.getItem('access_token'),
    user: JSON.parse(localStorage.getItem('user_data')) || {},
    // ...existing code...
  },
  mutations: {
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    setUser(state, user) {
      state.user = user;
      localStorage.setItem('user_data', JSON.stringify(user));
    },
    // ...existing code...
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await this.$axios.post('/api/auth/login/', credentials);
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        commit('setAuthentication', true);
        commit('setUser', response.data.user);
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },
    logout({ commit }) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('user_data');
      commit('setAuthentication', false);
      commit('setUser', {});
    },
    // ...existing code...
  },
  // ...existing code...
});

export default store;

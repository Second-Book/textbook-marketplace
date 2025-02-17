<template>
  <header class="flex justify-between items-center px-6 py-4 w-full text-white bg-rose-800">
    <div class="flex items-center justify-start w-full max-w-2xl">
      <a href="/textbooks" class="text-2xl font-bold leading-none mr-4">EduMarket</a>
    </div>
    <nav class="flex gap-10 text-xl leading-tight justify-center w-full max-w-2xl">
      <router-link v-if="!isAuthenticated" to="/login" class="focus:outline-none focus:ring-2 focus:ring-white">Sign In</router-link>
      <router-link v-if="!isAuthenticated" to="/signup" class="focus:outline-none focus:ring-2 focus:ring-white">Sign Up</router-link>
      <router-link v-if="isAuthenticated" to="/profile" class="focus:outline-none focus:ring-2 focus:ring-white">Profile</router-link>
      <a v-if="isAuthenticated" @click="handleLogout" class="focus:outline-none focus:ring-2 focus:ring-white">Logout</a>
    </nav>
  </header>
</template>

<script>
import { mapState } from 'vuex';
import authService from '../services/authService';

export default {
  name: 'Navbar',
  computed: {
    ...mapState(['isAuthenticated']),
  },
  methods: {
    async handleLogout() {
      await authService.logout();
      this.$store.commit('setAuthentication', false);
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background-color: #8b0a1a;
}

a {
  color: white;
  text-decoration: none;
  font-size: 1.25rem;
}

a:hover {
  text-decoration: underline;
}

a.mr-4 {
  margin-right: 1rem;
}
</style>

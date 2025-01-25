<template>
  <div id="app">
    <AuthenticatedNavbar v-if="isLoggedIn" />
    <Navbar v-else />
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';
import AuthenticatedNavbar from './components/AuthenticatedNavbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    AuthenticatedNavbar
  },
  computed: {
    isLoggedIn() {
      console.log(this.$store);
      return this.$store.state.isAuthenticated;
    }
  }
};
</script>

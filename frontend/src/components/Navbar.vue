<template>
  <header class="flex justify-between items-center px-6 py-4 w-full text-white bg-rose-800">
    <div class="flex items-center justify-start w-full max-w-2xl">
      <a href="/textbooks" class="text-2xl font-bold leading-none mr-4">EduMarket</a>
    </div>
    <nav class="flex gap-10 text-xl leading-tight justify-center w-full max-w-2xl">
      <a v-if="!isAuthenticated" href="/login" class="focus:outline-none focus:ring-2 focus:ring-white">Sign In</a>
      <a v-if="!isAuthenticated" href="/signup" class="focus:outline-none focus:ring-2 focus:ring-white">Sign Up</a>
      <a v-if="isAuthenticated" href="/profile" class="focus:outline-none focus:ring-2 focus:ring-white">Profile</a>
      <a v-if="isAuthenticated" @click="handleLogout" class="focus:outline-none focus:ring-2 focus:ring-white">Logout</a>
    </nav>
  </header>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'Navbar',
  computed: {
    ...mapState(['isAuthenticated']),
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      this.logout();
      this.$router.push({ name: 'TextbooksSearch' });
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

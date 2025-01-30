<template>
  <div class="flex flex-col items-center py-10 bg-gray-100">
    <h1 class="text-3xl font-bold mb-6">Profile</h1>
    <div class="w-full max-w-lg bg-white p-8 rounded shadow-md">
      <h2 class="text-2xl font-bold mb-4">Welcome, {{ user.username }}</h2>
      <p class="text-lg mb-4">Email: {{ user.email }}</p>
      <router-link to="/new-textbook" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
        Add a New Textbook
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {}
    };
  },
  created() {
    this.fetchUserData();
  },
  methods: {
    async fetchUserData() {
      try {
        const response = await this.$axios.get('/api/users/me/');
        this.user = response.data;
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Add any additional styling here */
</style>

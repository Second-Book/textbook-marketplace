<template>
  <div class="min-h-screen flex items-center justify-center bg-white">
      <div class="bg-white shadow-md rounded p-8 max-w-md w-full mx-auto">
          <h2 class="text-2xl font-bold mb-4 text-blue-900">Login</h2>
          <form @submit.prevent="login" class="space-y-4">
              <div>
                  <label for="username" class="block text-zinc-400 font-bold mb-2">Username:</label>
                  <input id="username" v-model="credentials.username" required class="w-full border border-zinc-300 rounded py-2 px-4 leading-tight focus:outline-none focus:border-zinc-500" />
              </div>
              <div>
                  <label for="password" class="block text-zinc-400 font-bold mb-2">Password:</label>
                  <input id="password" type="password" v-model="credentials.password" required class="w-full border border-zinc-300 rounded py-2 px-4 leading-tight focus:outline-none focus:border-zinc-500" />
              </div>
              <button type="submit" class="bg-red-800 text-white py-2 px-4 rounded hover:bg-red-700 focus:outline-none focus:bg-red-700">Login</button>
          </form>
          <p v-if="errorMessage" class="text-red-500 mt-2">{{ errorMessage }}</p>
      </div>
  </div>
</template>

<script>
import authService from './authetification.js';

export default {
  data() {
      return {
          credentials: {
              username: '',
              password: '',
          },
          errorMessage: ''
      }
  },
  methods: {
      async login() {
          try {
              const response = await authService.login(this.credentials);
              this.$store.commit('setAuthentication', true);
              this.$store.commit('setUser', response.user);
              this.$router.push('/'); // Redirect to the home page
          } catch (error) {
              this.errorMessage = 'Invalid username or password';
          }
      }
  }
};
</script>

<style>
.error {
  color: red;
}
</style>
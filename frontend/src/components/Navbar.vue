<template>
  <header class="flex justify-between items-center px-6 py-4 w-full text-white bg-rose-800">
    <div class="flex items-center justify-start w-full max-w-2xl">
      <a href="/textbooks" class="text-2xl font-bold leading-none">EduMarket</a>
    </div>
    <nav class="flex gap-10 text-xl leading-tight justify-center w-full max-w-2xl">
      <a href="/login" class="focus:outline-none focus:ring-2 focus:ring-white">Sign In</a>
      <a href="/signup" class="focus:outline-none focus:ring-2 focus:ring-white">Sign Up</a>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Navbar',
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
</style>

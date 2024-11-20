<template>
    <header class="flex flex-wrap gap-5 justify-between px-6 py-4 w-full text-white bg-rose-800 max-md:pr-5 max-md:max-w-full">
        <h1 class="text-2xl font-bold leading-none">EduMarket</h1>
        <nav class="flex gap-10 self-start mt-1 text-xl leading-tight text-center">
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
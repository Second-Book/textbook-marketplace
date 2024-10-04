<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="hello container mx-auto p-4 bg-gray-100 rounded-lg shadow-md">
      <h1 class="text-3xl font-bold text-center text-blue-600 mb-4">{{ msg }}</h1>
      <p class="text-center text-gray-700 mb-4">
        For a guide and recipes on how to configure / customize this project,<br>
        check out the
        <a href="https://cli.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">vue-cli documentation</a>.
      </p>
      <h3 class="text-2xl font-semibold text-gray-800 mb-2">Installed CLI Plugins</h3>
      <ul class="list-disc list-inside mb-4">
        <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener" class="text-blue-500 underline">babel</a></li>
        <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener" class="text-blue-500 underline">eslint</a></li>
      </ul>
      <h3 class="text-2xl font-semibold text-gray-800 mb-2">Essential Links</h3>
      <ul class="list-disc list-inside mb-4">
        <li><a href="https://vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">Core Docs</a></li>
        <li><a href="https://forum.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">Forum</a></li>
        <li><a href="https://chat.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">Community Chat</a></li>
        <li><a href="https://twitter.com/vuejs" target="_blank" rel="noopener" class="text-blue-500 underline">Twitter</a></li>
        <li><a href="https://news.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">News</a></li>
      </ul>
      <h3 class="text-2xl font-semibold text-gray-800 mb-2">Ecosystem</h3>
      <ul class="list-disc list-inside">
        <li><a href="https://router.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">vue-router</a></li>
        <li><a href="https://vuex.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">vuex</a></li>
        <li><a href="https://github.com/vuejs/vue-devtools#vue-devtools" target="_blank" rel="noopener" class="text-blue-500 underline">vue-devtools</a></li>
        <li><a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener" class="text-blue-500 underline">vue-loader</a></li>
        <li><a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener" class="text-blue-500 underline">awesome-vue</a></li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<style scoped>
/* Add any additional custom styles here */
</style>

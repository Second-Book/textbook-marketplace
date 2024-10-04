<template>
  <div>
    <noscript>
      <strong>We're sorry but {{ title }} doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <!-- built files will be auto injected -->
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      title: 'Your Title Here'
    }
  }
}
</script>

<style>
/* Add your custom styles here */
</style>

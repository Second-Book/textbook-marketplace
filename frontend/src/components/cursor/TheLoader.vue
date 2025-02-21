<template>
  <div
    v-show="isLoading"
    class="loader-overlay fixed inset-0 flex items-center justify-center"
  >
    <div class="loader-content">
      <div class="spinner animate-spin">◌</div>
      <div class="loader-message">{{ message }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TheLoader',

  computed: {
    isLoading() {
      return this.$store.state.loading.isLoading
    },
    message() {
      return this.$store.state.loading.message || 'Загрузка...'
    }
  }
}
</script>

<style scoped>
.loader-overlay {
  background: rgba(255, 255, 255, 0.9);
  z-index: 9999;
}

.loader-content {
  text-align: center;
}

.spinner {
  font-size: 2em;
  color: #3498db;
  margin-bottom: 8px;
}

.animate-spin {
  animation: spin 1s linear infinite;
}

.loader-message {
  color: #2c3e50;
  font-size: 1.1em;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style> 
<template>
  <div class="rating" :class="sizeClass">
    <div
      v-for="i in 5"
      :key="i"
      class="star"
      :class="{
        'filled': i <= value,
        'half-filled': i - 0.5 === value,
        'clickable': !readonly
      }"
      @click="handleClick(i)"
      @mouseover="handleHover(i)"
      @mouseleave="handleLeave"
    >
      <svg
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
        />
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Rating',

  props: {
    value: {
      type: Number,
      default: 0,
      validator: value => value >= 0 && value <= 5
    },
    readonly: {
      type: Boolean,
      default: false
    },
    size: {
      type: String,
      default: 'medium',
      validator: value => ['small', 'medium', 'large'].includes(value)
    }
  },

  data() {
    return {
      hoverValue: 0
    }
  },

  computed: {
    sizeClass() {
      return `size-${this.size}`
    }
  },

  methods: {
    handleClick(value) {
      if (this.readonly) return
      this.$emit('input', value)
      this.$emit('change', value)
    },

    handleHover(value) {
      if (this.readonly) return
      this.hoverValue = value
    },

    handleLeave() {
      if (this.readonly) return
      this.hoverValue = 0
    }
  }
}
</script>

<style scoped>
.rating {
  display: inline-flex;
  gap: 4px;
}

.star {
  position: relative;
  cursor: default;
}

.star.clickable {
  cursor: pointer;
}

.star svg {
  width: 100%;
  height: 100%;
  fill: #ddd;
  transition: fill 0.2s;
}

.star.filled svg,
.star.half-filled svg {
  fill: #f1c40f;
}

.size-small {
  height: 16px;
}

.size-medium {
  height: 24px;
}

.size-large {
  height: 32px;
}

.star:hover svg {
  fill: #f1c40f;
}

.star:hover ~ .star svg {
  fill: #ddd;
}

.rating:hover .star svg {
  fill: #ddd;
}

.rating:hover .star:hover svg,
.rating:hover .star:hover ~ .star svg {
  fill: #f1c40f;
}
</style> 
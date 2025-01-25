<template>
  <div class="flex flex-col gap-5 p-5 bg-white rounded shadow-md relative">
    <img :src="image" :alt="title" class="object-contain aspect-[0.67] w-[400px]" />
    <button class="details-button absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" @click="$router.push({ name: 'Textbook', params: { id: id } })">
      Details
    </button>
    <h2 class="text-2xl font-bold leading-tight">{{ title }}</h2>
    <p class="text-lg leading-tight">Author: {{ author }}</p>
    <p class="text-lg leading-tight">Publisher: {{ publisher }}</p>
    <p class="text-lg leading-tight">Price: {{ price }}</p>
    <button class="add-to-cart-button" @click="addToCart">
      Add to Cart
    </button>
  </div>
</template>
<script>
import textbookService from '../services/TextbookService.js';

export default {
  name: 'TextbookCard',
  props: {
    id: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    author: {
      type: String,
      required: true,
    },
    publisher: {
      type: String,
      required: true,
    },
    price: {
      type: Number,
      required: true
    },
    school_class: {
      type: String,
      required: true
    },
    image: {
      type: String,
      required: true,
    },
  },
  computed: {
    // formattedPrice(price) {
    //   return Number().toFixed(2);
    // }
  },
  methods: {
    goToTextbookPage() {
      this.$router.push({ name: 'TextbookCard', params: { id: this.id } });
    },
    async fetchTextbooks() {
    try {
      const response = await textbookService.getTextbook(this.id);
      this.textbook = response.data;
      console.log('Fetched textbooks:', this.textbook);
    } catch (error) {
      console.error('Error fetching textbooks:', error);
    }
  },
  },
  created() {
  this.fetchTextbooks();
  },
};
</script>


<style scoped>
.details-button {
  background-color: #000;
  color: #fff;
  padding: 10px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

.add-to-cart-button {
  background-color: #8b0a1a;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

.relative:hover .details-button {
  opacity: 1;
}

.relative:hover .add-to-cart-button {
  opacity: 1;
}
</style>

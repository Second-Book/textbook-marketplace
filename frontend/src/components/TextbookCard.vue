<template>
  <div class="flex flex-col gap-5 p-5 bg-white rounded shadow-md">
    <img :src="image" :alt="title" class="object-contain aspect-[0.67] w-[200px]" />
    <h2 class="text-2xl font-bold leading-tight">{{ title }}</h2>
    <p class="text-lg leading-tight">Author: {{ author }}</p>
    <p class="text-lg leading-tight">Publisher: {{ publisher }}</p>
    <p class="text-lg leading-tight">Price: {{ price }}</p>
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

<template>
    <article class="flex flex-col w-3/12 max-md:ml-0 max-md:w-full">
      <div class="flex overflow-hidden flex-col grow items-start py-4 pr-14 pl-4 text-base text-blue-900 rounded border border-solid shadow-sm max-md:pr-5 max-md:mt-7">
        <!-- <img :src="imageSrc" :alt="title" class="object-contain aspect-[0.67] w-[200px]" /> -->
        <h3 class="mt-4 text-xl font-bold leading-snug">{{ this.title }}</h3>
        <p class="mt-2">Author: {{ this.author }}</p>
        <p class="mt-2">Publisher: {{ this.publisher }}</p>
        <p class="mt-2 font-bold text-red-800">{{ formattedPrice }}</p>
        <button @click="buyNow" class="px-4 py-2 mt-2 text-center text-white bg-red-800 focus:outline-none focus:ring-2 focus:ring-red-600">
          Buy Now
        </button>
      </div>
    </article>
  </template>
  
<script>
// import TextbookCard from '../components/TextbookCard.vue';
import textbookService from '../services/TextbookService.js';

  export default {
    name: 'Textbook',
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
      // imageSrc: {
      //   type: String,
      //   required: true,
      // },
    },
    computed: {
      formattedPrice() {
        let price = this.price;
        if (typeof price !== 'number') {
          price = parseFloat(price);
        }
        return isNaN(price) ? 'Invalid price' : price.toFixed(2);
      }
    },
    methods: {
      buyNow() {//button "buy now" is link to textbook card from textbooksearch page
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

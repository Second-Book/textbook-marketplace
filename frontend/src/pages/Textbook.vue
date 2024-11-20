<template>
  <div class="flex flex-col items-center justify-center h-screen p-10">
    <div class="flex flex-row items-start justify-center mb-4">
      <img :src="image" alt="Textbook Image" class="object-contain h-96 mr-8" />
      <div class="flex flex-col items-start text-base text-black max-w-2xl">
        <h1 class="text-5xl font-bold leading-none mb-4">{{ title }}</h1>
        <dl class="w-full">
          <div class="flex gap-6 mt-4">
            <dt class="font-bold grow">Author:</dt>
            <dd>{{ author }}</dd>
          </div>
          <div class="flex gap-6 mt-4">
            <dt class="font-bold grow">Publisher:</dt>
            <dd>{{ publisher }}</dd>
          </div>
          <div class="flex mt-4">
            <dt class="font-bold grow">School Class:</dt>
            <dd>{{ school_class }}</dd>
          </div>
          <div class="flex gap-6 mt-4">
            <dt class="font-bold grow">Date Added:</dt>
            <dd>{{ date_added }}</dd>
          </div>
          <div class="flex mt-4">
            <dt class="font-bold grow">Price:</dt>
            <dd>{{ price }} din.</dd>
          </div>
        </dl>
        <section class="w-full mt-8">
          <h3 class="font-bold mt-4">Contacts:</h3>
          <ul class="list-none p-0">
            <span>seller: {{ seller }}</span>
          </ul>
        </section>
      </div>
    </div>
    <button class="bg-red-800 text-white px-8 py-4 mt-8" @click="addToCart">Add to Cart</button>
  </div>
</template>

<script>
import textbookService from '../services/TextbookService.js';


export default {
  name: 'Textbook',
  components: {
  },
  data() {
    return {
      key: null,
      title: null,
      author: null,
      publisher: null,
      price: null,
      image: null,
      whatsappUrl: 'https://cdn.builder.io/api/v1/image/assets/f4c1588a1e044eaca829846f2a5403d3/b18ff27f2b78f4e9aa6c8a35213e6b106a72321e60a304ddc154e27d7b7c16b8?apiKey=f4c1588a1e044eaca829846f2a5403d3&',
      telefonUrl: 'https://cdn.builder.io/api/v1/image/assets/f4c1588a1e044eaca829846f2a5403d3/4b444aee593aca3ef65b8c5754d7df1cf22b4aef792e21d8d86c495b32ce79a2?apiKey=f4c1588a1e044eaca829846f2a5403d3&',
      viberUrl: 'https://cdn.builder.io/api/v1/image/assets/f4c1588a1e044eaca829846f2a5403d3/cbbc97949bf833e15266f0be56b1ee56fa57a024e8c6d69e2358458c4cae81b2?apiKey=f4c1588a1e044eaca829846f2a5403d3&',
    }
    },
  created() {
    this.id = this.$route.params.id;
    textbookService.getTextbook(this.id)
      .then(response => {
        this.title = response.data.title;
        this.author = response.data.author;
        this.publisher = response.data.publisher;
        this.price = response.data.price;
        this.seller = response.data.seller;
        this.image = `http://localhost:8000${response.data.image}`})
      .catch(error => {
        console.error('Error fetching textbook:', error);
      });
  }
};
</script>

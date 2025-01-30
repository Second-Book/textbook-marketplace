<template>
  <div class="flex flex-col pb-5 bg-white">
    <main class="flex flex-col items-center px-6 mt-6 w-full max-md:pl-5 max-md:max-w-full">
      <h2 class="self-center text-3xl font-bold leading-tight text-blue-900 text-center w-2/3">Find Cheap Textbooks</h2>
      <form class="flex flex-wrap gap-4 mt-4 text-base max-md:mr-2.5 max-md:max-w-full w-2/3 mx-auto" @submit.prevent="searchTextbooks">
        <label for="searchInput" class="sr-only">Search for textbooks</label>
        <input
          id="searchInput"
          type="text"
          placeholder="Search for textbooks..."
          class="overflow-hidden p-2.5 bg-white rounded-lg border border-blue-900 border-solid text-zinc-400 max-md:pr-5 max-md:max-w-full w-full"
          v-model="searchQuery"
        />
        <label for="sortCriteria" class="sr-only">Sort by</label>
        <select id="sortCriteria" v-model="sortCriteria" class="p-2.5 bg-white rounded-lg border border-blue-900 border-solid text-zinc-400">
          <option value="title">Title</option>
          <option value="school_class">School_Class</option>
          <option value="publisher">Publisher</option>
          <option value="price">Price</option>
        </select>
        <button type="submit" class="px-4 py-2 text-center text-white whitespace-nowrap bg-red-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-600">
          Search
        </button>
      </form>
      <section class="mt-14 max-md:mt-10 max-md:max-w-full w-2/3 mx-auto">
        <div class="textbook-grid">

            <TextbookCard
            v-for="(textbook, index) in textbooks"
            :key="index"
            :image="textbook.image.preview"
            :title="textbook.title"
            :author="textbook.author"
            :publisher="textbook.publisher"
            :price="parseFloat(textbook.price).toFixed(2) + '€'"
            :id="textbook.id"
          />
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import TextbookCard from '../components/TextbookCard.vue';
import textbookService from '../services/TextbookService.js';

export default {
  name: 'TextbookSearch',
  components: {
    TextbookCard
  },
  
  data() {
    return {
      searchQuery: '',
      sortCriteria: 'title',
      textbooks: [],
    };
  },
  computed: {
    // formattedPrice(price) {
    //   return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(price);
    // },
    sortedTextbooks() {
      if (this.sortCriteria === 'price') {
        return [...this.textbooks].sort((a, b) => a.price - b.price);
      }

      if (this.sortCriteria === 'school_class') {
        return [...this.textbooks].sort((a, b) => a.school_class.localeCompare(b.school_class));
      }

      if (this.sortCriteria === 'author') {
        return [...this.textbooks].sort((a, b) => a.author.localeCompare(b.author));
      } 
      return [...this.textbooks].sort((a, b) => a.price - b.price);

    },
    },

  methods: {
    async fetchTextbooks() {
      try {
        const response = await textbookService.getTextbooks();
        this.textbooks = response.data;
        
        for (let textbook of this.textbooks) {
          textbook.price = parseFloat(textbook.price).toFixed(2);
          textbook.image.preview = `http://localhost:8000${textbook.image.preview}`;
        }
        console.log('Fetched textbooks:', this.textbooks);
      } catch (error) {
        console.error('Error fetching textbooks:', error);
      }
    },
    searchTextbooks() {
      if (this.searchQuery === '') {
        this.fetchTextbooks();
        return;
      }
      this.textbooks = this.textbooks.filter(textbook => {
        return (
          textbook.price.toString().includes(this.searchQuery) ||
          textbook.school_class.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          textbook.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          textbook.author.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          textbook.publisher.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      });
    }
  },
  watch: {
    searchQuery() {
      this.searchTextbooks();
    },
    sortCriteria() {
      this.textbooks = this.sortedTextbooks;
    }
  },
  created() {
    this.fetchTextbooks();
  }
};

</script>

<style scoped>
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
.textbook-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 20px;
}
</style>

<template>
  <div>
    <header class="bg-burgundy-600 py-6 shadow-md">
      <div class="container mx-auto flex justify-between items-center px-4">
        <div class="flex items-center">
          <img src="path/to/learnsell-logo.png" alt="LearnSell Logo" class="h-10 mr-2" />
          <h1 class="text-3xl font-bold text-blue-900">Book Catalog</h1>
        </div>
        <nav>
          <ul class="flex space-x-6">
            <li><a href="#" class="text-white hover:text-blue-900">Home</a></li>
            <li><a href="#" class="text-white hover:text-blue-900">Categories</a></li>
            <li><a href="#" class="text-white hover:text-blue-900">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <main class="container mx-auto px-4 py-8">
      <div class="mb-6 flex justify-between items-center">
        <h2 class="text-2xl font-semibold text-blue-900">Featured Books</h2>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search..." 
          class="border rounded px-4 py-2" 
        />
      </div>

      <div class="flex mb-4">
        <select v-model="selectedCategory" class="border rounded px-4 py-2 mr-4">
          <option value="">All Categories</option>
          <option value="gymnasium">Gymnasium Textbooks</option>
          <option value="primary">Primary School Textbooks</option>
          <option value="college">College</option>
          <option value="children">Children's Books</option>
        </select>
        <button 
          @click="filterBooks" 
          class="bg-burgundy-600 text-white px-4 py-2 rounded hover:bg-burgundy-700"
        >
          Filter
        </button>
      </div>

      <section class="mb-12">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div 
            v-for="book in filteredBooks" 
            :key="book.id" 
            class="bg-gray-50 p-4 rounded shadow"
          >
            <img 
              :src="book.cover" 
              alt="Cover of a book" 
              class="w-full h-48 object-cover mb-4" 
            />
            <h3 class="text-lg font-semibold text-blue-900">{{ book.title }}</h3>
            <p class="text-gray-600">Author: {{ book.author }}</p>
            <p class="text-gray-600">Price: ${{ book.price }}</p>
          </div>
        </div>
      </section>

      <section class="mb-12">
        <h2 class="text-2xl font-semibold text-blue-900 mb-6">Informative Blocks</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-gray-50 p-6 rounded shadow">
            <h3 class="text-xl font-semibold mb-4">Book Reviews</h3>
            <p class="text-gray-600">Get insights and reviews from experts and readers.</p>
          </div>
          <div class="bg-gray-50 p-6 rounded shadow">
            <h3 class="text-xl font-semibold mb-4">Educational Articles</h3>
            <p class="text-gray-600">Explore articles on educational topics to enhance your learning.</p>
          </div>
          <div class="bg-gray-50 p-6 rounded shadow">
            <h3 class="text-xl font-semibold mb-4">Tips for Students</h3>
            <p class="text-gray-600">Discover useful tips and strategies for effective learning.</p>
          </div>
        </div>
      </section>
    </main>

    <footer class="bg-gray-100 py-6">
      <div class="container mx-auto px-4 text-center">
        <p class="text-gray-600">&copy; 2023 Book Catalog. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedCategory: '',
      books: [
        { id: 1, title: "Used Textbook 1", author: "John Doe", price: 20, cover: "https://placehold.co/150x200", category: "gymnasium" },
        { id: 2, title: "Children's Book 1", author: "Jane Smith", price: 15, cover: "https://placehold.co/150x200", category: "children" },
        { id: 3, title: "Used Textbook 2", author: "Emily Johnson", price: 18, cover: "https://placehold.co/150x200", category: "gymnasium" },
        { id: 4, title: "Children's Book 2", author: "Michael Brown", price: 12, cover: "https://placehold.co/150x200", category: "children" },
        // Add more book objects as needed
      ],
    };
  },
  computed: {
    filteredBooks() {
      return this.books.filter(book => {
        const matchesCategory = this.selectedCategory ? book.category === this.selectedCategory : true;
        const matchesSearch = book.title.toLowerCase().includes(this.searchQuery.toLowerCase());
        return matchesCategory && matchesSearch;
      });
    }
  },
  methods: {
    filterBooks() {
      // This method can be expanded if you want to perform additional logic when filtering
    }
  }
};
</script>

<style scoped>
/* You can add additional styling here if needed */
</style>

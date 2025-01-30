<template>
  <div class="flex flex-col items-center py-10 bg-gray-100">
    <h1 class="text-3xl font-bold mb-6">Add a New Textbook</h1>
    <form class="w-full max-w-lg bg-white p-8 rounded shadow-md" @submit.prevent="submitForm">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="title">Title</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="title" type="text" v-model="form.title" required>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="author">Author</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="author" type="text" v-model="form.author" required>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="school_class">School Class</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="school_class" type="text" v-model="form.school_class" required>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="publisher">Publisher</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="publisher" type="text" v-model="form.publisher" required>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="price">Price</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="price" type="number" v-model="form.price" required>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="condition">Condition</label>
        <select class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="condition" v-model="form.condition" required>
          <option value="New">New</option>
          <option value="Used - Excellent">Used - Excellent</option>
          <option value="Used - Good">Used - Good</option>
          <option value="Used - Fair">Used - Fair</option>
        </select>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="description">Description</label>
        <textarea class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="description" v-model="form.description"></textarea>
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="image">Image</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="image" type="file" @change="handleFileUpload">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="whatsapp_contact">WhatsApp Contact</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="whatsapp_contact" type="text" v-model="form.whatsapp_contact">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="viber_contact">Viber Contact</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="viber_contact" type="text" v-model="form.viber_contact">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="telegram_contact">Telegram Contact</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="telegram_contact" type="text" v-model="form.telegram_contact">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="phone_contact">Phone Contact</label>
        <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="phone_contact" type="text" v-model="form.phone_contact">
      </div>
      <div class="flex items-center justify-between">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
          Add Textbook
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        title: '',
        author: '',
        school_class: '',
        publisher: '',
        price: '',
        condition: 'Used - Good',
        description: '',
        image: null,
        whatsapp_contact: '',
        viber_contact: '',
        telegram_contact: '',
        phone_contact: ''
      }
    };
  },
  methods: {
    handleFileUpload(event) {
      this.form.image = event.target.files[0];
    },
    async submitForm() {
      const formData = new FormData();
      for (const key in this.form) {
        formData.append(key, this.form[key]);
      }
      try {
        await this.$axios.post('/api/textbooks/', formData);
        this.$router.push('/textbooks');
      } catch (error) {
        console.error('Error adding textbook:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Add any additional styling here */
</style>

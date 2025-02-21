<template>
    <div class="user-profile max-w-4xl mx-auto p-6">
      <div v-if="loading" class="text-center py-10">
        <TheLoader />
      </div>
  
      <div v-else-if="error" class="text-center py-10 text-red-600">
        <p>{{ error }}</p>
        <button @click="loadProfile" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded">
          Try Again
        </button>
      </div>
  
      <div v-else class="profile-content">
        <div class="profile-header flex gap-6 mb-8">
          <div class="avatar-wrapper relative">
            <img
              :src="user.avatar || '/images/default-avatar.png'"
              :alt="user.username"
              class="w-32 h-32 rounded-full object-cover"
            >
            <button
              v-if="isOwnProfile"
              class="absolute bottom-0 left-1/2 transform -translate-x-1/2 px-3 py-1 bg-black bg-opacity-60 text-white rounded-full text-sm"
              @click="triggerAvatarUpload"
            >
              Change
            </button>
            <input
              ref="avatarInput"
              type="file"
              accept="image/*"
              class="hidden"
              @change="handleAvatarChange"
            >
          </div>
  
          <div class="user-info flex-1">
            <h2 class="text-2xl font-bold">{{ user.username }}</h2>
            <p class="text-gray-600">Joined on {{ formatDate(user.createdAt) }}</p>
            <div class="rating flex items-center gap-2" v-if="user.rating">
              <Rating :value="user.rating" readonly size="small" />
              <span class="text-gray-600 text-sm">({{ user.reviewsCount }})</span>
            </div>
          </div>
  
          <div v-if="isOwnProfile" class="profile-actions">
            <button
              class="px-4 py-2 bg-blue-500 text-white rounded"
              @click="startEditing"
            >
              Edit Profile
            </button>
          </div>
        </div>
  
        <div v-if="isEditing" class="edit-form mb-8">
          <div class="form-group mb-4">
            <label for="name" class="block text-gray-700 font-medium mb-2">Name</label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              class="w-full px-3 py-2 border rounded"
            >
          </div>
  
          <div class="form-group mb-4">
            <label for="bio" class="block text-gray-700 font-medium mb-2">Bio</label>
            <textarea
              id="bio"
              v-model="form.bio"
              rows="4"
              class="w-full px-3 py-2 border rounded"
            ></textarea>
          </div>
  
          <div class="form-group mb-4">
            <label for="contacts" class="block text-gray-700 font-medium mb-2">Contacts</label>
            <input
              id="contacts"
              v-model="form.contacts"
              type="text"
              class="w-full px-3 py-2 border rounded"
            >
          </div>
  
          <div class="form-actions flex justify-end gap-4">
            <button
              class="px-4 py-2 bg-gray-200 text-gray-700 rounded"
              @click="cancelEditing"
            >
              Cancel
            </button>
            <button
              class="px-4 py-2 bg-blue-500 text-white rounded"
              :disabled="isSaving"
              @click="saveProfile"
            >
              {{ isSaving ? 'Saving...' : 'Save' }}
            </button>
          </div>
        </div>
  
        <div v-else class="profile-details">
          <div class="detail-section mb-6" v-if="user.name">
            <h3 class="text-lg font-medium text-gray-700">Name</h3>
            <p class="text-gray-700">{{ user.name }}</p>
          </div>
  
          <div class="detail-section mb-6" v-if="user.bio">
            <h3 class="text-lg font-medium text-gray-700">Bio</h3>
            <p class="text-gray-700">{{ user.bio }}</p>
          </div>
  
          <div class="detail-section mb-6" v-if="user.contacts">
            <h3 class="text-lg font-medium text-gray-700">Contacts</h3>
            <p class="text-gray-700">{{ user.contacts }}</p>
          </div>
  
          <div class="detail-section mb-6">
            <h3 class="text-lg font-medium text-gray-700">Statistics</h3>
            <div class="stats flex gap-8">
              <div class="stat-item text-center">
                <span class="block text-2xl font-bold text-gray-700">{{ user.textbooksCount }}</span>
                <span class="text-gray-600">Textbooks</span>
              </div>
              <div class="stat-item text-center">
                <span class="block text-2xl font-bold text-gray-700">{{ user.salesCount }}</span>
                <span class="text-gray-600">Sales</span>
              </div>
              <div class="stat-item text-center">
                <span class="block text-2xl font-bold text-gray-700">{{ user.reviewsCount }}</span>
                <span class="text-gray-600">Reviews</span>
              </div>
            </div>
          </div>
        </div>
  
        <div class="textbooks-section mt-8">
          <h3 class="text-lg font-medium text-gray-700">My Textbooks</h3>
          
          <div v-if="loading" class="text-center py-4">
            <TheLoader />
          </div>

          <div v-else-if="error" class="text-red-600 py-4">
            {{ error }}
          </div>

          <div v-else-if="!textbooks.length" class="text-gray-500 py-4">
            No textbooks found
          </div>

          <div v-else class="textbooks-list mt-4 space-y-4">
            <div v-for="textbook in textbooks" 
                :key="textbook.id"
                class="textbook-item p-4 border rounded-lg hover:shadow-md transition-shadow">
              <div class="flex justify-between items-start">
                <div>
                  <h4 class="font-medium text-lg">{{ textbook.title }}</h4>
                  <p class="text-gray-600">Author: {{ textbook.author }}</p>
                  <p class="text-gray-600">Grade: {{ textbook.grade }}</p>
                  <p class="text-gray-600">Price: ${{ textbook.price }}</p>
                  <p class="text-sm text-gray-500">Added: {{ formatDate(textbook.createdAt) }}</p>
                </div>
                <div class="flex space-x-2">
                  <button 
                    @click="editTextbook(textbook)"
                    class="px-3 py-1 text-blue-600 hover:bg-blue-50 rounded">
                    Edit
                  </button>
                  <button 
                    @click="deleteTextbook(textbook.id)"
                    class="px-3 py-1 text-red-600 hover:bg-red-50 rounded">
                    Delete
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        </div>
  
        <router-link to="/new-textbook" class="mt-8 inline-block px-4 py-2 bg-blue-500 text-white rounded">
          Add a New Textbook
        </router-link>
  </div>
</template>
  
<script>
import textbookService from '../services/TextbookService.js';
import { mapState } from 'vuex';

export default {
  name: 'UserProfile',

  components: {
    Rating: () => import('@/components/cursor/Rating.vue'),
    TheLoader: () => import('@/components/cursor/TheLoader.vue')
  },

  data() {
    return {
      loading: true,
      error: null,
      textbooks: [],
      isEditing: false,
      isSaving: false,
      form: {
        name: '',
        bio: '',
        contacts: ''
      }
    }
  },

  computed: {
    ...mapState(['user']),
    isOwnProfile() {
      return true // Always true in cabinet
    }
  },

  methods: {
    async loadTextbooks() {
      try {
        this.loading = true;
        const username = JSON.parse(localStorage.getItem('user_data')).username;
        const response = await textbookService.getUserTextbooks(username);
        this.textbooks = response.data;
      } catch (error) {
        this.error = 'Failed to load textbooks';
        console.error(error);
      } finally {
        this.loading = false;
      }
    },

    editTextbook(textbook) {
      this.$router.push(`/edit-textbook/${textbook.id}`);
    },

    async deleteTextbook(id) {
      if (!confirm('Are you sure you want to delete this textbook?')) return;
      
      try {
        await this.$store.dispatch('textbooks/deleteTextbook', id);
        await this.loadTextbooks();
        this.$store.dispatch('snackbar/show', {
          message: 'Textbook deleted successfully',
          color: 'success'
        });
      } catch (error) {
        this.$store.dispatch('snackbar/show', {
          message: 'Failed to delete textbook',
          color: 'error'
        });
      }
    },
    async loadProfile() {
      this.loading = true
      this.error = null

      try {
        if (!this.user) {
          throw new Error('User not authenticated')
        }

        // Initialize form with current user data
        this.form = {
          name: this.user.name || '',
          bio: this.user.bio || '',
          contacts: this.user.contacts || ''
        }
      } catch (error) {
        this.error = 'Error loading profile'
        console.error(error)
      } finally {
        this.loading = false
      }
    },

    formatDate(date) {
      return new Date(date).toLocaleString('en', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      })
    },

    startEditing() {
      this.isEditing = true
    },

    cancelEditing() {
      this.isEditing = false
      this.form = {
        name: this.user.name || '',
        bio: this.user.bio || '',
        contacts: this.user.contacts || ''
      }
    },

    async saveProfile() {
      this.isSaving = true

      try {
        const updatedProfile = await this.$store.dispatch('profile/update', {
          ...this.form
        })

        this.$store.commit('setUser', {
          ...this.user,
          ...updatedProfile
        })

        this.isEditing = false
        this.$store.dispatch('snackbar/show', {
          message: 'Profile updated',
          color: 'success'
        })
      } catch (error) {
        this.$store.dispatch('snackbar/show', {
          message: 'Error updating profile',
          color: 'error'
        })
      } finally {
        this.isSaving = false
      }
    },

    triggerAvatarUpload() {
      this.$refs.avatarInput.click()
    },

    async handleAvatarChange(event) {
      const file = event.target.files[0]
      if (!file) return

      try {
        const formData = new FormData()
        formData.append('avatar', file)

        const updatedProfile = await this.$store.dispatch('profile/updateAvatar', formData)
        
        this.$store.commit('setUser', {
          ...this.user,
          avatar: updatedProfile.avatar
        })

        this.$store.dispatch('snackbar/show', {
          message: 'Avatar updated',
          color: 'success'
        })
      } catch (error) {
        this.$store.dispatch('snackbar/show', {
          message: 'Error updating avatar',
          color: 'error'
        })
      }
    }
  },

  created() {
    this.loadProfile();
    this.loadTextbooks();
  }
}
</script>
  
  <style scoped>
  .user-profile {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .loading,
  .error {
    text-align: center;
    padding: 40px;
    color: #2c3e50;
  }
  
  .error {
    color: #e74c3c;
  }
  
  .retry-btn {
    margin-top: 16px;
    padding: 10px 20px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .profile-header {
    display: flex;
    gap: 24px;
    margin-bottom: 32px;
  }
  
  .avatar-wrapper {
    position: relative;
  }
  
  .avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .change-avatar-btn {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    padding: 4px 12px;
    background: rgba(0, 0, 0, 0.6);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 0.9em;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .change-avatar-btn:hover {
    background: rgba(0, 0, 0, 0.8);
  }
  
  .user-info {
    flex: 1;
  }
  
  .username {
    margin: 0 0 4px;
    font-size: 1.5em;
    color: #2c3e50;
  }
  
  .joined-date {
    margin: 0 0 8px;
    color: #7f8c8d;
    font-size: 0.9em;
  }
  
  .rating {
    display: flex;
    align-items: center;
    gap: 4px;
  }
  
  .reviews-count {
    color: #7f8c8d;
    font-size: 0.9em;
  }
  
  .edit-btn {
    padding: 8px 16px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .edit-btn:hover {
    background: #2980b9;
  }
  
  .edit-form {
    margin-bottom: 32px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 8px;
    color: #2c3e50;
    font-weight: 500;
  }
  
  input,
  textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1em;
  }
  
  textarea {
    resize: vertical;
    min-height: 100px;
  }
  
  .form-actions {
    display: flex;
    gap: 12px;
    justify-content: flex-end;
  }
  
  .save-btn,
  .cancel-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 1em;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .save-btn {
    background: #3498db;
    color: white;
  }
  
  .save-btn:hover:not(:disabled) {
    background: #2980b9;
  }
  
  .save-btn:disabled {
    background: #95a5a6;
    cursor: not-allowed;
  }
  
  .cancel-btn {
    background: #f8f9fa;
    color: #2c3e50;
  }
  
  .cancel-btn:hover {
    background: #e9ecef;
  }
  
  .detail-section {
    margin-bottom: 24px;
  }
  
  .detail-section h3 {
    margin: 0 0 8px;
    font-size: 1.1em;
    color: #2c3e50;
  }
  
  .detail-section p {
    margin: 0;
    color: #2c3e50;
    line-height: 1.5;
  }
  
  .stats {
    display: flex;
    gap: 32px;
  }
  
  .stat-item {
    text-align: center;
  }
  
  .stat-value {
    display: block;
    font-size: 1.5em;
    font-weight: 500;
    color: #2c3e50;
  }
  
  .stat-label {
    color: #7f8c8d;
    font-size: 0.9em;
  }
  
  .textbooks-section {
    margin-top: 32px;
  }
  
  .textbooks-section h3 {
    margin: 0 0 16px;
    font-size: 1.2em;
    color: #2c3e50;
  }
  
  .user-textbooks {
    margin-top: 16px;
  }
  
  .hidden {
    display: none;
  }
  .textbooks-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  }

  .textbook-item {
    background: white;
    transition: all 0.2s;
  }

  .textbook-item:hover {
    transform: translateY(-2px);
  }
  
  @media (max-width: 768px) {
    .profile-header {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
  
    .stats {
      justify-content: center;
    }
  }
  </style>

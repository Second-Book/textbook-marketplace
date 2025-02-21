<template>
  <div class="user-profile">
    <div v-if="loading" class="loading">
      <TheLoader />
    </div>

    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
      <button @click="loadProfile" class="retry-btn">
        Попробовать снова
      </button>
    </div>

    <div v-else class="profile-content">
      <div class="profile-header">
        <div class="avatar-wrapper">
          <img
            :src="user.avatar || '/images/default-avatar.png'"
            :alt="user.username"
            class="avatar"
          >
          <button
            v-if="isOwnProfile"
            class="change-avatar-btn"
            @click="triggerAvatarUpload"
          >
            Изменить
          </button>
          <input
            ref="avatarInput"
            type="file"
            accept="image/*"
            class="hidden"
            @change="handleAvatarChange"
          >
        </div>

        <div class="user-info">
          <h2 class="username">{{ user.username }}</h2>
          <p class="joined-date">
            На сайте с {{ formatDate(user.createdAt) }}
          </p>
          <div class="rating" v-if="user.rating">
            <Rating :value="user.rating" readonly size="small" />
            <span class="reviews-count">({{ user.reviewsCount }})</span>
          </div>
        </div>

        <div v-if="isOwnProfile" class="profile-actions">
          <button
            class="edit-btn"
            @click="startEditing"
          >
            Редактировать профиль
          </button>
        </div>
      </div>

      <div v-if="isEditing" class="edit-form">
        <div class="form-group">
          <label for="name">Имя</label>
          <input
            id="name"
            v-model="form.name"
            type="text"
          >
        </div>

        <div class="form-group">
          <label for="bio">О себе</label>
          <textarea
            id="bio"
            v-model="form.bio"
            rows="4"
          ></textarea>
        </div>

        <div class="form-group">
          <label for="contacts">Контакты</label>
          <input
            id="contacts"
            v-model="form.contacts"
            type="text"
          >
        </div>

        <div class="form-actions">
          <button
            class="cancel-btn"
            @click="cancelEditing"
          >
            Отмена
          </button>
          <button
            class="save-btn"
            :disabled="isSaving"
            @click="saveProfile"
          >
            {{ isSaving ? 'Сохранение...' : 'Сохранить' }}
          </button>
        </div>
      </div>

      <div v-else class="profile-details">
        <div class="detail-section" v-if="user.name">
          <h3>Имя</h3>
          <p>{{ user.name }}</p>
        </div>

        <div class="detail-section" v-if="user.bio">
          <h3>О себе</h3>
          <p>{{ user.bio }}</p>
        </div>

        <div class="detail-section" v-if="user.contacts">
          <h3>Контакты</h3>
          <p>{{ user.contacts }}</p>
        </div>

        <div class="detail-section">
          <h3>Статистика</h3>
          <div class="stats">
            <div class="stat-item">
              <span class="stat-value">{{ user.textbooksCount }}</span>
              <span class="stat-label">Учебников</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{{ user.salesCount }}</span>
              <span class="stat-label">Продаж</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{{ user.reviewsCount }}</span>
              <span class="stat-label">Отзывов</span>
            </div>
          </div>
        </div>
      </div>

      <div class="textbooks-section">
        <h3>Учебники пользователя</h3>
        <TextbookGrid
          :filters="{ userId: user.id }"
          class="user-textbooks"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',

  components: {
    Rating: () => import('./Rating.vue'),
    TextbookGrid: () => import('./TextbookGrid.vue'),
    TheLoader: () => import('./TheLoader.vue')
  },

  props: {
    userId: {
      type: [Number, String],
      required: true
    }
  },

  data() {
    return {
      user: null,
      loading: true,
      error: null,
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
    isOwnProfile() {
      return this.userId === this.$store.getters['auth/user']?.id
    }
  },

  methods: {
    async loadProfile() {
      this.loading = true
      this.error = null

      try {
        const response = await this.$store.dispatch('profile/fetch', this.userId)
        this.user = response
        this.form = {
          name: this.user.name || '',
          bio: this.user.bio || '',
          contacts: this.user.contacts || ''
        }
      } catch (error) {
        this.error = 'Ошибка при загрузке профиля'
        console.error(error)
      } finally {
        this.loading = false
      }
    },

    formatDate(date) {
      return new Date(date).toLocaleString('ru', {
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

        this.user = {
          ...this.user,
          ...updatedProfile
        }

        this.isEditing = false
        this.$store.dispatch('snackbar/show', {
          message: 'Профиль обновлен',
          color: 'success'
        })
      } catch (error) {
        this.$store.dispatch('snackbar/show', {
          message: 'Ошибка при обновлении профиля',
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
        this.user.avatar = updatedProfile.avatar

        this.$store.dispatch('snackbar/show', {
          message: 'Аватар обновлен',
          color: 'success'
        })
      } catch (error) {
        this.$store.dispatch('snackbar/show', {
          message: 'Ошибка при обновлении аватара',
          color: 'error'
        })
      }
    }
  },

  created() {
    this.loadProfile()
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
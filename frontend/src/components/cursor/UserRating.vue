<template>
  <div class="user-rating">
    <div v-if="loading" class="loading">
      <TheLoader />
    </div>

    <div v-else-if="error" class="error">
      <p>{{ error }}</p>
      <button @click="loadRating" class="retry-btn">
        Попробовать снова
      </button>
    </div>

    <div v-else class="rating-content">
      <div class="rating-header">
        <div class="average-rating">
          <span class="rating-value">{{ rating.average.toFixed(1) }}</span>
          <Rating
            :value="rating.average"
            readonly
            size="large"
          />
          <span class="total-reviews">
            {{ rating.total }} {{ pluralize(rating.total, ['отзыв', 'отзыва', 'отзывов']) }}
          </span>
        </div>

        <div class="rating-distribution">
          <div
            v-for="i in 5"
            :key="i"
            class="rating-bar"
          >
            <span class="rating-label">{{ i }} ★</span>
            <div class="bar-wrapper">
              <div
                class="bar"
                :style="{ width: `${getPercentage(i)}%` }"
              ></div>
            </div>
            <span class="rating-count">{{ getCount(i) }}</span>
          </div>
        </div>
      </div>

      <div v-if="canRate" class="rating-form">
        <h4>Оставить отзыв</h4>
        <div class="form-group">
          <Rating
            v-model="form.rating"
            size="medium"
          />
        </div>
        <div class="form-group">
          <textarea
            v-model="form.text"
            class="review-text"
            :class="{ 'has-error': errors.text }"
            placeholder="Напишите ваш отзыв..."
            rows="4"
          ></textarea>
          <span v-if="errors.text" class="error-message">
            {{ errors.text }}
          </span>
        </div>
        <div class="form-actions">
          <button
            type="button"
            class="submit-btn"
            :disabled="isSubmitting"
            @click="submitReview"
          >
            {{ isSubmitting ? 'Отправка...' : 'Отправить' }}
          </button>
        </div>
      </div>

      <div class="reviews-list">
        <div
          v-for="review in reviews"
          :key="review.id"
          class="review-item"
        >
          <div class="review-header">
            <div class="reviewer-info">
              <img
                :src="review.reviewer.avatar || '/images/default-avatar.png'"
                :alt="review.reviewer.username"
                class="reviewer-avatar"
              >
              <span class="reviewer-name">{{ review.reviewer.username }}</span>
            </div>
            <div class="review-meta">
              <Rating
                :value="review.rating"
                readonly
                size="small"
              />
              <span class="review-date">
                {{ formatDate(review.createdAt) }}
              </span>
            </div>
          </div>
          <div class="review-text">{{ review.text }}</div>
        </div>

        <div
          v-if="hasMore"
          class="load-more"
        >
          <button
            class="load-more-btn"
            :disabled="loadingMore"
            @click="loadMore"
          >
            {{ loadingMore ? 'Загрузка...' : 'Загрузить еще' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserRating',

  components: {
    TheLoader: () => import('./TheLoader.vue'),
    Rating: () => import('./Rating.vue')
  },

  props: {
    userId: {
      type: [Number, String],
      required: true
    },
    canRate: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      loading: true,
      loadingMore: false,
      isSubmitting: false,
      error: null,
      rating: {
        average: 0,
        total: 0,
        distribution: []
      },
      reviews: [],
      page: 1,
      hasMore: false,
      form: {
        rating: 0,
        text: ''
      },
      errors: {
        text: null
      }
    }
  },

  methods: {
    async loadRating() {
      this.loading = true
      this.error = null

      try {
        const response = await this.$store.dispatch('reviews/fetchUserRating', {
          userId: this.userId,
          page: 1
        })
        
        this.rating = response.rating
        this.reviews = response.reviews
        this.hasMore = response.hasMore
        this.page = 1
      } catch (error) {
        this.error = 'Ошибка при загрузке рейтинга'
        console.error(error)
      } finally {
        this.loading = false
      }
    },

    async loadMore() {
      this.loadingMore = true

      try {
        const response = await this.$store.dispatch('reviews/fetchUserRating', {
          userId: this.userId,
          page: this.page + 1
        })
        
        this.reviews.push(...response.reviews)
        this.hasMore = response.hasMore
        this.page++
      } catch (error) {
        this.$store.dispatch('snackbar/show', {
          message: 'Ошибка при загрузке отзывов',
          color: 'error'
        })
      } finally {
        this.loadingMore = false
      }
    },

    getCount(rating) {
      return this.rating.distribution.find(d => d.rating === rating)?.count || 0
    },

    getPercentage(rating) {
      const count = this.getCount(rating)
      return this.rating.total ? (count / this.rating.total * 100) : 0
    },

    validateForm() {
      this.errors = {
        text: null
      }

      let isValid = true

      if (!this.form.rating) {
        this.$store.dispatch('snackbar/show', {
          message: 'Выберите рейтинг',
          color: 'error'
        })
        isValid = false
      }

      if (!this.form.text.trim()) {
        this.errors.text = 'Напишите текст отзыва'
        isValid = false
      }

      return isValid
    },

    async submitReview() {
      if (!this.validateForm()) {
        return
      }

      this.isSubmitting = true

      try {
        const response = await this.$store.dispatch('reviews/create', {
          userId: this.userId,
          rating: this.form.rating,
          text: this.form.text
        })

        this.reviews.unshift(response)
        this.rating = {
          ...this.rating,
          total: this.rating.total + 1,
          distribution: response.newDistribution
        }

        this.form = {
          rating: 0,
          text: ''
        }

        this.$store.dispatch('snackbar/show', {
          message: 'Отзыв успешно добавлен',
          color: 'success'
        })
      } catch (error) {
        if (error.response?.data?.errors) {
          this.errors = error.response.data.errors
        } else {
          this.$store.dispatch('snackbar/show', {
            message: 'Ошибка при отправке отзыва',
            color: 'error'
          })
        }
      } finally {
        this.isSubmitting = false
      }
    },

    formatDate(date) {
      return new Date(date).toLocaleString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      })
    },

    pluralize(number, words) {
      const cases = [2, 0, 1, 1, 1, 2]
      return words[
        (number % 100 > 4 && number % 100 < 20)
          ? 2
          : cases[(number % 10 < 5) ? number % 10 : 5]
      ]
    }
  },

  created() {
    this.loadRating()
  }
}
</script>

<style scoped>
.user-rating {
  width: 100%;
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

.rating-content {
  padding: 20px;
}

.rating-header {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 32px;
  margin-bottom: 32px;
  padding: 24px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.average-rating {
  text-align: center;
}

.rating-value {
  font-size: 3em;
  font-weight: bold;
  color: #2c3e50;
  display: block;
  margin-bottom: 8px;
}

.total-reviews {
  display: block;
  margin-top: 8px;
  color: #6c757d;
  font-size: 0.9em;
}

.rating-distribution {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rating-bar {
  display: flex;
  align-items: center;
  gap: 8px;
}

.rating-label {
  width: 40px;
  text-align: right;
  color: #2c3e50;
}

.bar-wrapper {
  flex-grow: 1;
  height: 8px;
  background: #f8f9fa;
  border-radius: 4px;
  overflow: hidden;
}

.bar {
  height: 100%;
  background: #f1c40f;
  transition: width 0.3s;
}

.rating-count {
  width: 40px;
  color: #6c757d;
  font-size: 0.9em;
}

.rating-form {
  margin-bottom: 32px;
  padding: 24px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.rating-form h4 {
  margin: 0 0 16px;
  font-size: 1.2em;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 16px;
}

.review-text {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
  font-family: inherit;
  font-size: 1em;
}

.review-text.has-error {
  border-color: #e74c3c;
}

.error-message {
  color: #e74c3c;
  font-size: 0.9em;
  margin-top: 4px;
  display: block;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
}

.submit-btn {
  padding: 10px 20px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;
}

.submit-btn:hover:not(:disabled) {
  background: #2980b9;
}

.submit-btn:disabled {
  background: #95a5a6;
  cursor: not-allowed;
}

.reviews-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.review-item {
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.reviewer-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.reviewer-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.reviewer-name {
  font-weight: 500;
  color: #2c3e50;
}

.review-meta {
  display: flex;
  align-items: center;
  gap: 12px;
}

.review-date {
  color: #6c757d;
  font-size: 0.9em;
}

.review-text {
  color: #2c3e50;
  line-height: 1.5;
}

.load-more {
  text-align: center;
  margin-top: 16px;
}

.load-more-btn {
  padding: 10px 20px;
  background: #f8f9fa;
  color: #2c3e50;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;
}

.load-more-btn:hover:not(:disabled) {
  background: #e9ecef;
}

.load-more-btn:disabled {
  background: #f8f9fa;
  color: #95a5a6;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .rating-header {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .rating-distribution {
    padding-top: 16px;
    border-top: 1px solid #eee;
  }
}
</style> 
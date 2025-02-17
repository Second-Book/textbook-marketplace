<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card>
            <v-card-title>Мой профиль</v-card-title>
            <v-card-text>
              <v-form @submit.prevent="updateProfile">
                <v-text-field
                  v-model="form.username"
                  label="Имя пользователя"
                  readonly
                ></v-text-field>
                <v-text-field
                  v-model="form.email"
                  label="Email"
                  :rules="[v => /.+@.+\..+/.test(v) || 'Email должен быть валидным']"
                ></v-text-field>
                <v-text-field
                  v-model="form.phone"
                  label="Телефон"
                ></v-text-field>
                <v-textarea
                  v-model="form.bio"
                  label="О себе"
                  counter
                  maxlength="500"
                ></v-textarea>
                <v-btn
                  type="submit"
                  color="primary"
                  :loading="updating"
                >
                  Сохранить изменения
                </v-btn>
              </v-form>
            </v-card-text>
          </v-card>
  
          <!-- Мои объявления -->
          <v-card class="mt-4">
            <v-card-title>
              Мои объявления
              <v-spacer></v-spacer>
              <v-btn color="primary" to="/textbooks/add">
                Добавить объявление
              </v-btn>
            </v-card-title>
            <v-card-text>
              <v-data-table
                :headers="headers"
                :items="textbooks"
                :loading="loading"
              >
                <template #[`item.image`]="{ item }">
                  <v-img
                    :src="item.image || '/placeholder.jpg'"
                    max-width="100"
                    max-height="100"
                    contain
                  ></v-img>
                </template>
                <template #[`item.actions`]="{ item }">
                  <v-btn
                    small
                    text
                    color="primary"
                    :to="`/textbooks/${item.id}/edit`"
                  >
                    Редактировать
                  </v-btn>
                  <v-btn
                    small
                    text
                    color="error"
                    @click="deleteTextbook(item.id)"
                  >
                    Удалить
                  </v-btn>
                </template>
              </v-data-table>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        updating: false,
        loading: false,
        form: {
          username: 'testuser',
          email: 'testuser@example.com',
          phone: '+1234567890',
          bio: 'Это пример биографии пользователя.'
        },
        textbooks: [
          {
            id: 1,
            title: 'Математика 2 класс',
            subject: 'Математика',
            grade: '2',
            price: '500.00',
            image: 'http://127.0.0.1:8000/media/__sized__/textbook_images/hemija1razred_jgkxxnhjpg-thumbnail-240x312-90.jpg'
          },
          {
            id: 2,
            title: 'Русский язык 3 класс',
            subject: 'Русский язык',
            grade: '3',
            price: '450.00',
            image: 'http://127.0.0.1:8000/media/__sized__/textbook_images/hemija1razred_jgkxxnhjpg-thumbnail-240x312-90.jpg'
          }
        ],
        headers: [
          { text: 'Фото', value: 'image', sortable: false },
          { text: 'Название', value: 'title' },
          { text: 'Предмет', value: 'subject' },
          { text: 'Класс', value: 'grade' },
          { text: 'Цена', value: 'price' },
          { text: 'Действия', value: 'actions', sortable: false }
        ]
      };
    },
    methods: {
      async updateProfile() {
        try {
          this.updating = true;
          // Mock update profile request
          console.log('Profile updated:', this.form);
          this.$store.dispatch('snackbar/show', {
            text: 'Профиль успешно обновлен',
            color: 'success'
          });
        } catch (error) {
          console.error('Failed to update profile:', error);
          this.$store.dispatch('snackbar/show', {
            text: 'Ошибка при обновлении профиля',
            color: 'error'
          });
        } finally {
          this.updating = false;
        }
      },
      async deleteTextbook(id) {
        if (!confirm('Вы уверены, что хотите удалить это объявление?')) return;
  
        try {
          // Mock delete textbook request
          this.textbooks = this.textbooks.filter(textbook => textbook.id !== id);
          this.$store.dispatch('snackbar/show', {
            text: 'Объявление удалено',
            color: 'success'
          });
        } catch (error) {
          console.error('Failed to delete textbook:', error);
          this.$store.dispatch('snackbar/show', {
            text: 'Ошибка при удалении объявления',
            color: 'error'
          });
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styling here */
  </style>
  
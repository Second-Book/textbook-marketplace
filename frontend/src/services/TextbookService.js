import apiClient from './api';

export default {
  getTextbooks(params) {
    return apiClient.get('/textbooks/', { params });
  },
  getTextbook(id) {
    return apiClient.get(`/textbook/${id}/`);
  },
  createTextbook(textbook) {
    return apiClient.post('/textbooks/', textbook);
  },
  updateTextbook(id, textbook) {
    return apiClient.put(`/textbooks/${id}/`, textbook);
  },
  deleteTextbook(id) {
    return apiClient.delete(`/textbooks/${id}/`);
  },
  login(credentials) {
    return apiClient.post('token/', credentials);
  },
  refreshToken() {
    return apiClient.post('token/refresh/', { refresh: localStorage.getItem('refresh_token') });
  },
  signup(credentials) {
    return apiClient.post('signup/', credentials);
  }
};

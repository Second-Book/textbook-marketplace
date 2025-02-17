import apiClient from './api';

export default {
  getTextbooks(params) {
    return apiClient.get('/textbooks/', { params });
  },
  getTextbook(id) {
    return apiClient.get(`/textbook/${id}/`);
  },
  createTextbook(textbook, config) {
    return apiClient.post('/textbook/create/', textbook, config);
  },
  updateTextbook(id, textbook) {
    return apiClient.put(`/textbooks/${id}/`, textbook);
  },
  deleteTextbook(id) {
    return apiClient.delete(`/textbooks/${id}/`);
  }
};

import apiClient from '../services/api';

export default {
  name: 'authService',
  async login(credentials) {
    try {
      const response = await apiClient.post('token/', credentials);
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
      return response.data;
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  },

  async refreshToken() {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      const response = await apiClient.post('token/refresh/', { refresh: refreshToken });
      localStorage.setItem('access_token', response.data.access);
      return response.data;
    } catch (error) {
      console.error('Token refresh failed:', error);
      throw error;
    }
  },
};

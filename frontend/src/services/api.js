import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust the base URL as needed
  withCredentials: false, // This is the default
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
});

export default apiClient;

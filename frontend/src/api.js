// frontend/src/api.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "/api",
});

// Request interceptor to add the token to headers
apiClient.interceptors.request.use(
  (config) => {
    // Retrieve the token from localStorage
    const token = localStorage.getItem("authToken");
    if (token) {
      // Add the Authorization header
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default apiClient;

import axios from 'axios';

// Create an axios instance
const instance = axios.create({
    baseURL: 'http://localhost:8000/api/',
});

// Add a request interceptor
instance.interceptors.request.use((config) => {
    // Get the auth token from session storage
    const authToken = sessionStorage.getItem('authToken');

    // If the token exists, set the Authorization header
    if (authToken) {
        config.headers.Authorization = `Token ${authToken}`;
    }

    return config;
}, (error) => {
    // Do something with request error
    return Promise.reject(error);
});

export default instance;
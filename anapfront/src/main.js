import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'jquery'
import 'popper.js'
import 'bootstrap'

createApp(App).use(router).use(store).mount('#app')

if (sessionStorage.getItem('authToken')) {
    store.commit('setLoggedIn', true)
}
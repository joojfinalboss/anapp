<template>
    <form @submit.prevent="submitForm">
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>
</template>

<script>
import axios from 'axios';
import { mapMutations } from 'vuex';

export default {
    data() {
        return {
            username: '',
            password: '',
        };
    },
    methods: {
        ...mapMutations(['setLoggedIn']),
        async submitForm() {
            try {
                const response = await axios.post('http://localhost:8000/api/auth/login/', {
                    username: this.username,
                    password: this.password,
                });
                console.log(response.data);

                if (response.data.status === 'success') {
                    // Store the token in session storage
                    sessionStorage.setItem('authToken', response.data.token);

                    this.setLoggedIn(true);
                    this.$router.push('/bode');
                }
            } catch (error) {
                console.error(error);
            }
        },
    },
};
</script>
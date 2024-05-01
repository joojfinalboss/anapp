<template>
    <div>
        <button @click="logout">Logout</button>
    </div>
</template>

<script>
import axios from 'axios';
import { mapMutations } from 'vuex';

export default {
    name: 'UserLogout',
    methods: {
        ...mapMutations(['setLoggedIn']),
        async logout() {
            try {
                await axios.post('http://localhost:8000/api/auth/logout/');
                this.setLoggedIn(false);
                localStorage.removeItem('authToken');
                this.$router.push('/');
            } catch (error) {
                console.error(error);
            }
        },
    },
};
</script>

<style scoped>
</style>
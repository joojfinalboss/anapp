<template>
    <div>
        <input type="text" v-model="username" placeholder="Username">
        <input type="password" v-model="password1" placeholder="Password">
        <input type="password" v-model="password2" placeholder="Confirm Password">
        <button @click="register">Register</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
        }
    },
    methods: {
        async register() {
            console.log('This is the username:', this.username)
            console.log('This is the password1:', this.password1)
            console.log('This is the password2:', this.password2)
            try {
                const response = await axios.post('http://localhost:8000/api/auth/register/', {
                    username: this.username,
                    password1: this.password1,
                    password2: this.password2,
                }, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                console.log(response.data)
            } catch (error) {
                console.error('An error occurred')
            }
        },
    },
}
</script>
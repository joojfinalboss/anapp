<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <router-link to="/" class="navbar-brand">SHIFT</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item" v-if="!loggedIn">
                    <router-link to="/login" class="nav-link">Login</router-link>
                </li>
                <li class="nav-item" v-if="!loggedIn">
                    <router-link to="/register" class="nav-link">Cadastro</router-link>
                </li>
                <li class="nav-item" v-if="loggedIn">
                    <router-link to="/logout" class="nav-link">Logout</router-link>
                </li>
                <li class="nav-item" v-if="loggedIn">
                    <router-link to="/orcamento" class="nav-link">Orçamentos</router-link>
                </li>
                <li class="nav-item" v-if="loggedIn">
                    <router-link to="/pecaavulsapadrao" class="nav-link">Peças Padrão</router-link>
                </li>
                <li class="nav-item" v-if="loggedIn">
                    <router-link to="/material" class="nav-link">Materiais</router-link>
                </li>

            </ul>
        </div>
    </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: {
        ...mapState(['loggedIn'])
    }
}
</script>
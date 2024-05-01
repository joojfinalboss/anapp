import { createRouter, createWebHistory } from 'vue-router'
import UserRegister from './components/UserRegister.vue'
import UserLogin from './components/UserLogin.vue'
import UserLogout from './components/UserLogout.vue'
import CrudPecaAvulsa from './components/pecaavulsa/CrudPecaAvulsa.vue'
import CrudPecaAvulsaPadrao from './components/pecaavulsapadrao/CrudPecaAvulsaPadrao.vue'
import CrudMaterial from './components/material/CrudMaterial.vue'
import CrudOrcamento from './components/orcamento/CrudOrcamento.vue'
import EditMovel from './components/movel/EditMovel.vue'
import EditOrcamento from './components/orcamento/EditOrcamento.vue'
import store from './store'

const routes = [
    { path: '/register', component: UserRegister },
    { path: '/login', component: UserLogin },
    { path: '/logout', component: UserLogout, meta: { requiresAuth: true } },
    { path: '/pecaavulsa/', component: CrudPecaAvulsa, meta: { requiresAuth: true } },
    { path: '/pecaavulsapadrao', component: CrudPecaAvulsaPadrao, meta: { requiresAuth: true } },
    { path: '/movel/edit/:id', component: EditMovel, props: true, meta: { requiresAuth: true } },
    { path: '/material', component: CrudMaterial, meta: { requiresAuth: true }},
    { path: '/orcamento', component: CrudOrcamento, meta: { requiresAuth: true }},
    { path: '/orcamento/edit/:id', component: EditOrcamento, props: true, meta: { requiresAuth: true} },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.state.loggedIn) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            })
        } else {
            next()
        }
    } else {
        next() 
    }
})

export default router
<template>
    <div class="container">
        <table class="table mt-3">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Cliente</th>
                    <th scope="col">Preço Total</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(orcamento, index) in orcamentos" :key="index">
                    <th scope="row">{{ index + 1 }}</th>
                    <td>
                        <input type="text" class="form-control" v-model="orcamento.cliente" :disabled="!orcamento.isNew" required>
                    </td>
                    <td>{{ orcamento.preco_total }}</td>
                    <td>
                        <button v-if="orcamento.isNew" @click="saveOrcamento(orcamento)" class="btn btn-success">Create</button>
                        <router-link v-else :to="`/orcamento/edit/${orcamento.id}`" class="btn btn-primary">Edit</router-link>
                        <button @click="deleteOrcamento(orcamento)" class="btn btn-danger btn-sm" style="margin-left: 10px;">Deletar</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <button @click="addOrcamento" class="btn btn-primary">Adicionar Orcamento</button>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from '@/api'; // Import the axios instance

export default {
    setup() {
        const orcamentos = ref([]);

        onMounted(async () => {
            try {
                const response = await api.get('bode/orcamento/');
                orcamentos.value = response.data.map(orcamento => ({ ...orcamento, isNew: false }));
            } catch (error) {
                console.error(error);
            }
        });

        function addOrcamento() {
            orcamentos.value.push({ cliente: '', preco_total: 0, isNew: true });
        }

        async function createOrcamento(orcamento) {
            try {
                const response = await api.post('bode/orcamento/', orcamento);
                orcamento.id = response.data.id;
                orcamento.isNew = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function updateOrcamento(orcamento) {
            try {
                await api.put(`bode/orcamento/${orcamento.id}/`, orcamento);
            } catch (error) {
                console.error(error);
            }
        }

        async function saveOrcamento(orcamento) {
            if (orcamento.isNew) {
                await createOrcamento(orcamento);
            } else {
                await updateOrcamento(orcamento);
            }
        }

        async function deleteOrcamento(orcamento) {
            try {
                await api.delete(`bode/orcamento/${orcamento.id}/`);
                orcamentos.value = orcamentos.value.filter(o => o !== orcamento);
            } catch (error) {
                console.error(error);
            }
        }

        return { orcamentos, addOrcamento, saveOrcamento, deleteOrcamento };
    },
};
</script>

<style scoped>
</style>
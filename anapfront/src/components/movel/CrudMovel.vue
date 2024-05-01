<template>
    <div class="container">
        <table class="table mt-3">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Preço</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(movel, index) in moveis" :key="index">
                    <th scope="row">{{ index + 1 }}</th>
                    <td>
                        <input type="text" class="form-control" v-model="movel.nome" :disabled="!movel.isNew" required>
                    </td>
                    <td>{{ movel.preco }}</td>
                    <td>
                        <button v-if="movel.isNew" @click="saveMovel(movel)" class="btn btn-success btn-sm">Salvar Móvel</button>
                        <router-link v-else :to="`/movel/edit/${movel.id}`" class="btn btn-primary btn-sm">Editar Móvel</router-link>
                        <button @click="deleteMovel(movel)" class="btn btn-danger btn-sm" style="margin-left: 10px;">Deletar</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <button @click="addMovel" class="btn btn-primary">Adicionar Móvel</button>
    </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import api from '@/api'; // Import the axios instance

export default {
    props: ['orcamentoId'],
    emits: ['update-preco-total'],
    setup(props, { emit }) {
        const moveis = ref([]);

        const fetchData = async () => {
            console.log(props.orcamentoId);
            try {
                const response = await api.get(`bode/movel/?orcamento=${props.orcamentoId}`);
                moveis.value = response.data.map(movel => ({ ...movel, isEditable: false, isNew: false }));
                emit('update-preco-total', calculatePrecoTotal());
            } catch (error) {
                console.error(error);
            }
        };

        onMounted(fetchData);

        watch(() => props.orcamentoId, (newVal) => {
            if (newVal) {
                fetchData();
            }
        });

        function calculatePrecoTotal() {
            return moveis.value.reduce((sum, movel) => sum + movel.preco, 0);
        }

        function addMovel() {
            moveis.value.push({ nome: '', isEditable: true, isNew: true });
        }

        async function createMovel(movel) {
            try {
                const response = await api.post('bode/movel/', { ...movel, orcamento:props.orcamentoId });
                movel.id = response.data.id;
                movel.isNew = false;
                movel.isEditable = false;
                emit('update-preco-total', calculatePrecoTotal());
            } catch (error) {
                console.error(error);
            }
        }

        async function updateMovel(movel) {
            try {
                await api.put(`bode/movel/${movel.id}/`, movel);
                movel.isEditable = false;
                emit('update-preco-total', calculatePrecoTotal());
            } catch (error) {
                console.error(error);
            }
        }

        async function saveMovel(movel) {
            if (movel.isNew) {
                await createMovel(movel);
            } else {
                await updateMovel(movel);
            }
        }

        async function deleteMovel(movel) {
            if (movel.isNew) {
                moveis.value = moveis.value.filter(m => m !== movel);
                emit('update-preco-total', calculatePrecoTotal());
            } else {
                try {
                    await api.delete(`bode/movel/${movel.id}/`);
                    moveis.value = moveis.value.filter(m => m !== movel);
                    emit('update-preco-total', calculatePrecoTotal());
                } catch (error) {
                    console.error(error);
                }
            }
        }

        return { moveis, addMovel, saveMovel, deleteMovel };
    },
};
</script>
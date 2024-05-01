<template>
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">Nome</th>
                    <th scope="col">Altura</th>
                    <th scope="col">Largura</th>
                    <th scope="col">Espessura</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(pecaAvulsaPadrao, index) in pecasAvulsasPadrao" :key="index">
                    <td><input type="text" v-model="pecaAvulsaPadrao.nome" :disabled="!pecaAvulsaPadrao.isEditable" :class="{'bg-not-editable': !pecaAvulsaPadrao.isEditable}" required class="form-control" /></td>
                    <td><input type="number" v-model.number="pecaAvulsaPadrao.altura" :disabled="!pecaAvulsaPadrao.isEditable" :class="{'bg-not-editable': !pecaAvulsaPadrao.isEditable}" required class="form-control" /></td>
                    <td><input type="number" v-model.number="pecaAvulsaPadrao.largura" :disabled="!pecaAvulsaPadrao.isEditable" :class="{'bg-not-editable': !pecaAvulsaPadrao.isEditable}" required class="form-control" /></td>
                    <td><input type="number" v-model.number="pecaAvulsaPadrao.espessura" :disabled="!pecaAvulsaPadrao.isEditable" :class="{'bg-not-editable': !pecaAvulsaPadrao.isEditable}" required class="form-control" /></td>
                    <td>
                        <button v-if="pecaAvulsaPadrao.isNew" @click="createPecaAvulsaPadrao(pecaAvulsaPadrao)" class="btn btn-success">Criar</button>
                        <button v-else-if="!pecaAvulsaPadrao.isEditable" @click="editPecaAvulsaPadrao(pecaAvulsaPadrao)" class="btn btn-primary">Editar</button>
                        <button v-else @click="updatePecaAvulsaPadrao(pecaAvulsaPadrao)" class="btn btn-success btn-sm">Atualizar</button>
                        <button @click="deletePecaAvulsaPadrao(pecaAvulsaPadrao)" class="btn btn-danger btn-sm" style="margin-left: 10px;">Deletar</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <button @click="addPecaAvulsaPadrao" class="btn btn-success mt-3">Adicionar Peça</button>
    </div>
</template>

<script>
import { ref, onMounted, reactive } from 'vue';
import api from '@/api'; // Import the axios instance

export default {
    setup() {
        const pecasAvulsasPadrao = ref([]);

        onMounted(async () => {
            try {
                const response = await api.get('bode/pecaavulsapadrao/');
                pecasAvulsasPadrao.value = response.data.map(pecaAvulsaPadrao => ({ ...pecaAvulsaPadrao, isNew: false, isEditable: false }));
            } catch (error) {
                console.error(error);
            }
        });

        function addPecaAvulsaPadrao() {
            pecasAvulsasPadrao.value.push(reactive({ nome: '', altura: 0, largura: 0, espessura: 0, isNew: true, isEditable: true }));
        }

        function editPecaAvulsaPadrao(pecaAvulsaPadrao) {
            pecaAvulsaPadrao.isEditable = true;
        }

        async function createPecaAvulsaPadrao(pecaAvulsaPadrao) {
            try {
                const response = await api.post('bode/pecaavulsapadrao/', pecaAvulsaPadrao);
                pecaAvulsaPadrao.id = response.data.id;
                pecaAvulsaPadrao.isNew = false;
                pecaAvulsaPadrao.isEditable = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function updatePecaAvulsaPadrao(pecaAvulsaPadrao) {
            try {
                await api.put(`bode/pecaavulsapadrao/${pecaAvulsaPadrao.id}/`, pecaAvulsaPadrao);
                pecaAvulsaPadrao.isEditable = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function deletePecaAvulsaPadrao(pecaAvulsaPadrao) {
            try {
                await api.delete(`bode/pecaavulsapadrao/${pecaAvulsaPadrao.id}/`);
                pecasAvulsasPadrao.value = pecasAvulsasPadrao.value.filter(p => p.id !== pecaAvulsaPadrao.id);
            } catch (error) {
                console.error(error);
            }
        }

        return { pecasAvulsasPadrao, addPecaAvulsaPadrao, createPecaAvulsaPadrao, updatePecaAvulsaPadrao, deletePecaAvulsaPadrao, editPecaAvulsaPadrao };
    },
};
</script>

<style scoped>
.bg-not-editable {
    background-color: #e9ecef;
}
</style>
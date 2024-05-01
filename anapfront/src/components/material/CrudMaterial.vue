<template>
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">Nome</th>
                    <th scope="col">Preço</th>
                    <th scope="col">Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(material, index) in materials" :key="index">
                    <td><input type="text" v-model="material.nome" :disabled="!material.isEditable" :class="{'bg-not-editable': !material.isEditable}" required class="form-control" /></td>
                    <td>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text">R$</span>
                            </div>
                            <input type="number" v-model.number="material.preco" :disabled="!material.isEditable" :class="{'bg-not-editable': !material.isEditable}" required class="form-control" />
                        </div>
                    </td>                    <td>
                        <button v-if="material.isNew" @click="createMaterial(material)" class="btn btn-success">Criar</button>
                        <button v-else-if="!material.isEditable" @click="editMaterial(material)" class="btn btn-primary">Editar</button>
                        <button v-else @click="updateMaterial(material)" class="btn btn-success btn-sm">Atualizar</button>
                        <button @click="deleteMaterial(material)" class="btn btn-danger btn-sm" style="margin-left: 10px;">Deletar</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <button @click="addMaterial" class="btn btn-success mt-3">Adicionar Material</button>
    </div>
</template>

<script>
import { ref, onMounted, reactive } from 'vue';
import api from '@/api'; // Import the axios instance

export default {
    setup() {
        const materials = ref([]);

        onMounted(async () => {
            try {
                const response = await api.get('bode/material/');
                materials.value = response.data.map(material => ({ ...material, isNew: false, isEditable: false }));
            } catch (error) {
                console.error(error);
            }
        });

        function addMaterial() {
            materials.value.push(reactive({ nome: '', preco: 0, isNew: true, isEditable: true }));
        }

        function editMaterial(material) {
            material.isEditable = true;
        }

        async function createMaterial(material) {
            try {
                const response = await api.post('bode/material/', material);
                material.id = response.data.id;
                material.isNew = false;
                material.isEditable = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function updateMaterial(material) {
            try {
                await api.put(`bode/material/${material.id}/`, material);
                material.isEditable = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function deleteMaterial(material) {
            try {
                await api.delete(`bode/material/${material.id}/`);
                materials.value = materials.value.filter(m => m.id !== material.id);
            } catch (error) {
                console.error(error);
            }
        }

        return { materials, addMaterial, createMaterial, updateMaterial, deleteMaterial, editMaterial };
    },
};
</script>
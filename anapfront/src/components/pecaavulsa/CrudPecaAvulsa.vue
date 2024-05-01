<template>
    <div class="container">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Altura</th>
                    <th>Largura</th>
                    <th>Espessura</th>
                    <th>Material</th>
                    <th>Preço</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(pecaAvulsa, index) in pecasAvulsas" :key="index">
                    <td class="col-2">
                        <input type="text" v-model="pecaAvulsa.nome" :disabled="!pecaAvulsa.isEditable" :class="{'bg-not-editable': !pecaAvulsa.isEditable}" required class="form-control" />
                    </td>
                    <td class="custom-col">
                        <div class="input-group">
                            <input type="number" v-model.number="pecaAvulsa.altura" :disabled="!pecaAvulsa.isEditable" :class="{'bg-not-editable': !pecaAvulsa.isEditable}" required class="form-control" @keydown="preventDotAndComma($event)" />
                            <div class="input-group-append">
                                <span class="input-group-text">cm</span>
                            </div>
                        </div>
                    </td>
                    <td class="custom-col">
                        <div class="input-group">
                            <input type="number" v-model.number="pecaAvulsa.largura" :disabled="!pecaAvulsa.isEditable" :class="{'bg-not-editable': !pecaAvulsa.isEditable}" required class="form-control" @keydown="preventDotAndComma($event)" />
                            <div class="input-group-append">
                                <span class="input-group-text">cm</span>
                            </div>
                        </div>
                    </td>
                    <td class="custom-col">
                        <div class="input-group">
                            <input type="number" v-model.number="pecaAvulsa.espessura" :disabled="!pecaAvulsa.isEditable" :class="{'bg-not-editable': !pecaAvulsa.isEditable}" required class="form-control" @keydown="preventDotAndComma($event)" />
                            <div class="input-group-append">
                                <span class="input-group-text">cm</span>
                            </div>
                        </div>
                    </td>
                    <td class="col-2">
                        <select v-model="pecaAvulsa.material" class="form-control">
                            <option v-for="material in materials" :value="material.id" :key="material.id">{{ material.nome }}</option>
                        </select>
                    </td>
                    <td class="col-1">{{ formatCurrency(pecaAvulsa.preco) }}</td>
                    <td class="col-2">
                        <button v-if="!pecaAvulsa.isEditable" @click="editPecaAvulsa(pecaAvulsa)" class="btn btn-primary btn-sm" style="margin-right: 10px;">Editar</button>
                        <button v-else @click="updatePecaAvulsa(pecaAvulsa)" class="btn btn-success btn-sm">Atualizar</button>
                        <button @click="deletePecaAvulsa(pecaAvulsa)" class="btn btn-danger btn-sm" style="margin-left: 10px;">Deletar</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="modal" :class="{ 'show d-block': showModal }" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="myModalLabel">Seleciona uma peça</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <select v-model="selectedPecaAvulsaPadrao" style="font-size: 18px; height: 40px; width: 100%;">
                            <option v-for="padrao in pecaAvulsaPadraos" :value="padrao" :key="padrao.id" style="font-size: 18px;">{{ padrao.nome }}</option>
                        </select>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" @click="addPecaAvulsa">Confirm</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal" @click="showModal = false">Cancel</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="d-flex justify-content-center">
            <button type="button" class="btn btn-success btn-sm" @click="showModal = true">Adicionar Peça</button>
        </div>

    </div>
</template>

<script>
import { ref, onMounted, watch, computed } from 'vue';
import { formatCurrency, preventDotAndComma } from '../../utils';
import api from '@/api';

export default {
    props: ['movelId'],
    emits: ['updateValorTotal', 'save'],
    methods: {
        formatCurrency,
        preventDotAndComma,
    },

    setup(props, { emit }) {
        const showModal = ref(false);
        const selectedPecaAvulsaPadrao = ref(null);
        const pecaAvulsaPadraos = ref([]);
        const pecasAvulsas = ref([]);
        const materials = ref([]); 
        const selectedMaterial = ref(null);

        const fetchData = async () => {
            try {
                const responsePecasAvulsas = await api.get('bode/pecaavulsa/');
                pecasAvulsas.value = responsePecasAvulsas.data
                    .filter(pecaAvulsa => pecaAvulsa.movel === props.movelId)
                    .map(pecaAvulsa => ({ 
                        ...pecaAvulsa, 
                        altura: Number(pecaAvulsa.altura),
                        largura: Number(pecaAvulsa.largura),
                        material: pecaAvulsa.material,
                        isEditable: false, 
                        isNew: false,
                    }));

                const responseMaterials = await api.get('bode/material/');
                materials.value = responseMaterials.data;

                // Calculate resultado for each PecaAvulsa
                pecasAvulsas.value.forEach(pecaAvulsa => {
                    calculateResultado(pecaAvulsa);
                });

                const responsePecaAvulsaPadraos = await api.get('bode/pecaavulsapadrao/');
                pecaAvulsaPadraos.value = responsePecaAvulsaPadraos.data;
            } catch (error) {
                console.error(error);
            }
        };

        onMounted(fetchData);

        watch(() => props.movelId, fetchData);

        function addPecaAvulsa() {
            if (selectedPecaAvulsaPadrao.value) {
                pecasAvulsas.value.push({ 
                    movel: props.movelId, 
                    nome: selectedPecaAvulsaPadrao.value.nome, 
                    altura: selectedPecaAvulsaPadrao.value.altura, 
                    largura: selectedPecaAvulsaPadrao.value.largura, 
                    espessura: selectedPecaAvulsaPadrao.value.espessura, 
                    isEditable: true, 
                    isNew: true 
                });
                showModal.value = false;
            }
        }

        function editPecaAvulsa(pecaAvulsa) {
            pecaAvulsa.isEditable = true;
        }

        async function createPecaAvulsa(pecaAvulsa) {
            try {
                console.log('pecaAvulsa:', pecaAvulsa);
                const response = await api.post('bode/pecaavulsa/', { ...pecaAvulsa, movel: props.movelId });
                console.log('response:', response); // Log response
                pecaAvulsa.id = response.data.id;
                pecaAvulsa.isNew = false;
                pecaAvulsa.isEditable = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function updatePecaAvulsa(pecaAvulsa) {
            try {
                await api.put(`bode/pecaavulsa/${pecaAvulsa.id}/`, pecaAvulsa);
                pecaAvulsa.isEditable = false;
            } catch (error) {
                console.error(error);
            }
        }

        async function deletePecaAvulsa(pecaAvulsa) {
            try {
                if (!pecaAvulsa.isNew) {
                    await api.delete(`bode/pecaavulsa/${pecaAvulsa.id}/`);
                }
                pecasAvulsas.value = pecasAvulsas.value.filter(p => p !== pecaAvulsa);
            } catch (error) {
                console.error(error);
            }
        }

        function calculateResultado(pecaAvulsa) {
            if (typeof pecaAvulsa.material !== 'undefined') {
                const material = materials.value.find(m => {
                    return Number(m.id) === Number(pecaAvulsa.material);
                });

                if (material) {
                    console.log('preco: ', material.preco)

                    if (typeof pecaAvulsa.altura === 'number' && typeof pecaAvulsa.largura === 'number') {
                        pecaAvulsa.preco = ((pecaAvulsa.altura * pecaAvulsa.largura) * material.preco) / 10000;
                    }
                    else {
                        pecaAvulsa.preco = 0;
                    }
                }
                else {
                    console.log('No material found with id: ', pecaAvulsa.material);
                    pecaAvulsa.preco = 0;
                }
            }
            else {
                pecaAvulsa.preco = 0;
            }
        }

        const valorTotal = computed(() => {
            return pecasAvulsas.value.reduce((total, pecaAvulsa) => total + (pecaAvulsa.preco || 0), 0);
        });

        watch(valorTotal, (newVal) => {
            emit('updateValorTotal', newVal);
        });

        watch(() => pecasAvulsas.value.map(pecaAvulsa => [pecaAvulsa.altura, pecaAvulsa.largura, pecaAvulsa.valor_metro_quadrado]), () => {
            pecasAvulsas.value.forEach(pecaAvulsa => {
                calculateResultado(pecaAvulsa);
            });
        }, { deep: true });

        watch(() => pecasAvulsas.value.map(pecaAvulsa => [pecaAvulsa.altura, pecaAvulsa.largura, pecaAvulsa.material]), () => {
            pecasAvulsas.value.forEach(pecaAvulsa => {
                calculateResultado(pecaAvulsa);
            });
        }, { deep: true });

        watch(() => emit('save'), () => {
            pecasAvulsas.value.forEach(pecaAvulsa => {
                if (pecaAvulsa.isNew) {
                    this.createPecaAvulsa(pecaAvulsa);
                } else if (pecaAvulsa.isEditable) {
                    this.updatePecaAvulsa(pecaAvulsa);
                }
            });
        });
            
        return { 
            pecasAvulsas, 
            addPecaAvulsa, 
            createPecaAvulsa, 
            updatePecaAvulsa, 
            deletePecaAvulsa, 
            editPecaAvulsa, 
            calculateResultado, 
            showModal,
            selectedPecaAvulsaPadrao,
            pecaAvulsaPadraos,
            selectedMaterial,
            materials,
        };    
    }, 
};
</script>

<style scoped>
.bg-not-editable {
    background-color: #e9ecef;
}
.custom-col {
    flex: 0 0 12.5%; /* 1.5 out of 12 columns */
    max-width: 12.5%; /* 1.5 out of 12 columns */
}
</style>
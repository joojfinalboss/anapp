<template>
    <div class="container">
        <h1>Editar Móvel</h1>

        <div class="row">
            <div class="col-md-1">
                <label for="id">ID</label>
                <input id="id" type="text" class="form-control" v-model="movel.id" disabled>
            </div>
            <div class="col-md-3">
                <label for="nome">Nome do Móvel</label>
                <input id="nome" type="text" class="form-control" v-model="movel.nome">
            </div>
            <div class="col-md-3">
                <label for="valorTotal">Valor Total</label>
                <input id="valorTotal" type="text" class="form-control" :value="formatCurrency(valorTotal)" readonly>
            </div>
        </div>

        <h2 class="mt-3">Peças</h2>

        <!-- PecaAvulsa component is always visible -->
        <PecaAvulsa :movelId="movel.id" @updateValorTotal="valorTotal = $event" />

        <div v-for="(pecaAvulsa, index) in pecaAvulsas" :key="index">
            <PecaAvulsa :pecaAvulsa="pecaAvulsa" :movelId="movel.id" @updateValorTotal="valorTotal += $event" />
        </div>

        <button type="button" class="btn btn-success mt-3" @click="$emit('save')">Save</button>
        <div v-if="showAlert" class="alert alert-success" role="alert">
            {{ alertMessage }}
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import api from '@/api'; 
import PecaAvulsa from '@/components/pecaavulsa/CrudPecaAvulsa.vue';
import { formatCurrency } from '../../utils';

export default {
    components: { PecaAvulsa },
    props: ['id'],
    methods: {
        formatCurrency,
    },
    setup(props) {
        const movel = ref({});
        const pecaAvulsas = ref([]);
        const valorTotal = ref(0); // Add this line
        const showAlert = ref(false);
        const alertMessage = ref('');

        onMounted(async () => {
            try {
                const response = await api.get(`bode/movel/${props.id}/`);
                movel.value = response.data;
            } catch (error) {
                console.error(error);
            }
        });

        async function save() {
            try {
                movel.value.preco = valorTotal.value;
                await api.put(`bode/movel/${movel.value.id}/`, movel.value);
                alertMessage.value = 'Móvel salvo com sucesso!';
                showAlert.value = true;
                setTimeout(() => { showAlert.value = false; }, 3000);
            } catch (error) {
                console.error(error);
                alertMessage.value = 'Móvel não salvo!';
                showAlert.value = true;
                setTimeout(() => { showAlert.value = false; }, 3000);
            }
        }

        return { movel, pecaAvulsas, save, valorTotal, showAlert, alertMessage};
    },
};
</script>

<style scoped>
  /* Your styles here */
</style>
<template>
    <div class="container">
        <h1>Editar Orcamento</h1>

        <div class="row">
            <div class="col-md-1">
                <label for="id">ID</label>
                <input id="id" type="text" class="form-control" v-model="orcamento.id" disabled>
            </div>
            <div class="col-md-3">
                <label for="cliente">Cliente</label>
                <input id="cliente" type="text" class="form-control" v-model="orcamento.cliente">
            </div>
            <div class="col-md-3">
                <label for="precoTotal">Preço Total</label>
                <input id="precoTotal" type="text" class="form-control" :value="formatCurrency(precoTotal)" readonly>
            </div>
        </div>

        <h2 class="mt-3">Moveis</h2>

        <!-- CrudMovel component is always visible -->
        <CrudMovel :orcamentoId="orcamento.id" @updatePrecoTotal="updatePrecoTotal" />

    </div>
</template>

<script>
import { ref, onMounted, watch, watchEffect } from 'vue';
import api from '@/api'; 
import CrudMovel from '@/components/movel/CrudMovel.vue';
import { formatCurrency } from '../../utils';

export default {
    components: { CrudMovel },
    props: ['id'],
    methods: {
        formatCurrency,
    },
    setup(props) {
        const orcamento = ref({});
        const moveis = ref([]);
        const precoTotal = ref(0);

        const updatePrecoTotal = () => {
            if (Array.isArray(moveis.value)) {
                precoTotal.value = moveis.value.reduce((sum, movel) => sum + parseFloat(movel.preco), 0);
                precoTotal.value = parseFloat(precoTotal.value.toFixed(2));
            }
        };

        const fetchData = async () => {
            if (props.id) {
                try {
                    const response = await api.get(`bode/orcamento/${props.id}/`);
                    orcamento.value = response.data;
                    const moveisResponse = await api.get(`bode/movel/?orcamento=${props.id}`);
                    moveis.value = moveisResponse.data;
                    console.log('Moveis:', moveis.value); // Add this line
                    updatePrecoTotal();
                } catch (error) {
                    console.error(error);
                }
            }
        };

        watch(() => props.id, fetchData);

        onMounted(fetchData);

        const updateOrcamento = async () => {
            try {
                await api.put(`bode/orcamento/${orcamento.value.id}/`, orcamento.value);
            } catch (error) {
                console.error(error);
            }
        };

        // Watch for changes in moveis
        watchEffect(() => {
            if (Array.isArray(moveis.value)) {
                // Calculate the sum of the preco attribute of all movel models
                const total = moveis.value.reduce((sum, movel) => sum + parseFloat(movel.preco), 0);
                // Update orcamento.preco_total
                orcamento.value.preco_total = parseFloat(total.toFixed(2));
                // Update orcamento on the server
                updateOrcamento();
            }
        });


        return { orcamento, moveis, precoTotal, updatePrecoTotal };
    },  
};
</script>
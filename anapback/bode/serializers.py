from rest_framework import serializers
from .models import PecaAvulsa, Movel, Orcamento, PecaAvulsaPadrao, Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class PecaAvulsaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PecaAvulsa
        fields = '__all__'

class MovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movel
        fields = '__all__'

class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orcamento
        fields = '__all__'

class PecaAvulsaPadraoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PecaAvulsaPadrao
        fields = ['id', 'nome', 'altura', 'largura', 'espessura', ]   
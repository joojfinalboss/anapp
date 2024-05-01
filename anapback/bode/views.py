from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PecaAvulsa, Movel, Orcamento, PecaAvulsaPadrao, Material
from .serializers import PecaAvulsaSerializer, MovelSerializer, OrcamentoSerializer, PecaAvulsaPadraoSerializer
from .serializers import MaterialSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PecaAvulsaListCreate(generics.ListCreateAPIView):
    queryset = PecaAvulsa.objects.all()
    serializer_class = PecaAvulsaSerializer
    permission_classes = [IsAuthenticated]

class PecaAvulsaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PecaAvulsa.objects.all()
    serializer_class = PecaAvulsaSerializer
    permission_classes = [IsAuthenticated]


class MovelListCreate(generics.ListCreateAPIView):
    queryset = Movel.objects.all()
    serializer_class = MovelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['orcamento']
    
class MovelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movel.objects.all()
    serializer_class = MovelSerializer
    permission_classes = [IsAuthenticated]

class OrcamentoListCreate(generics.ListCreateAPIView):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer
    permission_classes = [IsAuthenticated]

class OrcamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer
    permission_classes = [IsAuthenticated]

class PecaAvulsaPadraoListCreate(generics.ListCreateAPIView):
    queryset = PecaAvulsaPadrao.objects.all()
    serializer_class = PecaAvulsaPadraoSerializer
    permission_classes = [IsAuthenticated]

class PecaAvulsaPadraoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PecaAvulsaPadrao.objects.all()
    serializer_class = PecaAvulsaPadraoSerializer
    permission_classes = [IsAuthenticated]

class MaterialListCreate(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

class MaterialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]
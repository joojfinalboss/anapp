from django.urls import path
from .views import PecaAvulsaListCreate, PecaAvulsaRetrieveUpdateDestroy, MovelListCreate, MovelRetrieveUpdateDestroy, OrcamentoListCreate, OrcamentoRetrieveUpdateDestroy, PecaAvulsaPadraoListCreate, PecaAvulsaPadraoRetrieveUpdateDestroy
from .views import MaterialListCreate, MaterialRetrieveUpdateDestroy

urlpatterns = [
    path('pecaavulsa/', PecaAvulsaListCreate.as_view(), name='pecaavulsa-list-create'),
    path('pecaavulsa/<int:pk>/', PecaAvulsaRetrieveUpdateDestroy.as_view(), name='pecaavulsa-retrieve-update-destroy'),
    path('movel/', MovelListCreate.as_view(), name='movel-list-create'),
    path('movel/<int:pk>/', MovelRetrieveUpdateDestroy.as_view(), name='movel-retrieve-update-destroy'),
    path('orcamento/', OrcamentoListCreate.as_view(), name='orcamento-list-create'),
    path('orcamento/<int:pk>/', OrcamentoRetrieveUpdateDestroy.as_view(), name='orcamento-retrieve-update-destroy'),
    path('pecaavulsapadrao/', PecaAvulsaPadraoListCreate.as_view(), name='pecaavulsapadrao-list-create'),
    path('pecaavulsapadrao/<int:pk>/', PecaAvulsaPadraoRetrieveUpdateDestroy.as_view(), name='pecaavulsapadrao-retrieve-update-destroy'),
    path('material/', MaterialListCreate.as_view(), name='material-list-create'),
    path('material/<int:pk>/', MaterialRetrieveUpdateDestroy.as_view(), name='material-retrieve-update-destroy'),
]
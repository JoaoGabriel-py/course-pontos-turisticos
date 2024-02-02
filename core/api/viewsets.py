from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    serializer_class = PontoTuristicoSerializer
    search_fields = ['nome', 'descricao', 'endereco__linha1']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
    
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
    
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass



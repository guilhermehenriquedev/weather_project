from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from weather_api.repository.main import Repository
from weather_api.models import PrevisaoTempoHistorico
from weather_api.serializer import PrevisaoTempoMS


class PrevisaoTempoHistoryViewSet(viewsets.ModelViewSet):
    """ Retorna dados de busca anteriores """
    
    queryset = PrevisaoTempoHistorico.objects.all()
    serializer_class = PrevisaoTempoMS
    filter_backends = (SearchFilter, OrderingFilter)

    search_fields = [
        'cidade',
    ]

    def __init__(self, *args, **kwargs):
        ''' Cria tabela de histórico, caso nao exista '''
        repo = Repository()
        repo.create_table_if_not_exist()
    
    def get_serializer_class(self):
        actions = [
            'create',
            'update',
            'partial_update'
        ]

        if self.action in actions:
            return PrevisaoTempoMS
        return self.serializer_class

    def put(self, request, id=None):

        _data = PrevisaoTempoHistorico.objects.filter(id=id)
        serializer = PrevisaoTempoMS(_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
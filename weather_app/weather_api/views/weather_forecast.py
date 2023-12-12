import requests

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from weather_api.repository.main import Repository
from configs.settings import OPENWEATHERMAP_API_KEY
from weather_api.models import PrevisaoTempoHistorico

class WeatherForecastViewSet(viewsets.ViewSet):

    def __init__(self, *args, **kwargs):
        ''' Cria tabela de histórico, caso nao exista '''
        repo = Repository()
        repo.create_table_if_not_exist()

    @action(detail=False, methods=['get'], url_path='get')
    def get_weather_data(self, request):
        """ Retorna dados de previsa de 5 dias """

        city = request.GET.get('city')  # Padrão: Londres
        api_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHERMAP_API_KEY}'

        try:

            response = requests.get(api_url)
            data = response.json()
            history = PrevisaoTempoHistorico(
                cidade=city,
                data=data
            )
            history.save()
            return Response(data, status=status.HTTP_200_OK)
        
        except Exception as err:
            print(err)
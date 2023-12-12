import requests
import logging

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from weather_api.repository.main import Repository
from configs.settings import OPENWEATHERMAP_API_KEY
from weather_api.models import PrevisaoTempoHistorico

#Bloco de configuração dos logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('logs/application.log')
fh.setFormatter(formatter)
logger.addHandler(fh)


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
            if data.get("cod") != "404":
                logger.info(f"Buscando dados para cidade {city}, na API weather_forecast")
                history = PrevisaoTempoHistorico(
                    cidade=city,
                    data=data
                )
                history.save()
                logger.info(f"Histórico de busca para a cidade {city}, salvo")
                return Response(data, status=status.HTTP_200_OK)
            else:
                logger.error(f"Cidade {city}, não encontrada")
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            logger.error(f"Erro de busca para a cidade {city}, {err}")
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
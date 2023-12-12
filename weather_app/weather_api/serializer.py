from weather_api.models import *
from rest_framework import serializers

class PrevisaoTempoMS(serializers.ModelSerializer):
    ''' Serializador da tabela previsao_tempo '''

    class Meta:
        model = PrevisaoTempoHistorico
        fields = '__all__'
# previsao_tempo_app/models.py

from django.db import models

class PrevisaoTempoHistorico(models.Model):
    id = models.AutoField(primary_key=True)
    cidade = models.CharField(max_length=100)
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'previsao_tempo'

import sqlite3
from django.db import connections
from weather_api.helpers.utils import dictfetchall


class Repository():
    ''' Funções sql para reutilização no projeto '''
    
    def __init__(self):
        pass

    def create_table_if_not_exist(self):
        ''' Cria a tabela de histórico, caso nao exista '''
        
        connection_obj = sqlite3.connect('db.sqlite3')
        cursor_obj = connection_obj.cursor()

        sql = """
            CREATE TABLE IF NOT EXISTS previsao_tempo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade TEXT NOT NULL,
                data JSON NOT NULL
            );
            """

        cursor_obj.execute(sql)
        connection_obj.commit()
        cursor_obj.fetchall()
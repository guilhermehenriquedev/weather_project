import csv
import io
import logging

def dictfetchall(cursor):
    ''' Retorna registros do cursor como uma lista de dicionarios '''

    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
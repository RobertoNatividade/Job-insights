from functools import lru_cache
import csv

@lru_cache

def read(path):
    with open(path) as file_lista:
        leitor = csv.DictReader(file_lista)  
        lista = [
            item for item in leitor
        ]
    return lista
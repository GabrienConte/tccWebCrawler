from typing import List
from src.database.db_handler import DbHandler

db = DbHandler()

# REGIAO URL VISITADAS
def carrega_urls_visitadas() -> List[str]:
    urls_dict = db.get_urls_visitadas()
    urls_formatada = list[str]()

    for url_dict in urls_dict:
        urls_formatada.append(url_dict["link"])

    return urls_formatada

def salva_urls_visitadas(lista_urls_visitadas: List[str]):
    lista_urls_visitadas_formatada = [{"link": url} for url in lista_urls_visitadas]
    db.set_urls_visitadas(lista_urls_visitadas_formatada)
# FIM REGIAO


# REGIAO URL NAO VISITADAS
def carrega_urls_nao_visitadas() -> List[str]:
    urls_dict = db.get_urls_nao_visitadas()
    urls_formatada = list[str]()

    for url_dict in urls_dict:
        urls_formatada.append(url_dict["link"])

    return urls_formatada

def salva_urls_nao_visitadas(lista_urls_visitadas: List[str]):
    lista_urls_nao_visitadas_formatada = [{"link": url} for url in lista_urls_visitadas]
    db.set_urls_nao_visitadas(lista_urls_nao_visitadas_formatada)
# FIM REGIAO
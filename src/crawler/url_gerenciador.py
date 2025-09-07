from typing import List
from src.database.db_handler import DbHandler
from src.models import UrlInfo

db = DbHandler()

# VISITADAS
def carrega_urls_visitadas() -> List[UrlInfo]:
    urls_dict = db.get_urls_visitadas()
    return [UrlInfo.from_dict(d) for d in urls_dict]

def salva_urls_visitadas(lista_urls_visitadas: List[UrlInfo]):
    db.set_urls_visitadas([u.to_dict() for u in lista_urls_visitadas])

# NÃO VISITADAS
def carrega_urls_nao_visitadas() -> List[UrlInfo]:
    urls_dict = db.get_urls_nao_visitadas()
    return [UrlInfo(link=d["link"]) for d in urls_dict]

def salva_urls_nao_visitadas(lista_urls_nao_visitadas: List[UrlInfo]):
    db.set_urls_nao_visitadas([{"link": u.link} for u in lista_urls_nao_visitadas])

# COM ERRO
def carrega_urls_com_erro() -> List[UrlInfo]:
    urls_dict = db.get_urls_com_erro()
    return [UrlInfo.from_dict(d) for d in urls_dict]

def salva_urls_com_erro(lista_com_erro: List[UrlInfo]):
    db.set_urls_com_erro([u.to_dict() for u in lista_com_erro])
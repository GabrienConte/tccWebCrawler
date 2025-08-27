from typing import List
from src.database.db_handler import DbHandler

db = DbHandler()

def carrega_urls_visitadas() -> List[str]:
    urls_dict = db.get_urls_visitadas()
    urls_formatada = list[str]()

    for url_dict in urls_dict:
        urls_formatada.append(url_dict["link"])

    return urls_formatada
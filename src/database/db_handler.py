import json
from config import configuracoes

class DbHandler:

    def __init__(self):
        self.path_urls_visitadas = configuracoes.ARQUIVO_URLS_VISITADAS

    def get_urls_visitadas(self) -> dict:
        with open(self.path_urls_visitadas, mode="r", encoding="utf-8") as read_file:
            urls_visitadas_json = json.load(read_file)

            return urls_visitadas_json
        
    def set_urls_visitadas(self, urls_visitadas: dict):
        with open(self.path_urls_visitadas, mode="w", encoding="utf-8") as write_file:
            json.dump(urls_visitadas, write_file)

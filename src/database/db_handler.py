import json
from typing import List
from config import configuracoes

class DbHandler:

    def __init__(self):
        self.path_urls_visitadas = configuracoes.ARQUIVO_URLS_VISITADAS
        self.path_urls_nao_visitadas = configuracoes.ARQUIVO_URLS_NAO_VISITADAS
        self.path_urls_com_erro = configuracoes.ARQUIVO_URLS_COM_ERRO

    # REGIAO URL VISITADAS
    def get_urls_visitadas(self) -> dict:
        if not self.path_urls_visitadas.exists():
            return []
        
        with open(self.path_urls_visitadas, mode="r", encoding="utf-8") as read_file:
            urls_visitadas_json = json.load(read_file)
            return urls_visitadas_json
        
    def set_urls_visitadas(self, urls_visitadas: List[dict]):
        with open(self.path_urls_visitadas, mode="w", encoding="utf-8") as write_file:
            json.dump(urls_visitadas, write_file)
    # FIM REGIAO


    # REGIAO URL NAO VISITADAS
    def get_urls_nao_visitadas(self) -> dict:
        if not self.path_urls_nao_visitadas.exists():
            return []
        
        with open(self.path_urls_nao_visitadas, mode="r", encoding="utf-8") as read_file:
            urls_visitadas_json = json.load(read_file)
            return urls_visitadas_json
        
    def set_urls_nao_visitadas(self, urls_visitadas: List[dict]):
        with open(self.path_urls_nao_visitadas, mode="w", encoding="utf-8") as write_file:
            json.dump(urls_visitadas, write_file)
    # FIM REGIAO

    # REGIAO URL COM ERRO
    def get_urls_com_erro(self) -> dict:
        if not self.path_urls_com_erro.exists():
            return []
        
        with open(self.path_urls_com_erro, mode="r", encoding="utf-8") as read_file:
            urls_com_erro_json = json.load(read_file)
            return urls_com_erro_json
        
    def set_urls_com_erro(self, urls_com_erro: List[dict]):
        with open(self.path_urls_com_erro, mode="w", encoding="utf-8") as write_file:
            json.dump(urls_com_erro, write_file)
    # FIM REGIAO


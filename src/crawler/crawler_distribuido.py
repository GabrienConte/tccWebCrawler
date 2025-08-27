from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
from typing import List, Dict

class CrawlerUFSM:
    def __init__(self):
        self.headers = {
            'User-Agent': 'GabrielConteTCC-UFSM-Crawler/1.0 (gabriel.conte@acad.ufsm.br)',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'pt-BR,pt;q=0.9'
        }

    def fazer_requisicao(self, url: str) -> str:
        try:
            req = Request(url, headers=self.headers)
            with urlopen(req) as response:
                return response.read().decode('utf-8')
        except URLError as e:
            print(f"Falha ao acessar {url}: {e}")
            raise
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise
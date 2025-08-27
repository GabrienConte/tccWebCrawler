from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import time
from typing import List, Dict
import src.crawler.url_gerenciador as url_gerenciador
from config import configuracoes

class CrawlerUFSM:
    def __init__(self):
        self.headers = {
            'User-Agent': 'GabrielConteTCC-UFSM-Crawler/1.0 (gabriel.conte@acad.ufsm.br)',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'pt-BR,pt;q=0.9'
        }
        self.urls_visitadas = url_gerenciador.carrega_urls_visitadas()
        self.urls_para_visitar = [configuracoes.URL_BASE_UFSM_PORTAL]

    def _fazer_requisicao(self, url: str) -> str:
        try:
            print(f"[LOG] Iniciando requisição para: {url}")
            req = Request(url, headers=self.headers)
            with urlopen(req) as response:
                status_code = response.getcode()
                print(f"[LOG] Resposta recebida de {url} - Status: {status_code}")
                return response.read().decode('utf-8')
        except URLError as e:
            print(f"Falha ao acessar {url}: {e}")
            raise
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise

    def _get_links_from_url(self, url: str) -> List[str]:
        try:
            html = self._fazer_requisicao(url)
            print(f"[LOG] HTML recebido ({len(html)} bytes)")
            soup = BeautifulSoup(html, "html.parser")
            body_find = soup.find('body')

            regex_href = re.compile(r'(https?\:\/\/(www\.)?(portal.)?ufsm[^\'\"]+)|(^\/[^\'\"]+)$', re.IGNORECASE)

            anchors = body_find.find_all('a', {'href': regex_href})
            print(f"[LOG] Total de links encontrados: {len(anchors)}")

            links = set()
            for a in anchors:
                href = a.get('href')
                if href:
                    if href.startswith('/'):
                        href = urljoin(configuracoes.URL_BASE_UFSM_PORTAL, href)
                    links.add(href)

            print(f"[LOG] Total de links únicos extraídos: {len(links)}")
            return list(links)
        except Exception as e:
            print(f"Falha na extração: {e}")
            return []
        
    def craw_paginas_ufsm(self):
        try:
            count_urls = 0
            while count_urls < configuracoes.MAX_REQUISICAO and self.urls_para_visitar:
                url = self.urls_para_visitar[0]
                try:
                    print(f"URL A SER RECOLHIDA OS LINK {url}")
                    links_paginas = self._get_links_from_url(url)

                    for link in links_paginas:
                        if link not in self.urls_para_visitar and link not in self.urls_visitadas:
                            self.urls_para_visitar.append(link)

                    removida = self.urls_para_visitar.pop(0)
                    print(f"[LOG] URL removida da lista: {removida}")
                except Exception as e:
                    print(f"Falha ao extrair a url: {url} Erro: {e}")
                    break
                finally:
                    count_urls += 1
                    time.sleep(5)
                        
        except Exception as e:
            print(f"Falha na extração: {e}")
        
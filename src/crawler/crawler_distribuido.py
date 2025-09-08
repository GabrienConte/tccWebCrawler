from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import time
from typing import List, Dict
from src.models import UrlInfo
import src.crawler.url_gerenciador as url_gerenciador
from config import configuracoes
from config.logger_config import logger

class CrawlerUFSM:
    def __init__(self):
        self.headers = {
            'User-Agent': 'GabrielConteTCC-UFSM-Crawler/1.0 (gabriel.conte@acad.ufsm.br)',
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'pt-BR,pt;q=0.9'
        }
        self.urls_visitadas = url_gerenciador.carrega_urls_visitadas()
        self.urls_para_visitar = url_gerenciador.carrega_urls_nao_visitadas()
        self.urls_com_erro = url_gerenciador.carrega_urls_com_erro()

    def _fazer_requisicao(self, url_info: UrlInfo) -> str:
        try:
            req = Request(url_info.link, headers=self.headers)
            with urlopen(req) as response:
                url_info.status = response.getcode()
                if url_info.status != 200:
                    return ""
                
                content_type = response.headers.get_content_charset()
                encoding = content_type if content_type else "utf-8"

                try:
                    return response.read().decode(encoding, errors="replace")
                except UnicodeDecodeError:
                    # fallback para latin-1 se falhar
                    return response.read().decode("latin-1", errors="replace")
                
        except URLError as e:
            logger.error(f"[_fazer_requisicao] Falha ao acessar {url_info.link}: {e}")
            url_info.status = url_info.status if url_info.status else 0
            return ""
        except Exception as e:
            logger.error(f"[_fazer_requisicao] Erro inesperado: {e}")
            url_info.status = url_info.status if url_info.status else 0
            return ""

    def _get_links_from_url(self, url_info: UrlInfo) -> List[UrlInfo]:
        try:
            html = self._fazer_requisicao(url_info)

            if url_info.status != 200:
                logger.warning(f"[_get_links_from_url] URL com erro: {url_info.link} ({url_info.status})")
                return []
            
            logger.info(f"[LOG] HTML recebido ({len(html)} bytes)")
            soup = BeautifulSoup(html, "html.parser")
            body_find = soup.find('body')

            regex_href = re.compile(r'^(https?\:\/\/(www\.)?(portal.)?ufsm[^\'\"]+)|(^\/[^\'\"]+)$', re.IGNORECASE)

            anchors = body_find.find_all('a', {'href': regex_href})
            logger.info(f"[_get_links_from_url] Total de links encontrados: {len(anchors)}")

            links = set()
            for a in anchors:
                href = a.get('href')
                if href:
                    if href.startswith('/'):
                        href = urljoin(configuracoes.URL_BASE_UFSM_PORTAL, href)

                    if any(dis in href for dis in configuracoes.DISALLOW_PATHS):
                        logger.info(f"[_get_links_from_url] Ignorando link proibido: {href}")
                        continue

                    if any(href.lower().endswith(ext) for ext in configuracoes.DISALLOW_EXTENSIONS):
                        logger.info(f"[_get_links_from_url] Ignorando tipo de arquivo proibido: {href}")
                        continue

                    if configuracoes.BLOCK_QUERY_STRING and "?" in href:
                        logger.info(f"[_get_links_from_url] Ignorando link com query string: {href}")
                        continue

                    links.add(href)

            logger.info(f"[_get_links_from_url] Total de links únicos extraídos: {len(links)}")
            return [UrlInfo(link=l) for l in links]
        except Exception as e:
            logger.error(f"[_get_links_from_url] Falha na extração: {e}")
            return []
        
    def craw_paginas_ufsm(self):
        try:
            count_urls = 0
            count_salvar = 0
            while count_urls < 10000 and self.urls_para_visitar:
                url_info = self.urls_para_visitar.pop(0)  # sempre um UrlInfo
                try:
                    logger.info(f"[craw_paginas_ufsm] Processando URL: {url_info.link}")

                    novos_links = self._get_links_from_url(url_info)

                    if url_info.status == 200:
                        self.urls_visitadas.append(url_info)

                        for nl in novos_links:
                            if all(nl.link != u.link for u in (self.urls_visitadas + self.urls_para_visitar + self.urls_com_erro)):
                                self.urls_para_visitar.append(nl)
                    else:
                        self.urls_com_erro.append(url_info)

                except Exception as e:
                    logger.error(f"[craw_paginas_ufsm] Falha ao processar {url_info.link}: {e}")
                    url_info.status = url_info.status or 0
                    self.urls_com_erro.append(url_info)
                finally:
                    count_urls += 1
                    count_salvar += 1
                    if(count_salvar == 10):
                        url_gerenciador.salva_urls_visitadas(self.urls_visitadas)
                        url_gerenciador.salva_urls_nao_visitadas(self.urls_para_visitar)
                        url_gerenciador.salva_urls_com_erro(self.urls_com_erro)
                        logger.info("[craw_paginas_ufsm] Estado atual salvo em JSON")
                        count_salvar = 0
                    time.sleep(configuracoes.DELAY_REQUISICAO)

        except Exception as e:
            logger.error(f"[craw_paginas_ufsm] Falha no crawler: {e}")

    def filtrar_urls_proibidas(self):
        """Remove de todas as listas e dos arquivos JSON as URLs que contenham partes proibidas do robots.txt
        ou terminem com extensões não permitidas (pdf, planilhas, docs etc.)"""

        def permitido(url_info: UrlInfo) -> bool:
            # bloqueio por robots.txt
            if any(dis in url_info.link for dis in configuracoes.DISALLOW_PATHS):
                return False
            # bloqueio por extensão
            if any(url_info.link.lower().endswith(ext) for ext in configuracoes.DISALLOW_EXTENSIONS):
                return False
            
            if configuracoes.BLOCK_QUERY_STRING and "?" in url_info.link:
                return False
            
            return True

        antes_v = len(self.urls_visitadas)
        antes_nv = len(self.urls_para_visitar)
        antes_e = len(self.urls_com_erro)

        # Filtra listas em memória
        self.urls_visitadas = [u for u in self.urls_visitadas if permitido(u)]
        self.urls_para_visitar = [u for u in self.urls_para_visitar if permitido(u)]
        self.urls_com_erro = [u for u in self.urls_com_erro if permitido(u)]

        # Sobrescreve os arquivos JSON já filtrados
        url_gerenciador.salva_urls_visitadas(self.urls_visitadas)
        url_gerenciador.salva_urls_nao_visitadas(self.urls_para_visitar)
        url_gerenciador.salva_urls_com_erro(self.urls_com_erro)

        logger.info(
            f"[ROBOTS] Filtradas URLs proibidas/extensões - "
            f"visitadas: {antes_v}->{len(self.urls_visitadas)}, "
            f"não visitadas: {antes_nv}->{len(self.urls_para_visitar)}, "
            f"com erro: {antes_e}->{len(self.urls_com_erro)}"
        )

        
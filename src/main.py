from src.crawler.crawler_distribuido import CrawlerUFSM
from src.database.db_handler import DbHandler
import src.crawler.url_gerenciador as url_gerenciador
import src.relatorio.gerador_relatorio as gerador_relatorio
def main():
    scrapper = CrawlerUFSM()

    #scrapper.craw_paginas_ufsm()

    gerador_relatorio.relatorio_basico()

    #scrapper.filtrar_urls_proibidas()

if __name__ == "__main__":
    main()
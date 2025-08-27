from src.crawler.crawler_distribuido import CrawlerUFSM
from src.database.db_handler import DbHandler
import src.crawler.url_gerenciador as url_gerenciador

def main():
    url = "https://www.ufsm.br/"

    scrapper = CrawlerUFSM()

    db = DbHandler()

    url_visitada = [
        {
        "link": "https://www.teste.br/",
        },
         {
        "link": "https://www.ufsm.br/",
        }
    ]

    scrapper.craw_paginas_ufsm()

    #print(url_gerenciador.carrega_urls_visitadas())

    #db.set_urls_visitadas(url_visitada)

    #print(url_gerenciador.carrega_urls_visitadas())
    #teste = scrapper.fazer_requisicao(url)

if __name__ == "__main__":
    main()
from src.crawler.crawler_distribuido import CrawlerUFSM
from src.database.db_handler import DbHandler

def main():
    url = "https://www.ufsm.br/"

    scrapper = CrawlerUFSM()

    db = DbHandler()

    url_visitada = [
        {
        "link": "https://www.teste.br/"
        }
    ]

    db.set_urls_visitadas(url_visitada)

    ler =  db.get_urls_visitadas()

    print(ler)
    #teste = scrapper.fazer_requisicao(url)

if __name__ == "__main__":
    main()
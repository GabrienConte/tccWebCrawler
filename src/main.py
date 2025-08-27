from crawler.crawler_distribuido import CrawlerUFSM

def main():
    url = "https://www.ufsm.br/"

    scrapper = CrawlerUFSM()

    teste = scrapper.fazer_requisicao(url)

if __name__ == "__main__":
    main()
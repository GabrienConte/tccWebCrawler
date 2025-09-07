from src.crawler.crawler_distribuido import CrawlerUFSM

crawlerUFSM = CrawlerUFSM() 

def relatorio_basico ():

    antes_v = len(crawlerUFSM.urls_visitadas)
    antes_nv = len(crawlerUFSM.urls_para_visitar)
    antes_e = len(crawlerUFSM.urls_com_erro)

    print(
            f"URLS ATÉ O MOMENTO "
            f"visitadas: {antes_v} "
            f"não visitadas: {antes_nv} "
            f"com erro: {antes_e}"
        )
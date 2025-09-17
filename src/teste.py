from src.crawler.crawler_distribuido import CrawlerUFSM
import src.relatorio.gerador_relatorio as gerador_relatorio

gerador_relatorio.relatorio_basico()

scrapper = CrawlerUFSM()
# scrapper.filtrar_urls_proibidas()

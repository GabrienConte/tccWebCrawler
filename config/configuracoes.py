from pathlib import Path

DELAY_REQUISICAO = 4 # em segundos
MAX_REQUISICAO = 5 # Para testes

URL_BASE_UFSM_PORTAL = "https://www.ufsm.br/"
URL_ASES = "https://asesweb.governoeletronico.gov.br/"

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "src" / "database"

ARQUIVO_URLS_VISITADAS = DATABASE_DIR / "links_ufsm_visitados.json"
ARQUIVO_URLS_NAO_VISITADAS = DATABASE_DIR / "links_nao_visitados.json"
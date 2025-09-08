from pathlib import Path

DELAY_REQUISICAO = 3 # em segundos
MAX_REQUISICAO = 5 # Para testes

URL_BASE_UFSM_PORTAL = "https://www.ufsm.br/"
URL_ASES = "https://asesweb.governoeletronico.gov.br/"

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "src" / "database"

ARQUIVO_URLS_VISITADAS = DATABASE_DIR / "links_ufsm_visitados.json"
ARQUIVO_URLS_NAO_VISITADAS = DATABASE_DIR / "links_nao_visitados.json"
ARQUIVO_URLS_COM_ERRO = DATABASE_DIR / "links_com_erro.json"

DISALLOW_PATHS = [
    "/feed/",
    "/wp-admin/",
    "/wp-includes/",
    "/wp-content",
    "/xmlrpc.php",
    "/wp"
]

DISALLOW_EXTENSIONS = [
    ".pdf", ".xls", ".xlsx", ".csv", ".doc", ".docx", ".ods", ".odt", ".jpg", ".jpeg", ".png"
]

# Bloquear URLs com query string (?param=valor)
BLOCK_QUERY_STRING = True
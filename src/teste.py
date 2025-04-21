from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.ufsm.br/")

soup = BeautifulSoup(html, "html.parser")

body_find = soup.find('body')

regex_href = re.compile(r'(https?\:\/\/(www\.)?(portal.)?ufsm[^\'\"]+)|(^\/[^\'\"]+)$', re.IGNORECASE)

anchors = body_find.find_all('a', href=True)

hrefs = []

for anchor in anchors: hrefs.append(anchor['href'])

matches = re.findall(regex_href, str(hrefs))

for match in matches: print(match)

print(len(matches))
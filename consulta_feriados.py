import requests
from bs4 import BeautifulSoup


url = "https://www.calendarr.com/brasil/feriados-nacionais-e-pontos-facultativos/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


table = soup.find('table')
trs = table.find_all('tr')
feriado = []
for tr in trs:
    ativo = tr.find_all('td')
    feriados = {
        ativo[0].find('a').text
    }
    feriados.append(feriado)
    print(tr)

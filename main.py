import requests
import io
from bs4 import BeautifulSoup
import re

cookies = {
    'MEMAAABBBCCDEEFGGGH_XX':"________________________________"
    'Domain':"aaa.bbb.it",
    }

def cleanhtml(raw_html):
    raw_html = str(raw_html).replace("•", "")
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantextspace = re.sub(' +', ' ', cleantext.strip().replace('\n','').replace('\r',''))
    return cleantextspace

with io.open("graduatoria.csv", "w", encoding="utf-8") as f:
    for cont in range(1,196):
        url = "https://aaa.bbb.it/aaa_graduatoria.php?user=MEMAAABBBCCDEEFGGGH_XX&year_aaa=2021&page="+str(cont)

        page = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(page.content, 'html.parser')

        tabelle = soup.find_all(class_="table")
        for tabella in tabelle:
            bstabella = BeautifulSoup(str(tabella), 'html.parser')
            righe = bstabella.find_all("tr")

            if(len(righe)>0):

                for riga in righe:
                    bsriga = BeautifulSoup(str(riga), 'html.parser')
                    colonne = bsriga.find_all("td")

                    if(len(colonne)>0):
                        risultato = cleanhtml(colonne[0]) + "|" + cleanhtml(colonne[1]) + "|" + cleanhtml(colonne[6]) + "\n"
                        f.write(risultato)
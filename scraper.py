import requests
from bs4 import BeautifulSoup
import random

def scraperArticleWiki (lien):
    reponse = requests.get(
        url=lien,
    )
    soup = BeautifulSoup(reponse.content, 'html.parser')
    titre = soup.find(id="firstHeading")
    print(titre.text)
    toutLien = soup.find(id="bodyContent").find_all("a")
    random.shuffle(toutLien)
    lienaScraper = 0

    for lien in toutLien :
        if lien['href'].find("/wiki/") == -1 :
            continue
        lienaScraper = lien
        break

    nouveauLien = "https://en.wikipedia.org" + lienaScraper['href']
    scraperArticleWiki (nouveauLien)




scraperArticleWiki("https://en.wikipedia.org/wiki/Web_scraping")



import requests
from bs4 import BeautifulSoup
import random


def scrapeWikiArticle(url):
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    # within the body of the page, pull all link, links use the <a> tag
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # pulls the links that has wiki in them
        if link['href'].find("/wiki/") == -1:
            continue

        # Link here will be scraped next
        linkToScrape = link
        break

    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

# Article we will begin with
scrapeWikiArticle("https://en.wikipedia.org/wiki/Breaking_Bad")

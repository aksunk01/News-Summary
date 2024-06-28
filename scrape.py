from bs4 import BeautifulSoup
import requests
import re

def getArticleLinks():
    url = "https://www.cnn.com/politics"
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")

    '''This gets the headlines for the politics page of CNN'''
    href = doc.find_all("div", class_="container__field-links container_lead-plus-headlines__field-links")
    links = []
    beginning  = "https://www.cnn.com"

    '''This gets and formats the links from the provided headlines'''
    for i in href:
        end = str(i.find("a").get("href"))
        
        link = beginning + end
        links.append(link)
    return(links)

def newsArticle(link):
    url = link
    results = requests.get(url)
    doc = BeautifulSoup(results.text, "html.parser")
    page = doc.find_all("p")

    article_body = ""
    
    for i in page:
        article_body+=i.text

    return (article_body)



   
for i in getArticleLinks():
    print(newsArticle(i))



'''
def newsText(link):
    url = link
    print(url)


page = doc.find_all("p")

article = ""

for i in page:
    article+=i.text

print(article)
'''

from bs4 import BeautifulSoup
import requests
import re
'''url = "https://www.cnn.com/politics"'''
url = "https://www.cnn.com/2024/06/26/politics/supreme-court-abortion-idaho-bloomberg/index.html"
results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")

'''

href = doc.find_all("div", class_="container__field-links container_lead-plus-headlines__field-links")
links = []
beginning = "https://www.cnn.com"

for i in href:
    end = str(i.find("a").get("href"))
    link = beginning + end
    links.append(link)



def newsText(link):
    url = link
    print(url)

'''
page = doc.find_all("p")

article = ""

for i in page:
    article+=i.text







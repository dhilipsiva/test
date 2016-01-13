import requests
from pyquery import PyQuery as pq

PLAY_DOMAIN = "https://play.google.com"
SEARCH_URL = PLAY_DOMAIN + "/store/search?q=%s&c=apps"

print("Enter your search term:")
search_term = input()
url = SEARCH_URL % search_term
print("Requesting URL:", url)
print("======================================================================")
resp = requests.get(url)
doc = pq(resp.content)
for el in doc(".card")[:10]:
    card = pq(el)
    href = card(".cover .card-click-target")[0].attrib.get('href')
    app_id = href.split("=")[1]
    print("Getting Details for:", app_id)
    resp = requests.get(PLAY_DOMAIN + href)
    doc2 = pq(resp.content)
    title = doc2(".id-app-title").text()
    print("Title:", title)
    email = doc2(".dev-link")[1].attrib.get('href').split(":")[1]
    print("Developer Email:", email)
    print("=================================================================")

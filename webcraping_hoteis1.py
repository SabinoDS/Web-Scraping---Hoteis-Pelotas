
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.booking.com/city/br/pelotas-br.pt.html?aid=1702940;label=pelotas-br-BaYZ4W6Zx6qS0O2vuxSFCAS525510290343:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-1626424587:lp9102513:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YcpDr58xwogAwmVmCRFhsnQ;ws=&gad=1&gclid=Cj0KCQjw9fqnBhDSARIsAHlcQYSlV6ZrOyPTKmbyqHYHFOPnTvJrW4bolal1_DedrUr2Yh0IfWVtdAMaAhpYEALw_wcB",headers=headers)

content = response.content
soup = BeautifulSoup(content,"lxml")

top_hoteis = soup.find_all("div",attrs={"class": "lp-bui-section-wrap"})
list_tr = top_hoteis[0].find_all("div",attrs={"class": "sr__card_content"})

list_hoteis =[]
for tr in list_tr:
    dataframe ={}
    dataframe["hotel_name"] = (tr.find("span",attrs={"class": "bui-card__title"})).text.replace('\n', ' ')
    dataframe["preco_diaria"] = (tr.find("div",attrs={"class": "bui-price-display__value bui-f-color-constructive"})).text.replace('\n', ' ')
    dataframe["score"] = (tr.find("div",attrs={"class":"bui-review-score__badge"})).text.replace('\n', ' ')
    dataframe["num_avaliacao"] = (tr.find("div",attrs={"class":"bui-review-score__text"})).text.replace('\n', ' ')
    list_hoteis.append(dataframe)
list_hoteis

df = pd.DataFrame(list_hoteis)
df.to_csv("pel_hoteis.csv",index=False)
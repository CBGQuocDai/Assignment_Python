from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url= 'https://www.footballtransfers.com/us/transfers/confirmed/2023-2024/uk-premier-league'
r= requests.get(url) 
data= bs(r.content,'html.parser')
data2 = data.find('tbody',attrs={'id':'player-table-body'})
print(data2.prettify())
# ans= dict()
# ans['player']=[]
# ans['from']=[]
# ans['to']=[]
# ans['value']=[]
# for x in data2:
#     y= x.find_all('td')
#     for v in y:
#         g= v.find('a').getText()
#         print(g)
#     break
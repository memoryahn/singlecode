from pymongo import MongoClient
import urllib.request
from bs4 import BeautifulSoup
from firebase_admin import db
import re
import datetime

client = MongoClient("mongodb://220.230.124.148:27017")
db = client.gif
gifcoll = db.gifcoll

data = []
resp = []
idx = 0
with urllib.request.urlopen('http://mlbpark.donga.com/mp/b.php?p=1&m=search&b=bullpen&query=gif&select=sct&user=') as url:
    content = url.read()
    soup = BeautifulSoup(content, 'html.parser')
bullpen = soup.find_all('a')

for s in bullpen:
    try:
        prop =s.get('class')
        if prop != None and prop[0] == "bullpenbox":
            resp.append(s.get('href'))            
    except UnicodeEncodeError:
        print("Errror : %d" % (idx))
resp.reverse()
for link in resp:
# try:
    with urllib.request.urlopen(link) as url:
        content = url.read()
        soup = BeautifulSoup(content, 'html.parser')
    title =  soup.find('div',{'class':'titles'})  
    titles = re.search('span\>(.*?)\<\/div',str(title)).group(1)
    gifUrl =  soup.find_all('img')
    artdate =  soup.find_all('em')
    srcs = []
    number = 1
    for art in artdate:
        if '2018' in str(art.get_text):
            number = art.get_text()
    for i in gifUrl:
        if 'dimg' not in i.get('src') and 'image' not in i.get('src'):
            srcs.append(i.get('src'))
    if srcs:
        idx+=1
        print(str(idx))
        num = gifcoll.find({"number":number}).count()
        print(num)
        if num==0:
            data.append({'title':titles,'srcs':srcs,'number':number,'last_update':datetime.datetime.now()})             
    # except:
    #     print('error')        
if data != None:
    gifcoll.insert(data)
client.close()

# print(list(gifcoll.find()))    
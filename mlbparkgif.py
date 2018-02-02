#파이어베이스를 이용한 엠팍의 gif수집
from firebase_admin import credentials
import firebase_admin
import urllib.request
from bs4 import BeautifulSoup
from firebase_admin import db
import os

cred = credentials.Certificate(os.environ['firebaseToken'])
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://pyserver-ahn.firebaseio.com/'
})    

data = []
resp = []
idx = 0
with urllib.request.urlopen('http://mlbpark.donga.com/mp/b.php?p=1&m=search&b=bullpen&query=gif&select=sct&user=') as url:
    content = url.read()
    soup = BeautifulSoup(content, 'html.parser')
bullpen = soup.find_all('a')
data = []
resp = []
idx = 0
for s in bullpen:
    try:
        prop =s.get('class')
        if prop != None and prop[0] == "bullpenbox":
            resp.append(s.get('href'))
            # print(s.get('href'))
    except UnicodeEncodeError:
        print("Errror : %d" % (idx))
    idx += 1
linkCount=0
idx2=0
for link in resp:
    try:
        print(str(idx2))
        with urllib.request.urlopen(link) as url:
            content = url.read()
            soup = BeautifulSoup(content, 'html.parser')
        titles =  soup.find('div',{'class':'titles'})
        gifUrl =  soup.find_all('img')
        artdate =  soup.find_all('em')
        srcs = []
        number = 1
        for art in artdate:
            # print(art.get_text()+'a')
            if '2018' in str(art.get_text):
                number = art.get_text()
                print(number)
        for i in gifUrl:
            if 'dimg' not in i.get('src') and 'image' not in i.get('src'):
            # if 'donga' not in i.get('src'):
                srcs.append(i.get('src'))
        data.append({'title':titles.get_text(),'srcs':srcs,'number':number})
        idx2 += 1
        # if len(srcs) > 0:
            
    except:
        print('error')
pydb = db.reference('getgif')
for d in data:
    newkey = pydb.child(d['number']).update(d)

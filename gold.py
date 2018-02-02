#골드만삭스의 주식매입크롤링
from lxml import html
import requests
import time
import json

count=0
with open('list.txt', encoding='UTF8') as text:
    code=json.load(text)

for i in code:
    page = requests.get('http://finance.naver.com/item/main.nhn?code='+i[1])
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    buy1 = tree.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[2]/td[3]/span/text()')
    #This will create a list of prices
    buy2 = tree.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[3]/td[3]/span/text()')
    buy3 = tree.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[4]/td[3]/span/text()')
    buy4 = tree.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[5]/td[3]/span/text()')
    buy5 = tree.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[6]/td[3]/span/text()')

    print('title: '+i[0])
    print ('1: '+str(buy1))
    print ('2: '+str(buy2))
    print ('3: '+str(buy3))
    print ('4: '+str(buy4))
    print ('5: '+str(buy5))
    print(str(count))
    count+=1
    time.sleep(1)
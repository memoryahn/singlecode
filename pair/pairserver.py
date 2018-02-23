from flask import Flask, jsonify, request
import urllib.request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def get_pair():
    btcdata={
        'name':'비트코인',
        'code':'BTC'
    }
    bchdata={
        'name':'비트코인캐시',
        'code':'BCH'
    }
    ethdata={
        'name':'이더리움',
        'code':'ETH'
    }
    ltcdata={
        'name':'라이트코인',
        'code':'LTC'
    }
    upbit=[
        {'code':'BTC'},
        {'code':'BCC'},
        {'code':'ETH'},
        {'code':'LTC'}
    ]
    gopax=[
        {'code':'BTC'},
        {'code':'BCH'},
        {'code':'ETH'},
        {'code':'LTC'}
    ]
    bithumb=[
        {'code':'BTC'},
        {'code':'BCH'},
        {'code':'ETH'},
        {'code':'LTC'}
    ]
    for code in upbit:
        url='https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-'+code['code']+'&count=1'
        headersObject = { 'User-Agent': '', 'Accept': '*/*' }
        with urllib.request.urlopen(urllib.request.Request(url, headers = headersObject)) as coinUrl:
            coinData = coinUrl.read()
            encoding = coinUrl.info().get_content_charset('utf-8')    
            tradePrice=json.loads(coinData.decode(encoding))[0]['tradePrice']
            candleDateTimeKst=json.loads(coinData.decode(encoding))[0]['candleDateTimeKst']
            openingPrice=json.loads(coinData.decode(encoding))[0]['openingPrice']
            highPrice=json.loads(coinData.decode(encoding))[0]['highPrice']
            lowPrice=json.loads(coinData.decode(encoding))[0]['lowPrice']
        if code['code'] == 'BTC':
            btcdata['upbit']=tradePrice
        elif code['code'] == 'BCC':
            bchdata['upbit']=tradePrice
        elif code['code'] == 'ETH':
            ethdata['upbit']=tradePrice
        elif code['code'] == 'LTC':
            ltcdata['upbit']=tradePrice
    # tempdate = data[0]['candleDateTimeKst'].replace("+09:00","")
    # d =datetime.strptime(tempdate ,'%Y-%m-%dT%H:%M:%S')
    # print(d.hour)
    
    # gopaxUrlbtc='https://api.gopax.co.kr/trading-pairs/BTC-KRW/ticker'
    # gopaxUrlbch='https://api.gopax.co.kr/trading-pairs/BCH-KRW/ticker'
    # gopaxUrleth='https://api.gopax.co.kr/trading-pairs/ETH-KRW/ticker'
    # gopaxUrlltc='https://api.gopax.co.kr/trading-pairs/LTC-KRW/ticker'
    gopaxdata=[]
    for gopa in gopax:
        headersObject = { 'User-Agent': '', 'Accept': '*/*' }
        gourl='https://api.gopax.co.kr/trading-pairs/'+gopa['code']+'-KRW/ticker'
        with urllib.request.urlopen(urllib.request.Request(gourl, headers = headersObject)) as gopaxUrl:
            gopaxbtcData = gopaxUrl.read()
            encoding = gopaxUrl.info().get_content_charset('utf-8')    
            goprice=json.loads(gopaxbtcData.decode(encoding))['price']
        if gopa['code'] == 'BTC':
            btcdata['gopax'] = goprice
        elif gopa['code'] == 'BCH':
            bchdata['gopax'] = goprice
        elif gopa['code'] == 'ETH':
            ethdata['gopax'] = goprice
        elif gopa['code'] == 'LTC':
            ltcdata['gopax'] = goprice
    
    bithumbdata=[]
    for bit in bithumb:
        headersObject = { 'User-Agent': '', 'Accept': '*/*' }
        biturl='https://api.bithumb.com/public/ticker/'+bit['code']
        with urllib.request.urlopen(urllib.request.Request(biturl, headers = headersObject)) as bitUrl:
            bitData = bitUrl.read()
            encoding = bitUrl.info().get_content_charset('utf-8')    
            bitprice=json.loads(bitData.decode(encoding))['data']['closing_price']
        if bit['code'] == 'BTC':
            btcdata['bithumb'] = bitprice
        elif bit['code'] == 'BCH':
            bchdata['bithumb'] = bitprice
        elif bit['code'] == 'ETH':
            ethdata['bithumb'] = bitprice
        elif bit['code'] == 'LTC':
            ltcdata['bithumb'] = bitprice
    data=[]
    data.append(btcdata)
    data.append(bchdata)
    data.append(ethdata)
    data.append(ltcdata)
    # return jsonify({'btc':btcdata,'bch':bchdata,'eth':ethdata,'ltc':ltcdata})
    return jsonify(data)
if __name__=='__main__':
    app.run(debug=True)

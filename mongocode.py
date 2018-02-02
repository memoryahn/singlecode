from bson.json_util import dumps
from pymongo import MongoClient

client = MongoClient("mongodb://220.230.124.148:27017")
db = client.gif
gifcoll = db.list_collections()
data=[]
for i in list(gifcoll):
    data.append(i['name'])
client.close()    
print(data)
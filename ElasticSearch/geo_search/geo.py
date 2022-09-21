from datetime import datetime
from elasticsearch import Elasticsearch
from time import time 

from pymongo import MongoClient

import warnings 
warnings.filterwarnings("ignore")

from utils.query import body_1km, body_5km, body_30km, body_50km, settings

t1 = time()

client = MongoClient()
airData = client["airData"]
outsidepredict = airData['outsidepredict']

host='http://localhost:9200'
es = Elasticsearch([host])

my = es.indices.create(index = "test_index", ignore=400, body=settings)

#curl http://localhost:9200/_aliases
#curl -X DELETE "localhost:9200/test_index"
  
for idx, data in enumerate(list(outsidepredict.find({},{"_id":0}))):
    es.index(index="test_index", document=data, id = idx)

resp_all = es.search(index="test_index", size=10000, query = {
        "match_all": {}
    })

t1 = time()

resp_1km = es.search(index="test_index", size=10000, body=body_1km)

resp_5km = es.search(index="test_index", size=10000, body=body_5km)

resp_30km = es.search(index="test_index", size=10000, body=body_30km)

resp_50km = es.search(index="test_index", size=10000, body=body_50km)

print(len(resp_all['hits']['hits']))
print(len(resp_1km['hits']['hits']))
print(len(resp_5km['hits']['hits']))
print(len(resp_30km['hits']['hits']))
print(len(resp_50km['hits']['hits']))


for i in resp_5km['hits']['hits']:
    print(i['_source'])
    
print(time()-t1)
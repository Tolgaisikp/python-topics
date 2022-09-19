from datetime import datetime
from elasticsearch import Elasticsearch

host='http://localhost:9200'
es = Elasticsearch([host])

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
print("LOG1:",resp['result'])

resp = es.get(index="test-index", id=1)
print("LOG2:",resp['_source'])

es.indices.refresh(index="test-index")

resp = es.search(index="test-index", query={"match_all": {}})
print("LOG3:", resp)
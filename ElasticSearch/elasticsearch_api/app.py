from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
import json

host='http://localhost:9200'
es = Elasticsearch([host])
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    results = es.get(index='contents', id='1')
    return jsonify(results['_source'])

@app.route('/insert_data', methods=['POST'])
def insert_data():
    slug = request.form['slug']
    title = request.form['title']   
    content = request.form['content']
    
    body = {
        'slug': slug,
        'title': title,
        'content': content,
        'timestamp': datetime.now()
    }
    
    result = es.index(index='contents', id=slug, body=body)
    return {"result":result['result']}

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["content", "title"]
            }
        }
    }
    res = es.search(index="contents", body=body)
    return jsonify(res['hits']['hits'][0]['_source'])

app.run(port=5000, debug=True)

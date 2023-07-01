from elasticsearch import Elasticsearch

host = 'http://localhost:9200'

es = Elasticsearch([host])

if es.ping():
    print('Connected to ES!')
else:
    print('Could not connect!')

print(es.info())
from elasticsearch import Elasticsearch

host = 'http://localhost:9200'

es = Elasticsearch([host])

settings = {
    'settings': {
        'number_of_shards': 1,
        'number_of_replicas': 0
    },
    'mappings': {
        'properties': {
            'title': {
                'type': 'text'
            },
            'body': {
                'type': 'text'
            },
        }
    }
}

es.indices.create(index='test-index', ignore=400, body=settings)

# Import the client from the 'elasticsearch' module

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class MyElastic:
    __address = "http://localhost:9200"

    def __init__(self):
        self.__client = Elasticsearch(self.__address)

    def get_info(self):
        return(self.__client.info())

    def create_index(self, index_name='test'):
        '''
        Create an index and its mapping
        '''
        self.__index_mappings = {
            "settings": {
                "number_of_shards": 2,
                "number_of_replicas": 0,
                "analysis": {
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_smart"
                }
            },
            "mappings": {
                "properties": {
                    "building_name": {
                        "type": "text"
                    },
                    "date": {
                        "type": "text"
                    },
                    "cover_rate":{
                        "type":"integer"
                    },
                    "location": {
                        "type": "geo_point"
                    }
                }
            }
        }
        if self.__client.indices.exists(index=index_name) is not True:
            result = self.__client.indices.create(index=index_name, body=self.__index_mappings)
            print(result)

    def full_text_query(self, index_name: str, field: str, search_term):
        query = {
            "query": {
                "match": {
                    field: search_term
                }
            }
        }
        result = self.__client.search(index=index_name, body=query)
        for hit in result['hits']['hits']:
            print(hit['_source']['building_name'])

    def arc_query(self, index_name: str, lon: float, lat: float, radius: str):
        query = {
            "query": {
                "bool": {
                    "filter": {
                        "geo_distance": {
                            "distance": radius,
                            "distance_type": "arc",
                            "_name": "optional_name",
                            "location": {
                                "lat": lat,
                                "lon": lon
                            }
                        }
                    }
                }
            }
        }
        result = self.__client.search(index=index_name, body=query)
        for hit in result['hits']['hits']:
            print(hit['_source']['building_name'])

    def bulk_index_docs(self, index_name, doc_list):
        actions = []
        i = 1
        for doc in doc_list:
            actions.append({
                "_index": index_name,
                "_id": i,
                "_source": {
                    "building_name": doc['building_name'],
                    "location": doc['location']
                }
            })
            i += 1

        # 批量处理
        success, _ = bulk(self.__client, actions, index=index_name, raise_on_error=True)
        print('Successfully added %d docs' % success)

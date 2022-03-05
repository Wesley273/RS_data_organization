# Import the client from the 'elasticsearch' module

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class MyElastic:
    __address = "http://localhost:9200"
    __index_name = "test-index"

    def __init__(self):
        self.__client = Elasticsearch(self.__address)

    def get_info(self):
        return(self.__client.info())

    def create_index(self, __index_name='test'):
        '''
        Create an index and its mapping
        '''
        self._index_mappings = {
            "settings": {
                "number_of_shards": 2,
                "number_of_replicas": 2,
                "analysis": {
                    "analyzer": {
                        "default": {
                            "type": "ik_max_word"
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "building_name": {
                        "type": "keyword"
                    },
                    "location": {
                        "type": "geo_point"
                    }
                }
            }
        }
        if self.__client.indices.exists(index=__index_name) is not True:
            result = self.__client.indices.create(index=__index_name, body=self._index_mappings)
            print(result)

    def index_doc(self, index_name, doc):
        actions = []
        actions.append({
            "_index": index_name,
            "_id": 1,
            "_source": {
                "building_name": doc['building_name'],
                "location": doc['location']
            }
        })
        # 批量处理
        success, _ = bulk(self.__client, actions, index=index_name, raise_on_error=True)
        print('Successfully Performed %d actions' % success)

    def bulk_index_docs(self, index_name, doc_list):
        '''
        用bulk将批量数据存储到es
        '''
        actions = []
        for doc in doc_list:
            actions.append({
                "_index": index_name,
                "_id": doc['code'],
                "_source": {
                    "date": doc['date'],
                    "source": doc['source'],
                    "link": doc['link'],
                    "keyword": doc['keyword'],
                    "title": doc['title']}
            })
            # 批量处理
        success, _ = bulk(self.__client, actions, index=index_name, raise_on_error=True)
        print('Successfully Performed %d actions' % success)

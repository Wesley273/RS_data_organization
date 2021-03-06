# Import the client from the 'elasticsearch' module

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class MyElastic:

    def __init__(self):
        self.__address = "http://localhost:9200"
        self.__client = Elasticsearch(self.__address)

    def get_info(self):
        return(self.__client.info())

    def delete_doc(self, index_name, id):
        self.__client.delete(index_name, id)

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
                    "name": {
                        "type": "text"
                    },
                    "date": {
                        "type": "date"
                    },
                    "cover_rate": {
                        "type": "integer"
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

    def bulk_index_docs(self, index_name, doc_list):
        actions = []
        for doc in doc_list:
            actions.append({
                "_index": index_name,
                "_id": doc['code'],
                "_source": {
                    "name": doc['name'],
                    "date": doc['date'],
                    "cover_rate": doc['cover_rate'],
                    "location": doc['location']
                }
            })
        # 批量处理
        success, _ = bulk(self.__client, actions, index=index_name, raise_on_error=True)
        print('Successfully added %d docs' % success)

    def id_query(self, id: str, index_name: str, output: bool):
        query = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": {"match": {"_id": id}}
                }
            }
        }
        result = self.__client.search(index=index_name, body=query)
        if(output):
            print(f'对id:"{id}"搜索完成,耗时: ', result['took'], 'ms, 结果如下:')
            for hit in result['hits']['hits']:
                print(hit['_source'])
        return result

    def full_text_query(self, begin_date: str, end_date: str, index_name: str, field: str, search_term, match_degree: str, output: bool):
        query = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {"range": {"date": {"gte": begin_date, "lte": end_date}}},
                        {"match": {
                            field: {
                                "query": search_term,
                                "minimum_should_match": match_degree
                            }
                        }}
                    ]
                }
            }
        }
        result = self.__client.search(index=index_name, body=query)
        if(output):
            print('全文搜索完成,耗时: ', result['took'], 'ms, 结果如下:')
            for hit in result['hits']['hits']:
                print(hit['_source'])
        return result

    def arc_query(self, date: str, index_name: str, lon, lat, radius: str, output: bool):
        query = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": {"match": {"date": date}},
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
        if(output):
            print('范围搜索完成,耗时: ', result['took'], 'ms, 结果如下:')
            for hit in result['hits']['hits']:
                print(hit['_source'])
        return result

    def date_query(self, date: str, index_name: str, output: bool):
        query = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": {"match": {"date": date}}
                }
            }
        }
        result = self.__client.search(index=index_name, body=query)
        if(output):
            print(f'对{date}日搜索完成,耗时: ', result['took'], 'ms, 结果如下:')
            for hit in result['hits']['hits']:
                print(hit['_source'])
        return result

    def scroll_date_query(self, begin_date: str, end_date: str, index_name: str, output: bool):
        query = {
            "query": {
                "bool": {
                    "must": {"range": {"date": {"gte": begin_date, "lte": end_date}}}
                }
            }
        }
        result = self.__client.search(index=index_name, scroll='5m', timeout='3s', size=100, body=query)
        mdata = result.get("hits").get("hits")
        if not mdata:
            print('empty!')
        scroll_id = result["_scroll_id"]
        for i in range(0, int(result["hits"]["total"]['value']/100+1)):
            res = self.__client.scroll(scroll_id=scroll_id, scroll='5m')  # scroll参数必须指定否则会报错
            mdata += res["hits"]["hits"]
            # print(res)
        # print(len(mdata))
        return mdata

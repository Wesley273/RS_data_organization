from database.my_elastic import MyElastic
from database.my_hbase import MyHBase


class MySystem:
    def __init__(self):
        self.__hbase = MyHBase()
        self.__es = MyElastic()

    def __merge_result(self, index_name, es_result):
        merged = []
        for hit in es_result['hits']['hits']:
            hit['_source']['comment'] = self.__hbase.get_row(index_name, hit['_id'], True)['comment']
            merged.append(hit['_source'])
        return merged

    def arc_query(self, date, index_name, lon, lat, radius, output: bool, full: bool):
        es_result = self.__es.arc_query(date, index_name, lon, lat, radius, False)
        result = self.__merge_result(index_name, es_result)
        if(output):
            print(result)
        if(full):
            return result
        else:
            return es_result

    def get_row(self, rowkey: str, index_name: str, output: bool, full: bool):
        es_result = self.__es.id_query(rowkey, index_name, False)
        result = self.__merge_result(index_name, es_result)
        if(output):
            print(result)
        if(full):
            return result
        else:
            return es_result

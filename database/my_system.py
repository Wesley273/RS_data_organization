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

    def arc_query(self, date, index_name, lon, lat, radius,  full: bool):
        es_result = self.__es.arc_query(date, index_name, lon, lat, radius, False)
        if(full):
            merged = self.__merge_result(index_name, es_result)
            return merged
        else:
            return es_result['hits']['hits']

    def full_text_query(self, begin_date: str, end_date: str, index_name: str, field: str, search_term, match_degree: str, full: bool):
        es_result = self.__es.full_text_query(begin_date, end_date, index_name, field, search_term, match_degree, output=False)
        if(full):
            merged = self.__merge_result(index_name, es_result)
            return merged
        else:
            return es_result['hits']['hits']

    def date_query(self, begin_date: str, end_date: str, index_name: str, full: bool):
        es_result = self.__es.scroll_date_query(begin_date, end_date, index_name, output=False)
        if(full):
            merged = []
            for hit in es_result:
                hit['_source']['comment'] = self.__hbase.get_row(index_name, hit['_id'], True)['comment']
                merged.append(hit['_source'])
            return merged
        else:
            return es_result['hits']['hits']

    def get_row(self, rowkey: str, index_name: str,  full: bool):
        es_result = self.__es.id_query(rowkey, index_name, False)
        if(full):
            result = self.__merge_result(index_name, es_result)
            return result
        else:
            return es_result['hits']['hits']

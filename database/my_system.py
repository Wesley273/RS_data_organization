from database.my_elastic import MyElastic
from database.my_hbase import MyHBase


class MySystem:
    def __init__(self):
        self.__hbase = MyHBase()
        self.__es = MyElastic()

    def print_result(self, result):
        for hit in result:
            print(hit['_source'])

    def __merge_result(self, index_name, es_result):
        merged = []
        for hit in es_result['hits']['hits']:
            hit['_source']['comment'] = self.__hbase.get_row(index_name, hit['_id'], True)['comment']
            merged.append(hit)
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
                merged.append(hit)
            return merged
        else:
            return es_result

    def delete_row(self, rowkey: str, index_name: str):
        self.__es.delete_doc(index_name, rowkey)
        self.__hbase.delete_row(index_name, rowkey)

    def get_row(self, rowkey: str, index_name: str):
        result = {}
        location = {}
        row = self.__hbase.get_row(index_name, rowkey, True)
        result['name'] = row['name']
        result['date'] = row['date']
        result['cover_rate'] = row['cover_rate']
        location['lon'] = row['lon']
        location['lat'] = row['lat']
        result['location'] = location
        result['comment'] = row['comment']
        return result

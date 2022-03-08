import time

import generate_pois
import indexing.projection
from database.my_elastic import MyElastic

test_doc_list = [{
    "code": 1213,
    "name": generate_pois.gen_name(),
    "date": "2020-01-02",
    "cover_rate": 90,
    "location": {"lat": 31.256224, "lon": 121.462311}
}, {
    "code": 2432,
    "date": "2020-01-03",
    "cover_rate": 90,
    "name": generate_pois.gen_name(),
    "location": "POINT (121.460186 31.251281)"
}, {
    "code": 3543,
    "date": "2020-01-04",
    "name": generate_pois.gen_name(),
    "cover_rate": 90,
    "location": "POINT (121.473939 31.253531)"
}, {
    "code": 3244,
    "date": "2020-01-05",
    "name": generate_pois.gen_name(),
    "cover_rate": 90,
    "location": "POINT (121.448215 31.26229)"

}]


def arcquery_using_haversine(datequery_result, lon, lat, radius):  # radius:km
    result = []
    for hit in datequery_result['hits']['hits']:
        lat1 = hit['_source']['location']['lat']
        lon1 = hit['_source']['location']['lon']
        if(indexing.projection.get_distance(lon, lat, lon1, lat1) <= radius):
            result.append(hit['_source'])
    return result


def cost_time(date: str, index_name: str, lon: float, lat: float, radius: int, count: int):  # radius:km
    time_start = time.time()
    for i in range(1, count+1):
        # print(f'第{i}次测试')
        result = es.date_query(date, index_name, output=False)
        arcquery_using_haversine(result, lon, lat, radius)
    time_end = time.time()
    return time_end-time_start


if __name__ == "__main__":
    # basic infos
    es = MyElastic()
    # print(es.get_info())
    # es.create_index('test')

    # test inserting
    #es.bulk_index_docs('test', test_doc_list)

    # test arc_query
    es.arc_query("2021-04-20", "test", 100, 32, '2000km', output=True)

    # test full_text_query
    #es.full_text_query("2021-04-01", "test", "name", "合山亮",output=True)

    # test date_query
    es.date_query("2021-04-20", "test", output=True)

    # test the cost time of query based on Haversine method
    #print(cost_time(date="2021-04-20", index_name="test", lon=100, lat=32, radius=2000, count=100)*10, "ms")

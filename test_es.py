import datetime
import random
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


def arcquery_using_haversine(datequery_result, lon, lat, radius, output: bool):  # radius:km
    result = []
    if(output):
        print("Haversine法结果如下:")
    htime_start = time.time()
    for hit in datequery_result['hits']['hits']:
        lat1 = hit['_source']['location']['lat']
        lon1 = hit['_source']['location']['lon']
        if(indexing.projection.get_distance(lon, lat, lon1, lat1) <= radius):
            result.append(hit['_source'])
            if(output):
                print(hit['_source'])
    htime_end = time.time()
    htime = 1000*(htime_end-htime_start)
    return result, htime


def random_parameter():
    begin_day = datetime.date(2021, 1, 31)
    date = str(begin_day + datetime.timedelta(random.randint(1, 365)))
    radius = random.randint(5000, 6000)
    lon = float(random.randint(77, 92))
    lat = float(random.randint(21, 40))
    return date, radius, lon, lat


def cost_time(index_name: str,  count: int):  # radius:km
    # Haversine法测试
    htime = 0
    arctime = 0
    for i in range(1, count+1):
        date, radius, lon, lat = random_parameter()
        result = es.date_query(date, index_name, output=False)
        htime += result['took']
        _, cost = arcquery_using_haversine(result, lon, lat, radius, output=False)
        htime += cost
    # arc_query法测试
        result = es.arc_query(date, "test", lon, lat, str(radius)+"km", output=False)
        arctime += result['took']
    return htime/count, arctime/count


if __name__ == "__main__":
    # basic infos
    es = MyElastic()
    # print(es.get_info())
    # es.create_index('test')

    # test inserting
    #es.bulk_index_docs('test', test_doc_list)

    # test arc_query
    #es.arc_query("2021-04-20", "test", 100, 32, '1000km', output=True)

    # test full_text_query
    #es.full_text_query("2021-04-01", "test", "name", "合山亮",output=True)

    # test date_query
    #print(es.date_query("2021-04-20", "test", output=True))

    # test the cost time of query based on Haversine method
    print(cost_time('test', 1))

import datetime
import random
import time
import numpy as np

import pandas as pd

import indexing.projection
from database.my_elastic import MyElastic


def fixed_p(pixel: int):
    p = 0.5
    if (random.random() <= p):
        return True
    else:
        return False


def practical_p(pixel: int):
    p = 0.00003*pixel
    if (random.random() <= p):
        return True
    else:
        return False


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


def id_query_cost(csv_name: str, client, index_name, encoder: str, label: str):
    tables = pd.read_csv(f"data\\poi\\{csv_name}.csv")
    cost = 0
    count = 0
    for code, date, name, lon, lat, row, col, cover_rate, comment, lab in tables.iloc:
        if(lab == label):
            if encoder == 'xoy':
                code = '29A'+str(row*1000+col)
            if encoder == 'hilbert':
                code = code
            start = time.time()
            client.id_query(code, index_name, output=False)
            end = time.time()
            cost += (end-start)*1000
            count += 1
            # print(f'已测试{count}条')
    print(f'平均用时{cost/count}ms, 共{count}次查询')
    return cost/count, count


def test_arc_query(radius: str):
    cost_list = np.zeros(100)
    rand_lon = random.randint(80, 85)
    rand_lat = random.randint(20, 35)
    for i in range(0, 100):
        result = es.arc_query("2021-03-01", "test", rand_lon, rand_lat, radius, output=False)
        total = result['hits']['total']
        cost_list[i] = result['took']
    return total, cost_list


if __name__ == "__main__":
    # basic infos
    es = MyElastic()
    # print(es.get_info())
    # es.create_index('test')

    # test inserting
    # es.bulk_index_docs('test', test_doc_list)

    # test id_query
    #es.id_query("1A262373", "test", output=True)

    # test arc_query
    #result = es.arc_query("2021-03-01", "test-large", 80, 32, '250km', output=False)
    #total, cost_list = test_arc_query('5000km')
    # print(total,cost_list.mean())

    # test full_text_query
    #es.full_text_query("2021-03-01", "2021-03-01", "test", "name", "沈阳龙科考站", "95%", output=True)

    # test date_query
    # print(es.date_query("2021-04-20", "test", output=True))

    # test scroll query
    #es.scroll_date_query("2021-02-01", "2022-02-02", "test", output=False)

    # test id_query cost time
    cost_total = 0
    encoder = 'xoy'
    label = 'equably'
    for i in range(1, 101):
        cost, _ = id_query_cost('test_id_query',  es, 'test-large', encoder, label)
        cost_total += cost
    print(cost_total/100, encoder, label)

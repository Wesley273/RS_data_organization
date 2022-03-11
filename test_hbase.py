import random
import time
import pandas as pd

from database.my_hbase import MyHBase


def probability(pixel: int):
    p = 0.00002*pixel
    if (random.random() <= p):
        return True
    else:
        return False


def save2hbase(csv_name: str, hbase_client, index_name):
    tables = pd.read_csv(f"data\\poi\\{csv_name}.csv")
    i = 0
    for code, date, name, lon, lat, row, col, cover_rate, comment in tables.iloc:
        data = {
            'cf1:date': date,
            'cf2:name': name,
            'cf3:lon': str(lon),
            'cf4:lat': str(lat),
            'cf5:row': str(row),
            'cf6:col': str(col),
            'cf7:cover_rate': str(cover_rate),
            'cf8:comment': comment}
        hbase_client.insert_row(index_name, code, data)
        i += 1
        print(f'已存入{i}条')


def test_query_time(csv_name: str, hbase_client, index_name):
    tables = pd.read_csv(f"data\\poi\\{csv_name}.csv")
    cost = 0
    count = 0
    for code, date, name, lon, lat, row, col, cover_rate, comment in tables.iloc:
        if(random.random() <= 0.00017):
            start = time.time()
            hbase_client.get_row(index_name, code, False)
            end = time.time()
            cost += (end-start)*1000
            count += 1
            print(f'已测试{count}条')
    print(f'平均用时{cost/count}ms, 共{count}次查询')
    return cost/count, count


if __name__ == "__main__":
    # initiate the hbase
    hbase = MyHBase()

    # test creat and delete table
    # table=hbase.create_table('test-large')
    # hbase.delete_table('test')

    # save data in csv to hbase
    #save2hbase('2021_3_1', hbase, 'test-large')

    # the time cost of query
    test_query_time('2021_3_1', hbase, 'test-large')

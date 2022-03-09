import csv
import datetime
import random

import pandas as pd
import rasterio
from faker import Faker

from database.my_elastic import MyElastic
from indexing.geo_points import POI


def gen_name():
    fake = Faker("zh_CN")
    return fake.city_name()+fake.first_name_male()+"科考站"


def gen_comment():
    fake = Faker("zh_CN")
    return fake.name()+"负责,地址与联系方式: "+fake.address()+"; "+fake.email()+"; "+fake.phone_number()


def probability(pixel: int):
    p = 0.002*pixel
    if (random.random()*100 <= p):
        return True
    else:
        return False


def gen_pois_nozero(csv_name: str, begin: datetime.date, end: datetime.date):
    file = open(f'data\\poi\\{csv_name}.csv', 'w', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(["code", "date", "name", "lon", "lat", "row", "col", "cover_rate", "comment"])
    for i in range((end-begin).days):
        points = []
        day = begin + datetime.timedelta(days=i)
        print(f"对 {day} 日图像采样····· ")
        ds = rasterio.open(f'data\\img\\NDSI_{str(day).replace("-", "_", 2)}.tif')
        img_array = ds.read(1)
        for row in range(len(img_array)):
            for col in range(len(img_array[row])):
                if(img_array[row][col] > 0):
                    date = int(str(day).replace("-", "", 2))
                    poi = POI(date, row, col, "name", img_array[row][col], "comment")
                    points.append(poi)
                    csv_writer.writerow([poi.code, poi.date, poi.name, poi.lon, poi.lat, row, col, poi.cover_rate, poi.comment])
                    #print("%2d " % (img_array[row][col]), end='')
        print(f"{day} 所含点数: ", len(points))
    file.close()


def gen_pois(csv_name: str, begin: datetime.date, end: datetime.date):
    file = open(f'data\\poi\\{csv_name}.csv', 'w', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(["code", "date", "name", "lon", "lat", "row", "col", "cover_rate", "comment"])
    for i in range((end-begin).days):
        points = []
        day = begin + datetime.timedelta(days=i)
        print(f"对 {day} 日图像采样····· ")
        ds = rasterio.open(f'data\\img\\NDSI_{str(day).replace("-", "_", 2)}.tif')
        img_array = ds.read(1)
        for row in range(len(img_array)):
            for col in range(len(img_array[row])):
                if(probability(img_array[row][col])):
                    date = int(str(day).replace("-", "", 2))
                    poi = POI(date, row, col, gen_name(), img_array[row][col], gen_comment())
                    points.append(poi)
                    csv_writer.writerow([poi.code, poi.date, poi.name, poi.lon, poi.lat, row, col, poi.cover_rate, poi.comment])
                    #print("%2d " % (img_array[row][col]), end='')
        print(f"{day} 所含点数: ", len(points))
    file.close()


def save2es(csv_name: str, client, index_name):
    tables = pd.read_csv(f"data\\poi\\{csv_name}.csv")
    doc_list = []
    for code, date, name, lon, lat, row, col, cover_rate, comment in tables.iloc:
        doc_list.append({
            "code": code,
            "name": name,
            "date": date,
            "cover_rate": cover_rate,
            "location": {"lat": lat, "lon": lon}
        })
        if(len(doc_list) == 10000):
            client.bulk_index_docs(index_name, doc_list)
            doc_list = []
    if(len(doc_list) > 0):
        client.bulk_index_docs(index_name, doc_list)


if __name__ == "__main__":
    # create the client and index
    es = MyElastic()
    # es.create_index('test')

    # generate pois randomly
    begin = datetime.date(2021, 2, 1)
    end = datetime.date(2021, 2, 2)
    #gen_pois("2021_3_1", begin, end)

    # save docs to elasticsearch
    #save2es("2021_3_1", es, 'test1')
    gen_pois_nozero("2021_2_1_nozero", begin, end)

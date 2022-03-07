import csv
import datetime
import random

import rasterio
from faker import Faker

from indexing.geo_points import POI


def gen_name():
    fake = Faker("zh_CN")
    return fake.city_name()+fake.first_name_male()+"科考站"


def gen_comment():
    fake = Faker("zh_CN")
    return fake.name()+"负责,地址与联系方式: "+fake.address()+"; "+fake.email()+"; "+fake.phone_number()


def gen_pois(csv_writer, img_array, date: int):
    points = []
    for row in range(len(img_array)):
        for col in range(len(img_array[row])):
            if(random.random()*100 <= 0.03):
                poi = POI(date, row, col, gen_name(), img_array[row][col], gen_comment())
                points.append(poi)
                csv_writer.writerow([poi.code, poi.date, poi.name, poi.lon, poi.lat, row, col, poi.cover_rate, poi.comment])
                #print("%2d " % (img_array[row][col]), end='')
    return(points)


if __name__ == "__main__":
    begin = datetime.date(2021, 2, 3)
    end = datetime.date(2021, 2, 4)
    file = open(r'data\poi\test.csv', 'a+', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(["code", "date", "name", "lon", "lat", "row", "col", "cover_rate", "comment"])
    # 遍历对每天的遥感图像采样
    for i in range((end - begin).days):
        day = begin + datetime.timedelta(days=i)
        print(f"对 {day} 日图像采样····· ")
        ds = rasterio.open(f'data\\img\\NDSI_{str(day).replace("-", "_", 2)}.tif')
        img_array = ds.read(1)
        points = gen_pois(csv_writer, img_array, int(str(day).replace("-", "", 2)))
        print(f"{day} 所含点数: ", len(points))
    file.close()

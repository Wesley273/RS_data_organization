import random
import rasterio
from indexing.geo_points import POI
from faker import Faker


def export2csv(points):
    plist = []


def gen_name():
    fake = Faker("zh_CN")
    return fake.city_name()+fake.first_name_male()+"科考站"


def gen_comment():
    fake = Faker("zh_CN")
    return fake.address()


def gen_pois(img_array):
    points = []
    for x in range(len(img_array)):
        for y in range(len(img_array[x])):
            if(random.random()*100 < 0.01):
                points.append(POI(20220118, x, y, gen_name(), img_array[x][y], gen_comment()))
                print(img_array[x][y])
    return(points)


if __name__ == "__main__":
    ds = rasterio.open(r'data\img\NDSI_2022_01_18.tif')
    
    img_array = ds.read(1)
    points = gen_pois(img_array)
    print(points[1])
    print(len(points))

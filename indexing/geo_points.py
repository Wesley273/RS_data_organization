from numpy import deg2rad
import rasterio
from indexing import encoder, projection
import pandas as pd


class POI:
    # let the Hilbert curve to cover the entire image
    __n = 2**18
    __left_bound = -3044000
    __top_bound = 5188000
    __cell = 4000

    def __init__(self, time: int, row: int, col: int, name: str, cover_rate: int, comment: str):
        self.code = time + encoder.xy2d(self.__n, row, col)
        self.__geo_x = self.__left_bound + row*self.__cell
        self.__geo_y = self.__top_bound - col*self.__cell
        self.lon, self.lat = projection.xy2lonlat(self.__geo_x, self.__geo_y)
        self.name = name
        self.cover_rate = cover_rate
        self.comment = comment

    def get_geoxy(self):
        return self.__geo_x, self.__geo_y


def export2csv(points):
    plist = []


def generate_pois(img_array):
    points = []
    for x in range(len(img_array)):
        for y in range(len(img_array[x])):
            if(img_array[x][y] >= 80):
                points.append(POI(20220304, x, y, "泰山", img_array[x][y], "站"))
    return(points)


if __name__ == "__main__":
    img_array = rasterio.open(r'data\cloud_free\NDSI_2021_02_01.tif').read(1)
    points = generate_pois(img_array)
    for p in points:
        print("编码:", p.code, "积雪率:", p.cover_rate)

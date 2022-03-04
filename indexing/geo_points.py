import rasterio
import encoder
import pandas as pd


class POI:
    # let the Hilbert curve to cover the entire image
    __n = 2**18

    def __init__(self, time: int, x: int, y: int, name: str, cover_rate: int, comment: str):
        self.__x = x
        self.__y = y
        self.code = time + encoder.xy2d(self.__n, self.__x, self.__y)
        self.name = name
        self.cover_rate = cover_rate
        self.comment = comment


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
        print("编码:",p.code,"积雪率:",p.cover_rate)

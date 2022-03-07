import csv
import datetime
import random
from turtle import *

import pylab
import rasterio
from numpy import mean
from PIL import Image


class SanJiangYuanAnalyzer:

    def __init__(self):
        begin = datetime.date(2021, 2, 1)
        end = datetime.date(2022, 2, 1)
        file = open(r'data\poi\Sanjiangyuan.csv', 'w', encoding='utf-8-sig', newline='')
        csv_writer = csv.writer(file)
        csv_writer.writerow(["date", "cover_rate"])
        # Traverse and sample daily remote sensing images
        for i in range((end - begin).days):
            day = begin + datetime.timedelta(days=i)
            print(f"对 {day} 日图像采样····· ")
            ds = rasterio.open(f'data\\img\\NDSI_{str(day).replace("-", "_", 2)}.tif')
            img_array = ds.read(1)
            img_slice = img_array[385:682, 291:361]
            csv_writer.writerow([day, mean(img_slice)])
            print(f" {day} 日平均积雪率为:{mean(img_slice)}")


class Sampler:

    def __init__(self, img_array):
        self.img_array = img_array
        self.show_pois()

    def show_pois(self):
        self.image = Image.fromarray(self.img_array, mode='L').convert('RGB')
        print(self.image.size)
        x = []
        y = []
        for row in range(self.image.size[0]):
            for col in range(self.image.size[1]):
                if(self.probability(self.img_array[col][row])):
                    x.append(row)
                    y.append(col)
        pylab.imshow(self.image)
        pylab.plot(x, y, 'r*')
        pylab.show()

    def probability(self, pixel: int):
        p = 0.002*pixel
        if (random.random()*100 <= p):
            return True
        else:
            return False


class HilbertCurver:
    # 步幅
    __l = 15

    def __init__(self, n=8):
        shape('turtle')
        left(90)
        penup()
        goto(-280, 0)
        pendown()
        # 笔刷宽度
        width(3)
        # 曲线的阶数
        self.hilbert_left(n)
        done()
    # hilbert_left means ⬇―→⬆

    def hilbert_left(self, n):
        if n == 0:
            pass
        if n > 0:
            right(90)
            self.hilbert_right(n-1)
            forward(self.__l)
            left(90)
            self.hilbert_left(n-1)
            forward(self.__l)
            self.hilbert_left(n-1)
            left(90)
            forward(self.__l)
            self.hilbert_right(n-1)
            right(90)
    # hilbert_right means ⬆―→⬇

    def hilbert_right(self, n):
        if n == 0:
            pass
        if n > 0:
            left(90)
            self.hilbert_left(n-1)
            forward(self.__l)
            right(90)
            self.hilbert_right(n-1)
            forward(self.__l)
            self.hilbert_right(n-1)
            right(90)
            forward(self.__l)
            self.hilbert_left(n-1)
            left(90)


if __name__ == "__main__":
    # show hilbert curve
    #img = HilbertCurver(8)

    # show pois
    sample = Sampler(rasterio.open(r'data\img\NDSI_2021_02_19.tif').read(1))

    # Statistics on the snow cover rate in the Sanjiangyuan area
    #analyzer = SanJiangYuanAnalyzer()

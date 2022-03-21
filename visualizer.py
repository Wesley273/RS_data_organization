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
        x = [112, 252, 397, 86, 436, 426, 11, 140, 338, 100, 43, 402, 94, 453, 130, 171, 399, 265, 61, 107, 8, 322, 328, 274, 257, 409, 104, 359, 281, 413, 350, 85, 357, 436, 30, 10, 455, 322, 12, 35, 49, 354, 354, 15, 74, 54, 25, 530, 78, 75, 544, 47, 110, 7, 17, 40, 72, 22, 8, 52, 21, 7, 19, 68, 84, 4, 70, 756, 31, 743, 107, 84, 44, 753, 9, 15, 17, 3, 134, 121, 127, 136, 121, 10, 18, 9, 12, 74, 24, 138, 36, 39, 58, 54, 97, 100, 50, 102, 395, 556, 48, 568,
             344, 382, 409, 331, 98, 83, 316, 76, 200, 325, 86, 189, 401, 69, 242, 94, 661, 76, 683, 407, 402, 47, 636, 231, 565, 661, 688, 615, 227, 442, 55, 587, 659, 148, 573, 696, 71, 75, 358, 557, 59, 610, 53, 437, 600, 69, 662, 431, 591, 653, 325, 131, 242, 598, 602, 678, 603, 80, 406, 594, 395, 761, 63, 651, 77, 103, 405, 689, 652, 93, 81, 128, 132, 74, 590, 97, 610, 90, 99, 703, 125, 368, 258, 715, 109, 130, 737, 525, 527, 388, 652, 440, 431, 257, 254, 374]
        y = [0, 0, 0, 3, 3, 4, 6, 6, 6, 7, 8, 8, 10, 10, 11, 11, 11, 12, 13, 13, 14, 14, 15, 16, 17, 17, 18, 18, 22, 22, 26, 27, 30, 30, 32, 33, 35, 37, 39, 42, 44, 44, 46, 52, 53, 55, 59, 60, 61, 70, 70, 72, 73, 74, 74, 74, 76, 80, 84, 84, 85, 92, 92, 94, 95, 96, 100, 100, 102, 103, 106, 108, 112, 112, 122, 124, 127, 134, 134, 135, 135, 141, 144, 145, 149, 150, 150, 150, 153, 153, 155, 160, 160, 162, 169, 169, 171, 172, 172, 174, 175, 175, 176, 179, 181, 182,
             183, 187, 188, 189, 189, 190, 192, 193, 193, 195, 195, 197, 199, 200, 200, 201, 203, 204, 205, 206, 206, 207, 208, 209, 211, 211, 212, 212, 213, 214, 214, 215, 216, 218, 219, 219, 220, 221, 222, 222, 222, 223, 223, 226, 228, 230, 231, 233, 233, 235, 237, 241, 242, 245, 247, 248, 250, 250, 260, 264, 269, 269, 270, 270, 275, 278, 281, 282, 284, 288, 288, 293, 295, 304, 310, 313, 323, 323, 328, 328, 332, 337, 345, 390, 391, 399, 404, 415, 427, 442, 444, 447]
        i = 0
        for row in range(self.image.size[0]):
            for col in range(self.image.size[1]):
                if((row % 34 == 0) & (col % 57 == 0) & (row != 0) & (col != 0)):
                    # if(self.practical_p(self.img_array[col][row])):
                    # x.append(row)
                    # y.append(col)
                    i += 1
        print(i)
        pylab.figure(figsize=(762/100, 569/100), dpi=100)
        pylab.axis('off')
        pylab.imshow(self.image)
        pylab.plot(x, y, 'r*')
        pylab.show()

    def average_p(self, pixel: int):
        p = 0.00024881
        if (random.random() <= p):
            return True
        else:
            return False

    def practical_p(self, pixel: int):
        p = 0.00006*pixel
        if (random.random() <= p):
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
    #img = HilbertCurver(2)

    # show pois
    sample = Sampler(rasterio.open(r'data\img\NDSI_2021_03_01.tif').read(1))

    # Statistics on the snow cover rate in the Sanjiangyuan area
    #analyzer = SanJiangYuanAnalyzer()

    # show difference between hilbert indexing and xOy indexing

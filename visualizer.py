from turtle import *


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
    img = HilbertCurver(8)

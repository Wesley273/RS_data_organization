from turtle import *

shape('turtle')
left(90)
penup()
goto(-280, 0)
pendown()

# hilbert_left means ⬇―→⬆
def hilbert_left(n):
    if n==0:
        pass
    if n>0:
        right(90)
        hilbert_right(n-1)
        forward(l)
        left(90)
        hilbert_left(n-1)
        forward(l)
        hilbert_left(n-1)
        left(90)
        forward(l)
        hilbert_right(n-1)
        right(90)

# hilbert_right means ⬆―→⬇
def hilbert_right(n):
    if n==0:
        pass
    if n>0:
        left(90)
        hilbert_left(n-1)
        forward(l)
        right(90)
        hilbert_right(n-1)
        forward(l)
        hilbert_right(n-1)
        right(90)
        forward(l)
        hilbert_left(n-1)
        left(90)

#笔刷宽度
width(3)
#步幅
l=15
#曲线的阶数
hilbert_left(8)
done()
# convert (x,y) to d
def xy2d(n, x, y):
    rx = ry = d = 0
    s = n//2
    while s > 0:
        rx = (x & s) > 0
        ry = (y & s) > 0
        d += s * s * ((3 * rx) ^ ry)
        x, y = rot(n, x, y, rx, ry)
        s //= 2
    return d


# convert d to (x,y)
def d2xy(n, d):
    rx = ry = t = d
    x = y = 0
    s = 1
    while (s < n):
        rx = 1 & (t//2)
        ry = 1 & (t ^ rx)
        x, y = rot(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y

# rotate/flip a quadrant appropriately


def rot(n, x, y, rx, ry):
    if (ry == 0):
        if (rx == 1):
            x = n - 1 - x
            y = n - 1 - y
        # Swap x and y
        temp = x
        x = y
        y = temp
    return x, y


if __name__ == "__main__":
    # test here
    n = 4
    for y in range(0, n):
        for x in range(0, n):
            if x == n-1:
                print('%3d ' % xy2d(n, x, y))
            else:
                print('%3d ' % xy2d(n, x, y), end='')
    print(d2xy(n, 15))

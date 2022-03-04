
def xy2d(n, x, y):
    """
     convert (x,y) to d
    """
    rx = ry = d = 0
    s = n//2
    while s > 0:
        rx = (x & s) > 0
        ry = (y & s) > 0
        d += s * s * ((3 * rx) ^ ry)
        x, y = rot(n, x, y, rx, ry)
        s //= 2
    return d


def d2xy(n, d):
    """
     convert d to (x,y)
    """
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


def rot(n, x, y, rx, ry):
    """
    rotate/flip a quadrant appropriately
    """
    if (ry == 0):
        if (rx == 1):
            x = n - 1 - x
            y = n - 1 - y
        # Swap x and y
        temp = x
        x = y
        y = temp
    return x, y

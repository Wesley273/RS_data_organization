def uv2d(n, u, v):
    """
     convert (u,v) to d
    """
    ru = rv = d = 0
    s = n//2
    while s > 0:
        ru = (u & s) > 0
        rv = (v & s) > 0
        d += s * s * ((3 * ru) ^ rv)
        u, v = __rot(n, u, v, ru, rv)
        s //= 2
    return d


def d2uv(n, d):
    """
     convert d to (u,v)
    """
    ru = rv = t = d
    u = v = 0
    s = 1
    while (s < n):
        ru = 1 & (t//2)
        rv = 1 & (t ^ ru)
        u, v = __rot(s, u, v, ru, rv)
        u += s * ru
        v += s * rv
        t //= 4
        s *= 2
    return u, v


def __rot(n, u, v, ru, rv):
    """
    rotate/flip a quadrant appropriately
    """
    if (rv == 0):
        if (ru == 1):
            u = n - 1 - u
            v = n - 1 - v
        # Swap u and v
        u, v = v, u
    return u, v

def uv2d(L, u, v):
    """
     convert (u,v) to d
    """
    u0 = v0 = d = 0
    s = L//2
    while s > 0:
        u0 = (u & s) > 0
        v0 = (v & s) > 0
        d += s * s * ((3 * u0) ^ v0)
        u, v = __rot(L, u, v, u0, v0)
        s //= 2
    return d


def d2uv(L, d):
    """
     convert d to (u,v)
    """
    u0 = v0 = t = d
    u = v = 0
    s = 1
    while (s < L):
        u0 = 1 & (t//2)
        v0 = 1 & (t ^ u0)
        u, v = __rot(s, u, v, u0, v0)
        u += s * u0
        v += s * v0
        t //= 4
        s *= 2
    return u, v


def __rot(L, u, v, u0, v0):
    """
    rotate/flip a quadrant appropriately
    """
    if (v0 == 0):
        if (u0 == 1):
            u = L - 1 - u
            v = L - 1 - v
        # Swap u and v
        u, v = v, u
    return u, v

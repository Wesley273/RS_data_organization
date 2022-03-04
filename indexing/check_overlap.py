def checkOverlap(radius: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    a = max(0, x1 - xc, xc - x2) ** 2
    b = max(0, y1 - yc, yc - y2) ** 2
    c = radius ** 2
    return a + b <= c


if __name__ == "__main__":
    print(checkOverlap(1, 1, 1, 1, 1, 1, 1))

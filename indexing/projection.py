from math import radians, cos, sin, asin, sqrt
from pyproj import Transformer


def xy2lonlat(x, y):
    transformer = Transformer.from_crs("epsg:32649", "epsg:4326")
    # Verify the result here: http://epsg.io/
    lat, lon = transformer.transform(x, y)
    return lon, lat


def lonlat2xy(lon, lat):
    transformer = Transformer.from_crs("epsg:4326", "epsg:32649")
    x, y = transformer.transform(lat, lon)
    return x, y


def get_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees into radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine equation
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # the average radius of the Earth
    r = 6371.393
    return c * r * 1000


if __name__ == "__main__":
    print(get_distance(110, 40, 120, 43))
    print(xy2lonlat(-3043700.0, 5187700.0))
    print(lonlat2xy(70.52826039493459, 39.020410447061074))

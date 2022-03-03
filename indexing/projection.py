from math import asin, cos, radians, sin, sqrt

from geopy.distance import geodesic
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


def precise_distance(lon1, lat1, lon2, lat2):

    return geodesic((lat1, lon1), (lat2, lon2)).m


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
    # some tests
    print(xy2lonlat(-3014000.0, 5158000.0))
    print(xy2lonlat(-3010000.0, 5158000.0))
    lon1, lat1 = xy2lonlat(-8000.0, 5158000.0)
    lon2, lat2 = xy2lonlat(-4000.0, 5158000.0)
    print("Use equation: ",get_distance(lon1, lat1, lon2, lat2))
    print("Use geopy: ",precise_distance(lon1, lat1, lon2, lat2))

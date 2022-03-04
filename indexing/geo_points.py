from indexing import encoder, projection


class POI:
    __n = 2**18  # let the Hilbert curve to cover the entire image
    __left_bound = -3044000
    __top_bound = 5188000
    __cell = 4000

    def __init__(self, time: int, row: int, col: int, name: str, cover_rate: int, comment: str):
        self.code = time + encoder.xy2d(self.__n, row, col)
        self.__geo_x = self.__left_bound + row*self.__cell
        self.__geo_y = self.__top_bound - col*self.__cell
        self.lon, self.lat = projection.xy2lonlat(self.__geo_x, self.__geo_y)
        self.name = name
        self.cover_rate = cover_rate
        self.comment = comment

    def get_geoxy(self):
        return self.__geo_x, self.__geo_y


def export2csv(points):
    plist = []


def generate_pois(img_array):
    points = []
    for x in range(len(img_array)):
        for y in range(len(img_array[x])):
            if(img_array[x][y] >= 80):
                points.append(POI(20220304, x, y, "泰山", img_array[x][y], "站"))
    return(points)

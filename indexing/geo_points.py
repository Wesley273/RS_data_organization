import datetime

from indexing import encoder, projection


class POI:
    __n = 2**18  # let the Hilbert curve to cover the entire image
    __left_bound = -3044000
    __top_bound = 5188000
    __cell = 4000
    __begin_day = datetime.date(2021, 1, 31)

    def __init__(self, date: int, row: int, col: int, name: str, cover_rate: int, comment: str):
        self.date = self.get_date(date)
        self.delta_date = (self.date-self.__begin_day).days
        self.code = str(self.delta_date) + 'A'+str(encoder.xy2d(self.__n, row, col))
        self.__geo_x = self.__left_bound + row*self.__cell
        self.__geo_y = self.__top_bound - col*self.__cell
        self.lon, self.lat = projection.xy2lonlat(self.__geo_x, self.__geo_y)
        self.name = name
        self.cover_rate = cover_rate
        self.comment = comment
        self.__row = row
        self.__col = col

    def get_date(self, date):
        day = date % 100
        month = ((date-day)//100) % 100
        year = (date-day-month*100) // 10000
        return datetime.date(year, month, day)

    def get_rowcol(self):
        return self.__row, self.__col

    def get_rowcol(self, lon, lat):
        geo_x, geo_y = projection.lonlat2xy(lon, lat)
        row = int((geo_x-self.__left_bound)/self.__cell)
        col = -int((geo_y-self.__top_bound)/self.__cell)
        return row, col

    def get_geoxy(self):
        return self.__geo_x, self.__geo_y

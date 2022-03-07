import datetime
import rasterio
import indexing.geo_points


def basic_test(row: int, col: int):
    with rasterio.open(r'data\img\NDSI_2022_01_18.tif') as ds:
        print(f'波段数目:{ds.count}')
        print(f'影像尺寸:{ds.width}×{ds.height}')
        print(f'地理坐标范围:{ds.bounds}')
        print(f'反射变换参数(六参数模型):\n {ds.transform}')
        print(f'投影定义:{ds.crs}')
        # 获取第一个波段数据，跟GDAL一样索引从1开始
        # 直接获得numpy.ndarray类型的二维数组表示，如果read()函数不加参数，则得到所有波段（第一个维度是波段）
        band1 = ds.read(1)
        print(f'第一波段的最大值:{band1.max()}')
        print(f'第一波段的最小值:{band1.min()}')
        print(f'第一波段的平均值:{band1.mean()}')
        # 注意矩阵的第一维为图像的y轴
        # 观察点之间的坐标关系
        x, y = ds.transform*(row, col)
        print(f'行列号({row}, {col})对应的投影坐标是({x}, {y})')
        row += 1
        col = col
        x, y = ds.transform*(row, col)
        print(f'行列号({row}, {col})对应的投影坐标是({x}, {y})')
        row = row
        col += 1
        x, y = ds.transform*(row, col)
        print(f'行列号({row}, {col})对应的投影坐标是({x}, {y})')


if __name__ == "__main__":
    row = 761
    col = 568
    basic_test(row, col)
    poi = indexing.geo_points.POI(20190228, row, col, "name", 90, "comment")
    print(poi.lon, poi.lat)
    print('三江源中心点:', poi.get_rowcol(95.5, 33.5))
    print('三江源最西南点:', poi.get_rowcol(90, 32))
    print('三江源最东北点:', poi.get_rowcol(102, 36))

import rasterio

import indexing.encoder
import indexing.geo_points
import indexing.projection


def test_encoder(u, v):
    n = 2**18
    print(indexing.encoder.uv2d(n, u, v))


def basic_test(row: int, col: int):
    with rasterio.open(r'data\img\NDSI_2021_03_01.tif') as ds:
        print(f'波段数目:{ds.count}')
        print(f'影像尺寸:{ds.width}×{ds.height}')
        print(f'地理坐标范围:{ds.bounds}')
        print(f'仿射变换参数(六参数模型):\n {ds.transform}')
        print(f'投影定义:{ds.crs}')
        # 获取第一个波段数据，跟GDAL一样索引从1开始
        # 直接获得numpy.ndarray类型的二维数组表示，如果read()函数不加参数，则得到所有波段（第一个维度是波段）
        band1 = ds.read(1)
        print(band1.sum())
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
    row = 762
    col = 569
    basic_test(row, col)
    poi = indexing.geo_points.POI(20190228, row, col, "name", 90, "comment")
    print(indexing.projection.get_distance(70.52421,45.66236,70.52421,16.63815))
    print(indexing.encoder.uv2d(1,1,1))

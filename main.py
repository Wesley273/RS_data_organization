import rasterio


def basic_test():
    with rasterio.open(r'data\cloud_free\NDSI_2021_02_01.tif') as ds:
        print('该栅格数据的基本数据集信息(这些信息都是以数据集属性的形式表示的):')
        print(f'数据格式:{ds.driver}')
        print(f'波段数目:{ds.count}')
        print(f'影像宽度:{ds.width}')
        print(f'影像高度:{ds.height}')
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
        row = 7
        col = 7
        x, y = (row, col)*ds.transform
        print(f'行列号({row}, {col})对应的左上角投影坐标是({x}, {y})')
        x, y = ds.xy(row, col)  # 中心点的坐标
        print(f'行列号({row}, {col})对应的中心投影坐标是({x}, {y})')
        row += 1
        col = col
        x, y = (row, col)*ds.transform
        print(f'行列号({row}, {col})对应的左上角投影坐标是({x}, {y})')
        x, y = ds.xy(row, col)  # 中心点的坐标
        print(f'行列号({row}, {col})对应的中心投影坐标是({x}, {y})')
        row = row
        col += 1
        x, y = (row, col)*ds.transform
        print(f'行列号({row}, {col})对应的左上角投影坐标是({x}, {y})')
        x, y = ds.xy(row, col)  # 中心点的坐标
        print(f'行列号({row}, {col})对应的中心投影坐标是({x}, {y})')


if __name__ == "__main__":
    basic_test()

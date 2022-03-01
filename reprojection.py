from pyproj import Transformer

 
# 参数1：WGS84地理坐标系统 对应 4326
# 参数2：坐标系WKID 广州市 WGS_1984_UTM_Zone_49N 对应 32649
transformer = Transformer.from_crs("epsg:32649","epsg:4326") 

x = -3043700.0
y = 5187700.0

lat, lon = transformer.transform(x, y)

# Verify the result here: http://epsg.io/
print("lat:", lat, "lon:", lon)
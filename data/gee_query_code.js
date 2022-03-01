/*
    This code is used to get MODIS products via https://code.earthengine.google.com/
*/

Map.addLayer(table, {}, "Tibetan")// show the mask on google map
Map.centerObject(table, 4)

var mod10a1NDSI = ee.ImageCollection("MODIS/006/MOD10A1")
    .filterBounds(table)// vector-mask needs to be imported
    .filterDate("2021-2-1", "2021-3-1")// March 1 is not included
    .select("NDSI_Snow_Cover");// product you need
print('Collection: ', mod10a1NDSI);
var num = 150;// The maximum number of days allowed to output
var list = mod10a1NDSI.toList(num);
print(list);
var count = list.size().getInfo();
print(count)
for (var i = 0; i < count; i++) {
    // get the single image from list
    var image = ee.Image(list.get(i));
    print(i, image);
    // get the id property as the part of filenames
    var id = image.id();
    print(id);
    // out name
    var name2 = "NDSI_" + id.getInfo();
    print(name2)
    Export.image.toDrive({
        image: image,
        description: 'imageToCOGeoTiffExample',
        fileNamePrefix: name2,
        scale: 4000,//resolution
        maxPixels: 9999999999,
        crs: 'EPSG:32649',
        region: table,
        fileFormat: 'GeoTIFF',
        formatOptions: {
            cloudOptimized: true
        }
    });
}
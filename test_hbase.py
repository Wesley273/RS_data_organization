from unicodedata import name

import happybase
from matplotlib.pyplot import table
from database.my_hbase import MyHBase

if __name__ == "__main__":
    hbase = MyHBase()
    # table=hbase.create_table('test')
    # hbase.delete_table('test')
    data = {
        'cf1:date': '2021-2-1',
        'cf2:name': u'台北利科考站',
        'cf3:lon': '75.418335259978', 'cf4:lat': '29.8874001627856',
        'cf5:row': '0', 'cf6:col': '321',
        'cf7:cover_rate': '55',
        'cf8:comment': u'刘博负责,地址与联系方式: 台湾省晶县南长合肥路y座 545681; lei02@example.net; 18235389126'}
    table = hbase.connection.table('test')
    bat = table.batch(batch_size=10)
    #table.put(row='1A241665', data=data)
    row = table.row('1A241665')
    print(row)

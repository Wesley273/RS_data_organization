
import happybase

# remenber to run'hbase thrift -p 9090 start' in cmd


def open_connection():
    connection = happybase.Connection('localhost', port=9090, autoconnect=False)  # 连接到hbase
    connection.open()
    return connection


if __name__ == "__main__":
    connection = open_connection()
    print(connection.tables())  # 查看hbase现有的所有表名
    table = connection.table('MODIS')

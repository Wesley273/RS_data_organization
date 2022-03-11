import time
import happybase

# remenber to run'hbase thrift -p 9090 start' in cmd and the port can be changed


class MyHBase:

    def __init__(self):
        self.connection = happybase.Connection('localhost', port=9090, autoconnect=False)  # 连接到hbase
        self.__families = {
            'cf1': dict(),  # use defaults
            'cf2': dict(),
            'cf3': dict(),
            'cf4': dict(),
            'cf5': dict(),
            'cf6': dict(),
            'cf7': dict(),
            'cf8': dict(),
        }
        self.connection.open()
        print(self.connection.tables())  # 查看hbase现有的所有表名

    def create_table(self, table_name: str):
        self.connection.create_table(table_name, self.__families)
        return self.connection.table(table_name)

    def delete_table(self, table_name: str):
        self.connection.disable_table(table_name)
        self.connection.delete_table(table_name, disable=False)

    def insert_row(self, index_name: str, rowkey: str, data: dict):
        table = self.connection.table(index_name)
        table.put(row=rowkey, data=data)

    def get_row(self, index_name: str, rowkey: str, decoder: bool):
        table = self.connection.table(index_name)
        row = table.row(rowkey)
        if decoder:
            row_decode = {}
            for key, value in row.items():
                row_decode[key.decode().split(':')[1]] = value.decode()
            return row_decode
        return row

    def delete_row(self, index_name: str, rowkey: str):
        table = self.connection.table(index_name)
        if not table.row(rowkey):
            return False
        else:
            table.delete(rowkey)
            return True

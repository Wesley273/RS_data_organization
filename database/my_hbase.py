import happybase

# remenber to run'hbase thrift -p 9090 start' in cmd and the port can be changed


class MyHBase:

    def __init__(self):
        self.connection = happybase.Connection('localhost', port=9093, autoconnect=False)  # 连接到hbase
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

    def byte_transform(raw):
        return raw.encode('raw_unicode_escape').decode()

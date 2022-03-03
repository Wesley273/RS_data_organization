import happybase
connection = happybase.Connection('localhost', port=9090, autoconnect=False)
connection.open()
# see all tables in hbase
print(connection.tables())
connection.close()
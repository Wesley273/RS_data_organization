from database.my_system import MySystem

if __name__ == "__main__":
    my_system = MySystem()
    print(my_system.get_row(rowkey='1A1684', index_name='test-practical', output=True, full=True))
    my_system.arc_query("2021-03-01", "test-practical", 80, 32, '2500km', output=True, full=True)

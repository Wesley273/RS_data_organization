import random
import time

import numpy as np
from database.my_system import MySystem


def test_arc_query(radius: str, full: bool):
    cost_list = np.zeros(100)
    rand_lon = random.randint(80, 85)
    rand_lat = random.randint(20, 35)
    for i in range(0, 100):
        start = time.time()
        result = my_system.arc_query("2021-03-01", "test-large", rand_lon, rand_lat, radius, full)
        # my_system.print_only_result(result)
        end = time.time()
        total = len(result)
        cost_list[i] = (end-start)*1000
    return total, cost_list.mean()


if __name__ == "__main__":
    my_system = MySystem()
    # print(my_system.get_row(rowkey='1A1684', index_name='test-practical', full=True))
    #print(test_arc_query("50km", False))
    #result=my_system.date_query("2021-03-01", "2021-03-03", "test-practical", full=False)
    #my_system.print_result(result)
    #print(my_system.full_text_query("2021-03-01", "2021-03-01", "test-practical", "name", "沈阳龙", "100%", full=True))

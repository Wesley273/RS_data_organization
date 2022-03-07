from faker import Faker

import generate_pois
from database.my_elastic import MyElastic

test_doc_list = [{
    "code": 1213,
    "name": generate_pois.gen_name(),
    "date": "2020-01-02",
    "cover_rate": 90,
    "location": {"lat": 31.256224, "lon": 121.462311}
}, {
    "code": 2432,
    "date": "2020-01-03",
    "cover_rate": 90,
    "name": generate_pois.gen_name(),
    "location": "POINT (121.460186 31.251281)"
}, {
    "code": 3543,
    "date": "2020-01-04",
    "name": generate_pois.gen_name(),
    "cover_rate": 90,
    "location": "POINT (121.473939 31.253531)"
}, {
    "code": 3244,
    "date": "2020-01-05",
    "name": generate_pois.gen_name(),
    "cover_rate": 90,
    "location": "POINT (121.448215 31.26229)"

}]

if __name__ == "__main__":
    es = MyElastic()
    fake = Faker("zh_CN")
    #print(es.get_info())
    es.create_index('test')
    #es.bulk_index_docs('test', test_doc_list)
    #es.arc_query("test", 100, 32, '2000km')
    #es.full_text_query("test", "name", "合山亮")

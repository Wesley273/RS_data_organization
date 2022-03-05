from database.my_elastic import MyElastic

if __name__ == "__main__":
    es = MyElastic()
    #print(es.get_info())
    #es.create_index('test')
    doc_list = [{
        "_id": 1,
        "building_name": "上海站",
        "location": {"lat": 31.256224, "lon": 121.462311}
    }, {
        "_id": 2,
        "building_name": "上海静安洲际酒店",
        "location": "POINT (121.460186 31.251281)"
    }, {
        "_id": 3,
        "building_name": "交通公园",
        "location": "POINT (121.473939 31.253531)"
    }, {
        "_id": 4,
        "building_name": "万业远景大厦",
        "location": "POINT (121.448215 31.26229)"

    }]
    es.bulk_index_docs('test', doc_list)
    es.arc_query("test", 121.462311, 31.256224, '200m')
    es.full_text_query("test", "building_name", "公园")

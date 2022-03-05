from database.my_elastic import MyElastic

if __name__ == "__main__":
    es = MyElastic()
    print(es.get_info())
    doc_list = [
        {"date": "2017-09-13",
         "source": "慧聪网",
         "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
         "code": 20210101,
         "keyword": "电视",
         "title": "付费 电视 行业面临的转型和挑战"
         },
        {"date": "2017-09-13",
         "source": "中国文明网",
         "code": 20210102,
         "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
         "keyword": "电视",
         "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
         },
        {"date": "2017-09-13",
         "source": "人民电视",
         "code": 20210103,
         "link": "http://tv.people.com.cn/BIG5/n1/2017/0913/c67816-29533981.html",
         "keyword": "电视",
         "title": "中国第21批赴刚果（金）维和部隊启程--人民 电视 --人民网"
         },
        {"date": "2017-09-13",
         "source": "站长之家",
         "code": 20210104,
         "link": "http://www.chinaz.com/news/2017/0913/804263.shtml",
         "keyword": "电视",
         "title": "电视 盒子 哪个牌子好？ 吐血奉献三大选购秘笈"
         }
    ]
    print(es.bulk_index_docs('test-index', doc_list))
    doc1 = {
        "building_name": "上海站",
        "location": {"lat": 31.256224, "lon": 121.462311}
    }
    print(es.index_doc('test', doc1))

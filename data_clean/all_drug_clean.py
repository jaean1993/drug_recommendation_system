import json,re
import pymysql

MYSQL_USER = "root"
MYSQL_PASS = ""
MYSQL_DB_NAME = "drug_system"

def getLastHTMLWord(string):
    first_split = string.split("/")
    second_split = first_split[-1].split(".")
    return second_split[0]

def getCleanJson():
    input_file = "/Users/anjin/work/git_anjin/drug_recommendation_system/scrapy/drug/all_drug.json"
    list = []
    with open(input_file) as p:
        dict = json.load(p)
        for tuple in dict:
            temp = {}
            temp['illness'] = getLastHTMLWord(tuple['illness'])
            if len(tuple['rating']) > 0:
                temp['rating'] = float(tuple['rating'][0].strip())
            else:
                temp['rating'] = 0

            temp['drug'] =getLastHTMLWord(tuple['drug_link'][0])
            if len(tuple['alcohol']) > 0:
                temp['alcohol'] = tuple['alcohol'][0].strip()
            else:
                temp['alcohol'] = ""
            temp["rx_otc"] = tuple['rx_otc'][0].strip()
            temp["popularity"] = int(re.findall('\d+', tuple["popularity"][0])[0])
            temp['csa'] = tuple['csa'][0].strip()
            if len(tuple['pregnancy']) > 0:
                temp['pregnancy'] = tuple['pregnancy'][0].strip()
            else:
                temp['pregnancy'] = ""
            review_num = tuple['review_num'][0].strip()
            if review_num == 'Add':
                temp['review_num'] = 0
            else:
                temp['review_num'] = int(review_num)

            list.append(temp)
    print len(list)
    return list

def insert_to_db(dict):
    db = pymysql.connect("localhost", MYSQL_USER, MYSQL_PASS, "MYSQL_DB_NAME")
    cursor = db.cursor()


    cursor.execute("DROP TABLE IF EXISTS CURE")
    create_table_sql = """CREATE TABLE CURE (
                 CURE_ID INT NOT NULL AUTO_INCREMENT,
                 DRUG_NAME  VARCHAR(255) NOT NULL,
                 ILLNESS_NAME  VARCHAR(255) NOT NULL,
                 RATING INT,
                 ALCOHOL VARCHAR(100),
                 RX_OTC VARCHAR(100),
                 popularity FLOAT,
                 CSA VARCHAR(100),
                 pregnancy VARCHAR(100),
                 review_num INT,
                 PRIMARY KEY (CURE_ID))"""
    cursor.execute(create_table_sql)

    for record in dict:
        insert_sql = "INSERT INTO CURE (DRUG_NAME, ILLNESS_NAME, RATING, ALCOHOL, RX_OTC,popularity,CSA, pregnancy,review_num)VALUES ('"+ record['drug'] + "','" + record['illness'] + "'," + str(record['rating']) + ",'" + record['alcohol'] + "','" + record["rx_otc"] + "'," + str(record["popularity"]) + ",'" + record["csa"] + "','" + record["pregnancy"]+ "'," + str(record['review_num']) + ");"
        print insert_sql
        try:
            cursor.execute(insert_sql)
            db.commit()
        except:
            db.rollback()

    db.close()


if __name__ == '__main__':
    dic = getCleanJson()
    insert_to_db(dic)


    #{"rating": [], "illness": "https://www.drugs.com/condition/bursitis.html", "drug_link": ["/naprosyn.html"], "alcohol": ["X"], "rx_otc": ["Rx/OTC"], "popularity": ["width:25%;"], "csa": ["\n    N  "], "pregnancy": ["\n          C        "], "review_num": ["\n                    Add", "\n        "]},

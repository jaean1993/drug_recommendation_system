import json,re
import pymysql

MYSQL_USER = "root"
MYSQL_PASS = ""
MYSQL_DB_NAME = "drug_system"

def getCleanDetails():
    input_file = "/Users/anjin/work/git_anjin/drug_recommendation_system/scrapy/drug/drug_details.json"
    list = []
    with open(input_file) as p:
        dict = json.load(p)
        drug_set = set()
        for tuple in dict:
            temp = {}
            if len(tuple['drug_name']) == 0 or tuple['drug_name'][0].lower() in drug_set:
                continue
            drug_set.add(tuple['drug_name'][0].lower())
            temp["drug_name"] = tuple['drug_name'][0].lower()
            if len(tuple['detailsOne']) == 0 and len(tuple['detailsTwo']) == 0:
                temp["details"] = "Sorry, there is no more details."
            else:
                temp["details"] = ' '.join(tuple['detailsOne']) + "." + ' '.join(tuple['detailsTwo'])
                temp["details"] = temp["details"].replace("'","")
                temp["details"] = temp["details"].replace("\"", "")
            list.append(temp)
    return list
def insert_to_db(dic):
    db = pymysql.connect("localhost", MYSQL_USER, MYSQL_PASS, MYSQL_DB_NAME)
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS DRUGDETAILS")
    create_table_sql = """CREATE TABLE DRUGDETAILS (
                     DRUG_ID INT NOT NULL AUTO_INCREMENT,
                     DRUG_NAME  VARCHAR(255) NOT NULL,
                     DRUG_DETAILS  TEXT NOT NULL,

                     PRIMARY KEY (DRUG_ID))"""
    cursor.execute(create_table_sql)

    for record in dic:
        insert_sql = "INSERT INTO DRUGDETAILS (DRUG_NAME, DRUG_DETAILS)VALUES (\""+record['drug_name'] + "\",\"" + record['details'] + "\");"
        print insert_sql
        try:
            cursor.execute(insert_sql)
            db.commit()
        except :
            db.rollback()

    db.close()

if __name__ == '__main__':
    dic = getCleanDetails()
    insert_to_db(dic)
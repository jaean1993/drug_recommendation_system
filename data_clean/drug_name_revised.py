import json
import all_drug_clean

def drugDetailsModify():
    input_file_Two = "/Users/anjin/work/git_anjin/drug_recommendation_system/scrapy/drug/drug_details.json"
    input_file_One= "/Users/anjin/work/git_anjin/drug_recommendation_system/scrapy/drug/all_drug.json"
    output_file = "/Users/anjin/work/git_anjin/drug_recommendation_system/scrapy/drug/drug_details_revised.json"
    with open(input_file_One) as p:
        dictOne = json.load(p)
        with open(input_file_Two) as q:
            dictTwo = json.load(q)
            assert len(dictOne)==len(dictTwo)
            for i in range(0,len(dictOne)):
                drug_name = all_drug_clean.getLastHTMLWord(dictOne[i]['drug_link'][0]).lower()
                dictTwo[i]["drug_name"] = drug_name
            with open(output_file,"a") as o:
                json.dump(dictTwo, o)
if __name__ == '__main__':
    drugDetailsModify()
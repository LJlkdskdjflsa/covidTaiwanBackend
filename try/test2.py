import requests
import json

response = requests.get("https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json")
def printjson(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj,sort_keys=True, indent=4, ensure_ascii=False)
    return text
#printjson(response.json())
print(type(printjson(response.json())))
'''print(response.status_code)
print(response.json())'''
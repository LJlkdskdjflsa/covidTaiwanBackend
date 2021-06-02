from fastapi import FastAPI

import requests
import json

app = FastAPI()


response = requests.get("https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json")
def printjson(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj,sort_keys=True, indent=4, ensure_ascii=False)
    return text
#printjson(response.json())
@app.get("/")
async def root():
    return response.json()
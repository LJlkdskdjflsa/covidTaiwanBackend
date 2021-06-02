import urllib.request
url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'

k = urllib.request.urlopen(url)

print(k.read())
import os
os.system('cls')
import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/p-2")
#-----------------------------------------------------------
import json
import requests
from external_modules.url_error_handling import Url_Error_Handling
#-----------------------------------------------------------
def read_api_data(cityname):
    result_list=[]
    req=requests.get('http://universities.hipolabs.com/search?country=IRAN')
    if req.status_code==200:
        for item in req.json():
            if item['state-province']==cityname.capitalize():
                result_list.append({'state-province':item['state-province'],"name":item["name"],"web_pages":item["web_pages"][0]})
        return result_list
    else:
        raise Url_Error_Handling ('our server is out of order')


for item in read_api_data('tehran'):
    print(item)

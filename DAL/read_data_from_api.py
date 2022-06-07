import os
os.system('cls')
import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/p-2")
#-----------------------------------------------------------
import json
import requests
from external_modules.url_error_handling import Url_Error_Handling
from external_modules.city_error_handling import City_Error_Handling
#-----------------------------------------------------------
def read_api_data(cityname):
    result_list=[]
    req=requests.get('http://universities.hipolabs.com/search?country=IRAN')
    if req.status_code==200:
        for item in req.json():
            if item['state-province']==cityname.capitalize():
                result_list.append({'state-province':item['state-province'],"name":item["name"],"web_pages":item["web_pages"][0]})
            else:
                raise City_Error_Handling('your city is not found')
        return result_list
    else:
        raise Url_Error_Handling ('our server is out of order')

if __name__=='__main__':
    try:
        for item in read_api_data('mashhad'):
            print(item)
    except Url_Error_Handling as error:
            print(error)
    except City_Error_Handling as error:
            print(error)

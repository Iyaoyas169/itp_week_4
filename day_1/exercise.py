# ITP Week 4 Day 1 Exercise

# https://data.messari.io/api/v2/assets

# List of Asset on one sheet
# Metrics on second sheet


import requests
import json
import openpyxl

# wb = openpyxl.load_workbook("C:\\Users\Leo.Lai.COMPUSOFT\OneDrive - Compusoft AS\Documents\GitHub\itp_week_4\day_1\output.xlsx")
# sheet = wb["Sheet1"]

def get_data(url):
    response = requests.get(url)
    # print(response)
    json_result = response.text
    # print(json_result)
    # print(type(json_result))
    clean_data = json.loads(json_result)
    result = clean_data["data"]
    return result

def retreive_symbol(list):
    new_list = []
    for each in list:
        new_list.append(each['symbol'])
    return new_list


asset_list = get_data("https://data.messari.io/api/v1/assets")
# print(asset_list)
symbol_list = retreive_symbol(asset_list)
print(symbol_list)
#write_data(result_1)




#wb.save("/home/dkayzee/vit/intro-python-august-2021/itp_week_4/day_1/output.xlsx")
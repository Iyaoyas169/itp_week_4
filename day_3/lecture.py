# ITP Week 4 Day 3 Lecture

# imports up top
import requests
import json
import openpyxl
import functions

pokemon_list = []

wb = openpyxl.Workbook()
sheet = wb.active

# sequence of commands
functions.make_header(sheet)
functions.populate_pokemon(requests, json, "https://pokeapi.co/api/v2/pokemon/", pokemon_list)
functions.populate_data(requests, json, pokemon_list)
wb.save("/home/dkayzee/vit/intro-python-august-2021/itp_week_4/day_3/output.xlsx")

def populate_pokemon(requests, json, url, pokemon_list):
    response = requests.get(url)
    json_data = json.loads(response.text)
    for each in json_data['results']:
        pokemon_list.append(each)
    if json_data['next'] != None:
        populate_pokemon(json_data['next'])


def make_header(sheet):
    sheet['A1'] = "Name"
    sheet['B1'] = "Abilities"
    # make them bold

def write_rows(sheet, row_num, name, abilities):
    sheet['A' + str(row_num)] = name
    sheet['B' + str(row_num)] = abilities


def retrieve_abilities(requests, json, url):
    abil_resp = requests.get(url)
    abil_json_data = json.loads(abil_resp.text)
    return abil_json_data['abilities']

def populate_data(requests, json, pokemons):
    for (row_num, each_pokemon) in enumerate(pokemons, start=2):
        just_abil_list = retrieve_abilities(requests, json, each_pokemon['url'])
        abil_string = stringify_abilities(just_abil_list)
        write_rows(row_num, each_pokemon['name'], abil_string)


def stringify_abilities(abilities_list):
    result_string = ""
    for ability in abilities_list:
        result_string += ability['ability']['name'] + " "
    return result_string
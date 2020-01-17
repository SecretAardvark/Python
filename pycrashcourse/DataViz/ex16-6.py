import json 
from country_codes import get_country_code
import pygal

filename = 'gdp_json.json'

with open(filename) as f: 
    gdp_data = json.load(f)

for gdp_dict in gdp_data:
    
   
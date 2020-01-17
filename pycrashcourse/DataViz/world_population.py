import json 
from country_codes import get_country_code
import pygal
from pygal.style import LightColorizedStyle as LCS,  RotateStyle as RS

#Opens our popdata json file
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#Creates a dictionary of all counntry population in 2010.
cc_populations, no_code = {}, {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

#Creates three new dictionaries divided by population size
cc_pops_1, cc_pop_2, cc_pop_3 = {}, {}, {},
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

#Prints the length of each dictionary. 
print(len(cc_pops_1), len(cc_pop_2), len(cc_pop_3))

#Styles and adds data to the worldmap
wm_style = RS('#336699',  base_style = LCS)
wm = pygal.maps.world.World(style = wm_style,)
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

#Creates the worldmap svg file. 
wm.render_to_file('world_population.svg')

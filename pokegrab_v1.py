# import api requesting module

import requests

# =============================================================================
# !!!
# requesting names list for each pokedex
# =============================================================================
# This is the one value to be manually modified
# =============================================================================
# Change end of URL for each Pokedex from 1 - 31
# !!!
# =============================================================================

x = requests.get('https://pokeapi.co/api/v2/pokedex/25').json()

# Here is the initial list of Pokemon names from the current Pokedex

names = []

for z in x["pokemon_entries"]:
    names.append(z["pokemon_species"]["name"])
    
# Name of Pokedex requested

DexName = (x["name"].capitalize())

# Now we need a list of URL's for each Pokemon's info

URLlist = [f'https://pokeapi.co/api/v2/pokemon/{i}' for i in names]

# Print Dex Name, right now because idk

print(DexName)

# =============================================================================
# The list. not changing name, sorry
# =============================================================================

List2 = []

# =============================================================================
# The while loop that writes the list that will be turned into a .txt for Excel
# =============================================================================

b = 0

while b < len(names):

# abtest tests for abilities to populate Null entries
    
    abtest = []
    

# appends the Pokemon's name

    List2.append(names[b])
    
# =============================================================================
# requests for Pokemon's specific json
# 
# add elif statements to plug up Pokemon with multiple forms that fuck up the req
#  most are covered but newer gens especially will have more to be added
# =============================================================================


    if names[b] == 'oricorio':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/oricorio-baile').json()
    elif names[b] == 'lycanroc':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/lycanroc-midday').json()
    elif names[b] == 'basculin':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/basculin-red-striped').json()
    elif names[b] == 'wishiwashi':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/wishiwashi-school').json()
    elif names[b] == 'zygarde':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/zygarde-50').json()
    elif names[b] == 'minior':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/minior-red').json()
    elif names[b] == 'mimikyu':
        a = requests.get('https://pokeapi.co/api/v2/pokemon/mimikyu-busted').json()
    else:
        a = requests.get(URLlist[b]).json()

# Adding abilities and populating NULL entries

    for c in a["abilities"]:
        List2.append(c["ability"]["name"])
        abtest.append(c["ability"]["name"])
    if len(abtest) == 3:
        pass
    elif len(abtest) == 2:
        List2.append("NULL")
    elif len(abtest) == 1:
        List2.append("NULL")
        List2.append("NULL")
        
# printing sprites

    List2.append(a["sprites"]["front_default"])
    List2.append(a["sprites"]["front_shiny"])

# tytest, abtest for types

    tytest = []
    
# printing types

    for d in a["types"]:
        List2.append(d["type"]["name"])
        tytest.append(d["type"]["name"])
    if len(tytest) == 2:
        pass
    elif len(tytest) == 1:
        List2.append("NULL")
        
# End Pokemon entry and repeat function

    List2.append("NEWLINE")
    b = b + 1
    
# =============================================================================
#     Finish by writing
# =============================================================================

file = open('Pokedex.txt','w')
file.write(str(List2))
file.close()
import requests
import time
import json
import os

def get_pokemon_data(limit):
    base_url = "https://pokeapi.co/api/v2"
    pokemon_list_url = f"{base_url}/pokemon?limit={limit}"
    
    response = requests.get(pokemon_list_url)
    response.raise_for_status()
    all_pokemon = response.json()["results"]
    
    all_data = []
    
    for p in all_pokemon:
        try:
            details = requests.get(p["url"]).json()
            stats = {stat['stat']['name']: stat['base_stat'] for stat in details['stats']}
            types = [t['type']['name'] for t in details['types']]
            height = details['height']
            weight = details['weight']
            species_url = details['species']['url']
            species_data = requests.get(species_url).json()
            color = species_data['color']['name']
            
            pokemon_data = {
                "name": details['name'],
                "types": types,
                "attack": stats.get("attack"),
                "hp": stats.get("hp"),
                "height": height,
                "weight": weight,
                "color": color
            }
            
            all_data.append(pokemon_data)
            print(f"Got data for {details['name']}")
            
            time.sleep(0.2)
            
        except Exception as e:
            print(f"Error fetching {p['name']}: {e}")
    
    return all_data

filename = "Pokémon_character_stats.json"

if os.path.exists(filename):
    print(f"File '{filename}' already exists. Loading data from file...")
    with open(filename, "r", encoding="utf-8") as f:
        pokemon_data = json.load(f)
    print(f"Loaded {len(pokemon_data)} Pokémon from file.")
else:
    print(f"File '{filename}' not found. Downloading data from API...")
    pokemon_data = get_pokemon_data(1100)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(pokemon_data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(pokemon_data)} Pokémon data to '{filename}'.")

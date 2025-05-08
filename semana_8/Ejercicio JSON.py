import json


with open('pokemon.json', 'r', encoding='utf-8') as file:
    pokemons = json.load(file)


print("\nEnter the new Pokémon's information:")
name = input("Name: ")
type_ = input("Type (e.g., Fire, Water): ")
hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))


new_pokemon = {
    "name": {
        "english": name
    },
    "type": [type_],
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}


pokemons.append(new_pokemon)

with open('pokemon.json', 'w', encoding='utf-8') as file:
    json.dump(pokemons, file, ensure_ascii=False, indent=2)

print(f"\n Pokemon '{name}' was successfully added to 'pokemon.json'")

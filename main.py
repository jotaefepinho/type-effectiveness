import pandas as pd
from enum import Enum
import csv

# Enum for the Pokemon types
class PokemonType(Enum):
    NORMAL = 0
    FIRE = 1
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHTING = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17

def read_effectiveness_csv_to_dataframe(filename):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filename, index_col=0)
    
    # Convert the DataFrame to float, replacing empty strings with 1.0 (neutral effectiveness)
    df = df.apply(pd.to_numeric, errors='coerce').fillna(1.0)
    
    return df

def get_pokemon_type_input(prompt):
    while True:
        try:
            user_input = input(prompt).strip().upper()
            return PokemonType[user_input]
        except KeyError:
            print("Invalid type. Please enter a valid Pokemon type (e.g., FIRE, WATER, GRASS).")

def effectiveness(effectiveness_df):
    # Get user input for attacking and defending types
    attacking_type = get_pokemon_type_input("Enter the attacking type: ")
    defending_type = get_pokemon_type_input("Enter the defending type: ")

    # Get effectiveness from DataFrame
    effectiveness = effectiveness_df.loc[attacking_type.name.capitalize(), defending_type.name.capitalize()]
    print(f"Effectiveness of {attacking_type.name} attacking {defending_type.name}: {effectiveness}")

def dual_effectiveness(effectiveness_df):
    # Get user input for attacking and defending types
    attacking_type = get_pokemon_type_input("Enter the attacking type: ")
    defending_type_one = get_pokemon_type_input("Enter the first defending type: ")
    defending_type_two = get_pokemon_type_input("Enter the second defending type: ")

    # Calculate combined effectiveness for dual types
    effectiveness = (
        effectiveness_df.loc[attacking_type.name.capitalize(), defending_type_one.name.capitalize()] *
        effectiveness_df.loc[attacking_type.name.capitalize(), defending_type_two.name.capitalize()]
    )
    print(f"Effectiveness of {attacking_type.name} attacking {defending_type_one.name}-{defending_type_two.name}: {effectiveness}")

def read_type_csv_to_dictionary(filename):
    pokedex_types = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pokemon = row[0].lower()
            types = row[1] if row[2] == '' else [row[1], row[2]]
            pokedex_types[pokemon] = types

    return pokedex_types

def get_weaknesses(types):
    return 0
def main():
    effectiveness_file = "./typing_chart.csv"
    effectiveness_df = read_effectiveness_csv_to_dataframe(effectiveness_file)

    pokedex_file = "./pokemon_data.csv"
    pokedex = read_type_csv_to_dictionary(pokedex_file)

    pokemon = input("Type a Pokémon name:\n").strip().lower()

    if pokemon in pokedex:
        pokemon_types = pokedex[pokemon.lower()]
        print(f"{pokemon.capitalize()} is of type(s): {pokemon_types}")
        line = effectiveness_df[pokemon_types[0]].mul(effectiveness_df[pokemon_types[1]])
        print([i for i in line.keys() if line[i] == max(line)])
    else:
        print(f"{pokemon.capitalize()} not found in the Pokémon data.")

if __name__ == "__main__":
    main()

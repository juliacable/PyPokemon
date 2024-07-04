import requests

import tkinter as tk
from tkinter import simpledialog, messagebox

# Type weaknesses dictionary
type_weaknesses = {
    "normal": ["fighting"],
    "fire": ["water", "ground", "rock"],
    "water": ["electric", "grass"],
    "electric": ["ground"],
    "grass": ["fire", "ice", "poison", "flying", "bug"],
    "ice": ["fire", "fighting", "rock", "steel"],
    "fighting": ["flying", "psychic", "fairy"],
    "poison": ["ground", "psychic"],
    "ground": ["water", "grass", "ice"],
    "flying": ["electric", "ice", "rock"],
    "psychic": ["bug", "ghost", "dark"],
    "bug": ["fire", "flying", "rock"],
    "rock": ["water", "grass", "fighting", "ground", "steel"],
    "ghost": ["ghost", "dark"],
    "dragon": ["ice", "dragon", "fairy"],
    "dark": ["fighting", "bug", "fairy"],
    "steel": ["fire", "fighting", "ground"],
    "fairy": ["poison", "steel"]
}


# Initialize the main window (root)
root = tk.Tk()
root.configure(bg="red")
root.withdraw()  # Hide the main window

# Define the base URL for the PokeAPI
base_url = 'https://pokeapi.co/api/v2/'
# Function to get Pokemon data
def call_pokeapi(pokemon_name):
    # Construct the full URL for the request
    url = f"{base_url}pokemon/{pokemon_name.lower()}"
    
    # Send the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        pokemon_data = response.json()
        return pokemon_data
    else:
        return None
# End of API interaction


# Prompt the user for input
pokemon_name = simpledialog.askstring("Input", "Enter a pokemon name:") 
# Display a message box with the input
if pokemon_name:
    data = call_pokeapi(pokemon_name)

    if data:
        arr_types = data['types']
        print(arr_types)

        type_names = [arr_types["type"]["name"] for arr_types in data["types"]]

        if len(type_names) == 1:
            weaks = ""
            typestring = type_names[0]
            wDict = type_weaknesses[type_names[0]]
            for w in wDict:
                weaks += w + "  "

        else:
            weaks = ""
            typestring = type_names[0] + ", " + type_names[1]
            wDict = type_weaknesses[type_names[0]]
            for w in wDict:
                weaks += w + "  "
            wDict2 = type_weaknesses[type_names[1]]
            for w in wDict2:
                weaks += w + "  "
        
        s = "" + "Name: " + data['name'] + "\nType: " + typestring + "\nWeaknesses: " + weaks
        messagebox.showinfo("Results", s)
    else:
        messagebox.showinfo("Results", f"Pokemon not found!")



# Optional: Destroy the root window after use
root.destroy()
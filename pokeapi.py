import requests
import tkinter as tk

# Define the base URL for the PokeAPI
base_url = 'https://pokeapi.co/api/v2/'

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


def custom_input_output_box(title, message, bg_color, width, height):
    def on_submit():
        user_input = entry.get()
        s = print_info(user_input)
        output_label.config(text=s)

    # Set and hide root
    root = tk.Tk()
    root.withdraw()
   
    # Create a new tkinter window
    window = tk.Toplevel()
    window.title(title) 
    
    # Set the window size using numeric values
    window.geometry(f"{width}x{height}")
    
    # Configure the background color of the window
    window.configure(bg=bg_color)
    
    # Create a label widget with the message
    message_label = tk.Label(window, text=message, padx=20, pady=10, bg=bg_color)
    message_label.pack(pady=10)
    
    # Create an entry widget for user input
    entry = tk.Entry(window)
    entry.pack(pady=10)
    
    # Create a submit button
    submit_button = tk.Button(window, text="Submit", command=on_submit)
    submit_button.pack(pady=10)
    
    # Create a label widget to display output
    output_label = tk.Label(window, text="", padx=20, pady=10, bg=bg_color)
    output_label.pack(pady=10)
    
    # Center the window on the screen
    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')
    
    # Run the window
    window.mainloop()


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


# Display a message box with the input
def print_info(pokemon_name):
    if pokemon_name:
        data = call_pokeapi(pokemon_name)

    if data:
        arr_types = data['types']

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
        return s
    else:
        return "Pokemon not found!"


custom_input_output_box("Pokemon Search", "Please enter Pokemon Name:", "lightblue", 400, 400)
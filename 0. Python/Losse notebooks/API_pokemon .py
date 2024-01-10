# Orde van kwaliteit van data
# 1. Database via SQL
# 2. API "Website voor computers" (JSON) 
# 3. CSV bestand (Comma seperated values)
# 4. Scraping (HTML)


# Inladen van de library
import pandas as pd
import requests

# Inladen van de dataset
df = pd.read_csv('Pokemon.csv')


# Zoeken naar een pokemon

#pokemon_naam = input('Naam van de pokemon die je zoekt: ')
#if pokemon_naam in df['Name'].values:
#    print(f"{pokemon_naam} bestaat in de dataset.")
#else:
#    print(f"{pokemon_naam} bestaat niet in de dataset.")

# Berekenen van de gemiddelde aanvalswaarde
#gemiddelde_aanvalswaarde = df['Attack'].mean()

#print(f"De gemiddelde aanvalswaarde van de pokemons is: {gemiddelde_aanvalswaarde}")


#strongest_per_type = pokemon_data.groupby('Type 1')['Total'].idxmax().apply(lambda idx: pokemon_data.loc[idx]['Name']#)
#strongest_per_type = df.groupby('Type 1')['Total'].idxmax().apply(lambda idx: df.loc[idx]['Name'])
#print(strongest_per_type)

# URL van de API
api_url = "https://api.example.com/data"

# Parameters voor de API (indien nodig)
params = {
    "param1": "value1",
    "param2": "value2"
}

# Een GET-verzoek naar de API sturen
response = requests.get(api_url, params=params)

# Controleren of het verzoek succesvol was (status code 200)
if response.status_code == 200:
    # De JSON-gegevens van de API ophalen
    api_data = response.json()
    
    # Verdergaan met de verwerking van de gegevens...
else:
    print("Er is een fout opgetreden bij het raadplegen van de API.")

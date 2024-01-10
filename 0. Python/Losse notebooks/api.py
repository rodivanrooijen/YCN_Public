# Laden van library
import requests

# URL van de API
api_url = "https://randomuser.me/api/"

# Een GET-verzoek naar de API sturen
response = requests.get(api_url)

# Controleren of het verzoek succesvol was (status code 200)
if response.status_code == 200:
    # De JSON-gegevens van de API ophalen
    api_data = response.json()
    #print(api_data)
    titel = api_data['results'][0]['name']['title']
    voornaam = api_data['results'][0]['name']['first']
    achternaam = api_data['results'][0]['name']['last']
    
    print("Titel:", titel)
    print("Voornaam:", voornaam)
    print("Achternaam:", achternaam)


    #Locatie
    stad = api_data['results'][0]['location']['city']
    straat = api_data['results'][0]['location']['street']['name']
    land = api_data['results'][0]['location']['country']
    nummer = api_data['results'][0]['location']['street']['number']

    print("Land:", land)
    print("Stad:", stad)
    print("Straat:", straat)
    print("Nummer:", nummer)
    
else:
    print("Er is een fout opgetreden bij het raadplegen van de API.")



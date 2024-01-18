import googlemaps
# 1. WEERGEGEVENS
# 2. 9292 API (OV)
# 3. GOOGLE MAPS API
# 4. SOCIAL MEDIA DATA (SENTIMENT ANALYSIS)
# 5. CONCURENTIE DATA (BOOKING.COM) (SCRAPING) 
# 6. EVENEMENTEN DATA (SCRAPING)
# 7. ESTIMATE CANCELLATION RATE BASED ON OTHER DATA FROM THE INTERNET
# 8. Hotel kansengebieden (dataset gemeente amsterdam)
# 9. Hotels, gasten, overnachtingen, woonland en regio (dataset CBS) // hotels, zakelijke overnachtingen regio (dataset CBS) // hotels, zakelijke overnachtingen, sterklasse (dataset CBS)
# 10. Hotel booking demand (dataset kaggle)


#--------------------------------------------------------------------------------
# 3. GOOGLE MAPS API
#--------------------------------------------------------------------------------

# Import the Google Maps client library
import googlemaps
import folium
import webbrowser

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'x'

# Create a client instance
client = googlemaps.Client(api_key)

# Specify the origin and destination
origin = 'Oudedijk 22, 3612AB, Tienhoven'
destination = 'Schapendrift 29, Zeist'

# Get the directions
directions_result = client.directions(origin, destination)

# Print the distance and travel time
distance = directions_result[0]['legs'][0]['distance']['text']
travel_time = directions_result[0]['legs'][0]['duration']['text']
print(f"Distance: {distance}")
print(f"Travel Time: {travel_time}")

# Extract the route polyline
polyline = directions_result[0]['overview_polyline']['points']

# Create a Google Maps URL with the route polyline
google_maps_url = f'https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=driving&dir_action=navigate&path=enc:{polyline}'

# Open the URL in a web browser
#webbrowser.open(google_maps_url)
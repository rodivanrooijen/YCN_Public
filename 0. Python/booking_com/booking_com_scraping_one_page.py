import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Een vertraging om de anti-scraping maatregelen van Booking.com te omzeilen
time.sleep(5)  # in seconden

# 1. input parameters
city = 'Maastricht'
checkin_date = '2024-01-18'
checkout_date = '2024-01-19'
num_adults = 2
num_children = 0

# 2. URL  Samenstellen
url = f'https://www.booking.com/searchresults.nl.html?ss={city}&ssne={city}&ssne_untouched={city}&label=gen173nr-1BCAEoggI46AdIM1gEaKkBiAEBmAEcuAEXyAEM2AEB6AEBiAIBqAIDuALsqKStBsACAdICJDE1MTQyOTBmLWU3ZTMtNGQ5NS04MDI2LWQ0Yzg3YTEyOGVkOdgCBeACAQ&sid=0ce72b9818a4078dc8ab51375ff64dcc&aid=304142&lang=nl&sb=1&src_elem=sb&src=searchresults&checkin={checkin_date}&checkout={checkout_date}&group_adults={num_adults}&no_rooms=1&group_children={num_children}&sb_travel_purpose=leisure&selected_currency=EUR'
# https://www.booking.com/searchresults.nl.html?ss=Maastricht&ssne=Maastricht&ssne_untouched=Maastricht&label=gen173nr-1BCAEoggI46AdIM1gEaKkBiAEBmAEcuAEXyAEM2AEB6AEBiAIBqAIDuALsqKStBsACAdICJDE1MTQyOTBmLWU3ZTMtNGQ5NS04MDI2LWQ0Yzg3YTEyOGVkOdgCBeACAQ&sid=0ce72b9818a4078dc8ab51375ff64dcc&aid=304142&lang=nl&sb=1&src_elem=sb&src=searchresults&checkin=2024-01-18&checkout=2024-01-19&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&selected_currency=EUR
# 3. headers (anti-scraping maatregelen)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# 4. HTTP GET request naar de Booking.com URL
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
hotels = soup.find_all('div', {'data-testid': 'property-card'})

# Create an empty list to store the hotel data later
hotels_data = []

# 5. Loop over de hotels om de data te extraheren
for hotel in hotels:
    # Extraheer de hotelnaam
    name_element = hotel.find('div', {'data-testid': 'title'})
    name = name_element.text.strip()

    # Extraheer de locatie van het hotel
    location_element = hotel.find('span', {'data-testid': 'address'})
    location = location_element.text.strip()

    # Extraheer de prijs van het hotel
    price_element = hotel.find('span', {'data-testid': 'price-and-discounted-price'})
    price = ''.join(filter(str.isdigit, price_element.text.strip()))
    
    # Extraheer de rating van het hotel
    rating_element = hotel.find('div', {'class': 'a3b8729ab1 d86cee9b25'})
    rating = rating_element.text.strip()

    # Voeg de data toe aan de hotels_data lijst
    hotels_data.append({
        'name': name,
        'location': location,
        'price': price,
        'rating': rating
    })

# Dataframe maken van de hotels_data lijst
hotels = pd.DataFrame(hotels_data)
print(hotels.head(10))
hotels.to_csv(f'C:/Users/rodiv/Desktop/YCN/Git/0. YCN_Public/0. Python/booking_com/hotels_{city}_{checkin_date}_{checkout_date}_{num_adults}_{num_children}.csv',header=True, index=False)
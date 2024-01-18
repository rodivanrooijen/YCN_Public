import pandas as pd
from func_scraping import scrape_booking_data

# Specificeer invoerparameters en het maximale aantal pagina's om te scrapen
stad = 'Maastricht'
checkin_datum = '2024-01-18'
checkout_datum = '2024-01-19'
num_volwassenen = 2
num_kinderen = 0
max_paginas = 2  # Maximaal aantal paginas om te scrapen // Houd rekening met een vertraging van 5 seconden tussen pagina's

# Roep de functie aan om gegevens van meerdere pagina's te scrapen
hotelgegevens = scrape_booking_data(stad, checkin_datum, checkout_datum, num_volwassenen, num_kinderen, max_paginas)

# Sla de gegevens op in een CSV-bestand
#hotelgegevens.to_csv(f'C:/Users/rodiv/Desktop/YCN/Git/0. YCN_Public/0. Python/booking_com/hotels_{stad}_{checkin_datum}_{checkout_datum}_{num_volwassenen}_{num_kinderen}.csv', header=True, index=False)

print(hotelgegevens.head(10))


# Zet de kolommen 'naam' en 'locatie' om naar het type 'string' (object blijft hetzelfde)
hotelgegevens['naam'] = hotelgegevens['naam'].astype(str)
hotelgegevens['locatie'] = hotelgegevens['locatie'].astype(str)

# Zet de kolom 'prijs' om naar het type 'integer' (als het mogelijk is)
hotelgegevens['prijs'] = pd.to_numeric(hotelgegevens['prijs'], errors='coerce').astype(pd.Int64Dtype())

# Zet de kolom 'beoordeling' om naar het type 'float' (als het mogelijk is)
hotelgegevens['beoordeling'] = hotelgegevens['beoordeling'].str.replace(',', '.').astype(float)

# Bekijk de bijgewerkte datatypes van de kolommen
print(hotelgegevens.dtypes)
print(hotelgegevens.head(10))
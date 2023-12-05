from geopy.geocoders import Nominatim
def get_coordinates(station_names):
    geolocator = Nominatim(user_agent="railway_station_locator")
    coordinates = []

    for station_name in station_names:
        location = geolocator.geocode(station_name)
        if location:
            coordinates.append({
                'station_name': station_name,
                'latitude': location.latitude,
                'longitude': location.longitude
            })
        else:
            coordinates.append({
                'station_name': station_name,
                'latitude': None,
                'longitude': None
            })

    return coordinates

import pandas as pd
sf = pd.read_excel('z1.xlsx')
a = sf['Name'].to_list()
l = len(a)
station_names = []
for i in range(l):
    b=a[i]+str(' Railway Station,India')
    station_names.append(b)

cordinates = get_coordinates(station_names)

df = pd.DataFrame(cordinates)
excel_filename = 'z_1.xlsx'
df.to_excel(excel_filename, index=False)
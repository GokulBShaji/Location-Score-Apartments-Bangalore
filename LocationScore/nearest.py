import pandas as pd
from haversine import haversine, Unit

df1 = pd.read_excel('Railway_Station.xlsx')
df2 = pd.read_excel('Hospitals.xlsx')
df3 = pd.read_excel('Location_of_apartments.xlsx')
df1 = df1.dropna()
df2 = df2.dropna()
df3 = df3.dropna()

lat1 = df3['Latitude '].to_list()
lat2 = df1['latitude'].to_list()
lat3 = df2['Latitude'].to_list()
lon1 = df3['Longitude '].to_list()
lon2 = df1['longitude'].to_list()
lon3 = df2['Longitude'].to_list()

l1 = len(lat1)
l2 = len(lat2)
l3 = len(lat3)
y = 0
Nearest_Rail = []
Nearest_Hospital = []
for i in range(l1):
    y+=1
    coord1 = (lat1[i], lon1[i])
    dist = []
    #for j in range(l3):
    for j in range(l2):
        #coord2 = (lat3[j], lon3[j])
        coord2 = (lat2[j], lon2[j])
        distance_in_km = haversine(coord1, coord2, unit=Unit.KILOMETERS)
        dist.append(distance_in_km)
    #Nearest_Hospital.append(max(dist))
    Nearest_Rail.append(max(dist))
    print(max(dist))
    print(y)

#print(Nearest_Hospital)
print(Nearest_Rail)
#df3['Nearest_Hospital']=Nearest_Hospital
df3['Nearest_Rail']=Nearest_Rail
df3.to_excel('Location_of_apartments.xlsx',sheet_name='Sheet1',index=False)
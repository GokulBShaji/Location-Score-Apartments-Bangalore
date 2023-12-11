import pandas as pd
from haversine import haversine

df1 = pd.read_excel('Location_of_apartments.xlsx')
df2 = pd.read_excel('Railway_Station.xlsx')
#df2 = pd.read_excel('hospital_karnataka.xlsx')

n1 = df1['Latitude '].to_list()
n2 = df1['Longitude '].to_list()

n3 = df2['latitude'].to_list()
n4 = df2['longitude'].to_list()
#n3 = df2['Latitude'].to_list()
#n4 = df2['Longitude'].to_list()

d = []
results = []
k = 0

def min_haversine_distance(target_point, point_set):
    min_distance = 2000.000 # randam float value
    for point in point_set:
        distance = haversine(target_point, point)
        if distance < min_distance:
            min_distance = distance
    return min_distance

l1 = len(n1)
l2 = len(n3)

for i1 in range(l2):
    b = (n3[i1],n4[i1])
    d.append(b)

for i2 in range(l1):
    k+=1
    a =(n1[i2],n2[i2])
    c =min_haversine_distance(a,d)
    results.append(c)
    print(c)
    print(k)

df1['Nearest_Rail'] = results
#df1['Nearest_Hospital']=results
df1.to_excel('Location_of_apartments.xlsx',sheet_name='Sheet1',index=False)

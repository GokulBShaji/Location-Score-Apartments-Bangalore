import pandas as pd


df = pd.read_excel('Location_of_apartments.xlsx')

a = df['Nearest_Rail'].to_list()
b = df['Nearest_Hospital'].to_list()
l = len(a)

Location_Score = []

for i in range(l):
    loc_score = 1000 * ((1/(a[i])) + (2/(b[i])) )
    Location_Score.append(loc_score)

print(Location_Score)
print(len(Location_Score))
df['Location_Score'] = Location_Score

df.to_excel('Location_of_apartments.xlsx',sheet_name='Sheet1',index=False)
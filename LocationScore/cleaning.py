import pandas as pd

#df = pd.read_excel('a3.xlsx')
#df = pd.read_excel('b6.xlsx')
#df = pd.read_excel('c2.xlsx')
#df = pd.read_excel('d3.xlsx')
#df = pd.read_excel('e1.xlsx')
#df = pd.read_excel('f1.xlsx')
#df = pd.read_excel('g3.xlsx')
#df = pd.read_excel('h2.xlsx')
#df = pd.read_excel('i1.xlsx')
#df = pd.read_excel('j2.xlsx')
#df = pd.read_excel('k6.xlsx')
#df = pd.read_excel('l2.xlsx')
#df = pd.read_excel('m5.xlsx')
#df = pd.read_excel('n3.xlsx')
#df = pd.read_excel('o1.xlsx')
#df = pd.read_excel('p3.xlsx')
#df = pd.read_excel('q1.xlsx')
#df = pd.read_excel('r2.xlsx')
#df = pd.read_excel('s5.xlsx')
#df = pd.read_excel('t3.xlsx')
#df = pd.read_excel('u1.xlsx')
#df = pd.read_excel('v2.xlsx')
#df = pd.read_excel('w1.xlsx')
#df = pd.read_excel('y1.xlsx')
df = pd.read_excel('z1.xlsx')

df = df.dropna()

#value_to_remove = 'NA'
#df = df[df['Name'] != value_to_remove]

name_list = df['Name'].to_list()

print(name_list)
print(len(name_list))
#df.to_excel('a3.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('b6.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('c2.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('d3.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('e1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('f1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('g3.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('h2.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('i1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('j2.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('k6.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('l2.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('m5.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('n3.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('o1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('p3.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('q1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('r2.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('s5.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('t3.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('u1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('v2.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('w1.xlsx',sheet_name='Sheet1',index=False)
#df.to_excel('y1.xlsx',sheet_name='Sheet1',index=False)
df.to_excel('z1.xlsx',sheet_name='Sheet1',index=False)
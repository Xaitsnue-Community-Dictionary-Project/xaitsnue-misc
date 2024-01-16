import numpy as np
import pandas as pd

a = pd.read_csv('Moshinsky1.csv')
print(a)

a.fillna('N/A', inplace=True)
print(a)

print(a.loc[[2, 3]])
print(a.loc[:, 'English'])
b = a.where(a.loc[:, 'English'].str.contains('head') == True).dropna()
print(b)
b.to_csv('Moshinskyheadresults.csv')

c = a.where(a.loc[:, 'English'].str.contains('nose') == True).dropna()
print(c)
c.to_csv('Moshinskynoseresults.csv')

d = pd.read_csv('Moshinsky1.csv')
d.fillna(' ', inplace=True) # this changes d itself, if you leave out the inplace, then it is a new df
print(d)
import pandas as pd 
series2 = pd.Series([10,20,30,40,50],index = ['a','b','c','d','e'])
print(series2['d'])
print(series2[['a','c','e']])

import pandas as pd 
student ={'Unit Test-1':[5,6,8,3,10], 'Unit Test-2' : [7,8,9,6,15]}
student1 ={'Unit Test-1':[3,3,6,6,8], 'Unit Test-2' : [5,9,8,10,5]}
ds =pd.DataFrame(student)
ds1 =pd.DataFrame(student1)
print(ds)
print(ds1)
print("subtraction")
print(ds.sub(ds1))   
print("rsub")
print(ds.sub(ds1))
print("addition")
print(ds.radd(ds1)) 
print("radd")
print(ds.radd(ds1)) 
print("multiplication")
print(ds.mul(ds1))
print("division")
print(ds.div(ds1)) 

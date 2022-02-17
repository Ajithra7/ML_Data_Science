import numpy as np
# Create a rank 1 array
a = np.array([1, 2, 3])   
# Prints "<class 'numpy.ndarray'>"
print("type: %s" %type(a))    
# Prints "(3,)"
print("shape: %s" %a.shape)   
# Prints "1 2 3"
print(a[0], a[1], a[2])   
# Change an element of the array
a[0] = 5    
# Prints "[5, 2, 3]"
print(a)                  
# Create a rank 2 array
b = np.array([[1,2,3],[4,5,6]])   
# Prints "(2, 3)"
print("\n shape of b:",b.shape)    
# Prints "1 2 4"
print(b[0, 0], b[0, 1], b[1, 0])   
# Create an array of all zeros
a = np.zeros((2,2))  
# Prints "[[ 0.  0.]
#         [ 0.  0.]]"
print("All zeros matrix:\n  %s" %a)              
                      
# Create an array of all ones
b = np.ones((1,2))    
# Prints "[[ 1.  1.]]"
print("\nAll ones matrix:\n  %s" %b)              
# Create a 2x2 identity matrix
d = np.eye(2)         
# Prints "[[ 1.  0.]
 #         [ 0.  1.]]"
print("\n identity matrix: \n%s"%d)              
                     
# Create an array filled with random values
e = np.random.random((2,2))  
print("\n random matrix: \n%s"%e)
print("Vectorized sum example\n")
x = np.array([[1,2],[3,4]])
print("x:\n %s" %x)
# Compute sum of all elements; prints "10"
print("sum: %s"%np.sum(x))  
 # Compute sum of each column; prints "[4 6]"
print("sum axis = 0: %s" %np.sum(x, axis=0)) 
# Compute sum of each row; prints "[3 7]"
print(" sum axis = 1: %s" %np.sum(x, axis=1))  

#matrix dot product
a = np.arange(10000)
b = np.arange(10000)

dp = np.dot(a,b)

print("Dot product: %s\n" %dp)

#outer product
op = np.outer(a,b)
print("\n Outer product: %s\n" %op)

#elementwise product

ep = np.multiply(a, b)

print("\n Element Wise product: %s \n" %ep)

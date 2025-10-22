import numpy as np

arr1 = np.array(['a','b','c','d','e'])
print("Array:",arr1) #Prints array in format: [val1, val2, ...]

print("index 0: ",arr1[0]) #Prints value in the specified position

arr1[1] = 'x' #Values of the array are mutable (modificables xd)
print("Index 1 modified:",arr1)

print("Sliced array",arr1[2:],"\n") #Slice notation can be used too

# Asign an array slice to another array results in a view
arr2 = arr1[1:3]
print("Array2:",arr2)
arr1[1:3] = ['h','w']
print("Modified array:",arr1)
print("Array2:",arr2,"\n")
# A view is pointer to the original array value, if the original array changes, the view changes. This helps to improve perfomance and memory use

# Advanced indexing create a copy of the array
arr3 = arr1[[1,2]] # Double bracket, to enter in the array dimension
print("Array3:",arr3)
arr1[1:3] = [1,2]
print("Modified array:",arr1)
print("Array2:",arr2)
print("Array3:",arr3,"\n")

# N-array can be created
arrN = np.array([[1,2,3],['a','b','c'],[1.1,2.2,3.3]])
print("ArrayN:",arrN)
print("Value in row 2, column 2: ",arrN[1,1],"\n")

# ARRAY ATRIBUTES
print("--------------------------")
# array.ndim: Returns the number of dimension the array has
print("Dimensions ArrayN: ",arrN.ndim)
# array.shape: Returns the number of elements in every array dimension
print("Elements in ArrayN: ",arrN.shape) # (no_dimensions , no_of_elements_in_dimensions)
# array.size: Returns the total number of elements in all dimensions
print("Total elements in ArrayN:",arrN.size)
# array.dtype: Returns the type of the elements in the array (Normally, all elements in the array are the same)
print("Type of elements in Array1: ",arr1.dtype, "\n") # <U1 = Unicode

# CREATE BASIC ARRAY (With default values)
print("--------------------------")
# Array full of zeros
arrZ = np.zeros(3)
print("Zero's array:",arrZ)
# Array full of ones
arrO = np.ones(3)
print("One's array:",arrO)
# Empty array (Takes the last values the memory register, sometimes random)
arrE = np.empty(3)
print("Empty array:", arrE)
# Array in range
arrR = np.arange(10)
print("Ranged array:",arrR)
# Spaced array
arrS = np.arange(0,10,2) #(Start,stop,step_size)
print("Spaced array:",arrS)
# Lineal spaced array
arrL = np.linspace(0,10,num=5) #(start,stop,numbers)
print("Linear spaced array:",arrL)
# The type of the elements in the creation of a basic array can be specified with dtype. The default type is np.float64
#Specific type array
arrDT = np.ones(5,dtype=np.int64)
print("Integer ones array:",arrDT, "\n")

# Arrays can be easly sorted with array.sort. Sort has more tools, like searchsorted or partition
arrA = ([9,5,2,7,6,2])
# arrA = np.sort([9,5,2,7,6,2])... same, but in one line
print("Sorted array:",np.sort(arrA))
# Arrays can be concatenated
arrB = ([0,-1,-2,-3])
print(np.concatenate((arrA,arrB)))

# Arithmetic operations beetwen arrays can be done too! For a specific problem, search a specific solution in documentation
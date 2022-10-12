import numpy as np

#create an Array
a1=np.array([1,4,2,5,3])
print("An Simple Array:\n")
print(a1)
print("\n")

#Create an simple array of type "float 32"
a2=np.array([1.1,2.3,3.6,4.8], dtype="float32")
print("An Simple Array of Float32:\n")
print(a2)
print("\n")

#Create a simple multidimentional array
a3=np.array([range(i,i+3) for i in [2,4,6]])
print("A simple Multidimentional Array:\n")
print(a3)
print("\n")

#Craete a length 10 integer array filled with zeros
a4=np.zeros(10,dtype='int')
print("Length 10 array filled with zeros:\n")
print(a4)
print("\n")

#Create 3*5 floating point array filled woth 1's
a5=np.ones((3,5),dtype='int')
print("An 3*5 Array filled with 1's:\n")
print(a5)
print("\n")

#Create a 3*5 Array filled with 3.14
a6=np.full((3,5),3.14)
print("An Array of 3*5 Filled With '3.14':\n")
print(a6)
print("\n")

#Create an array filled with linear sequence starting at 0 ending at 20 stepping by 2
a8=np.arange(start=0, stop=20, step=2)
print("An Array Filled with integer filled:\n")
print(a8)
print("\n")

#Create an array of five value evenly spaced between 0 to 1
a7=np.linspace(0, 1, 5)
print("An Array of fivre values evenly spaced:\n")
print(a7)
print("\n")

#Create an array of 3*3 evenly spaced 
a9=np.random.random((3,3))
print("An array of 3*3 evenly spaced:/n")
print(a9)
print("\n")

#Create an array of 3*3 evenly spaced betweeen 0 to 1
a10=np.random.normal(0,1,(3,3))
print("An Array of 3*3 evenly spaced between 0 to 1")
print(a10)
print("\n")

#Create an array of 3*3 Array of random integer in the internal [0,10]
a11=np.random.randint(0,10,(3*3))
print("An array of random integer from range 1 to 10:\n")
print(a11)
print("\n")

#Create a 3*3 identity matrix
a12=np.eye(3)
print("3*3 Identity Matrix:\n")
print(a12)
print("\n")

#Create an uninitiaiaized array of the integers
a13=np.empty(3)
print("An 3*3 Empty Array:\n")
print(a13)
print("\n")

#Create single dimentional array, Towo Dimentional Arry and print the array, no of dimension size of each dimension, Total size Of the array

np.random(0)

x1=np.random.randint(0,10,size=6)
x2=np.random.randint(0,10,size=(3,4))
x3=np.random.randint(0,10,size=(3,4,5))

print()

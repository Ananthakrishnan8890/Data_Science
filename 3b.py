import numpy as np
x1=np.random.randint(10,size=6)
print(x1)
#Print the 0th Element In The Array
print(x1[0])

#Print the 4th Element In The Array
print(x1[4])

#Print the last Element In The Array
print(x1[-1])

#Print the second element from the last
print(x1[-1])

#Access Element in mult dimentional Array
x2=np.random.randint(10,size=(3,4))
print(x2)

#Print the Element at 0,0 position
print(x2[0,0])

#Print the element In The 2,0 position
print(x2[2,0])

#Print the element In The 2,-1 position
print(x2[0,-1])

#Modify The Value using index notation
x2[0,0]=12

#Array String
#Create an array wth 0 element starting from 0
x=np.arrange(10)
print(x)

#To print First five Elements
print(x[:5])

#To Print elements after index 5
print(x[5:])

#To Print Elements from 4 to 7
print(x[4:7])

#Print Every other element(one after another)
print(x[::2])

#To Print every ther element starting at index 1
print(x[1::2])

#To Print Element in 



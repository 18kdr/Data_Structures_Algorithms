# There are two types in which we can work with arrays in python

# List in theory
# -> The most common way to use a array is this in python
# -> We can store hetrogenious elements in the list. (Ex: We can store string, int and float in the list unlike the array)
# List in code
listNew = [1,2,3,4,5,6]
print(listNew)

# Array in code

import array as arr

arrNew = arr.array('i',listNew)
print(arrNew[1])




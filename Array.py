"""
Some basic regarding time complexity while performing array operations

Inserting the element at the end -> O(1)
Inserting the element at a pos -> O(n)
Deleting the element at the end -> O(1)
Deleting the element at a pos -> O(n)
Searching for element with index given -> O(1)
Searching for the element throughout -> O(n)
Modifying one element -> O(1)
Modifying all the elements -> O(n)

"""

#List is used for hetrogenous storage whereas array is used for homogenous storage

# List in code
listNew = [1,2,3,4,5,6]

# Insert in list
listNew[0] = 10

#Search in the list

# -- To search an element is in the list or not
if 5 in listNew:
    print("True")
    
# -- To search an element if it is not in the list
if 100 not in listNew:
    print("True")

# -- To search an element with using a for loop
for i in range(0,len(listNew)):
    if i == 5:
        print("Element found")

# -- To search an element while using for loop
k = len(listNew)
while k > 0:
    if k == 6:
        print("found")
    k -= 1 

# Delete in list
del(listNew[-1])

# Modify elements

# -- Modifying one element
listNew[-1] = 100

# -- Modifying multiple element [Sqaure each item]
listSquare = []
for i in listNew:
    listSquare.append(i*i)
    
print(listSquare)

print(listNew)
# Array in code
import array as arr

arrNew = arr.array('i',listNew)
print(arrNew[1])




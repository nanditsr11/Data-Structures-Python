# Set does not support duplicate values


mySet = {1, 2, 3, 4, 5, 1, 2}

mySet3 = {20, "20", 20.0}

print(mySet3)

print(mySet)

#Important : You cannot create an empty set as {}, this is a dictionary.

a = {}
print(type(a))

b = set()  #This is an empty set
print(type(b))

print(len(b))  #Length of empty set is 0


#Set Methods

b.add(1)
b.add(2)
b.add(3)
b.add(4)

print(b)

mySet.add(6)

print(mySet)

# You cannot add a list or dictionary to a set but you can add a tuple.

# b.add([9,8,7])  #This will give an error
b.add((9,8,7))

print(b)

b.remove(4)  #Removed 4 from the set
print(b)
print(len(b))  #Returns length of the set
print(b.pop())  #Removes an arbitrary element from the set and returns the removed element
mySet.clear()  #Clears the set)
print(mySet)

print("\n")

mySet1 = {1,2,3,4,5}
mySet2 = {1,2,3,6,7,8}

SetUnion = mySet1.union(mySet2)

print("Union of Set 1 and 2 - ", SetUnion)

SetIntersection = mySet1.intersection(mySet2)

print("Intersection of set 1 and 2 - ", SetIntersection)




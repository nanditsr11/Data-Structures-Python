Tuple1 = (1, 2, 3, 4, 5, 64, 63, 6, 2, 45, 2)  #Declared witn () and are immutable once defined.

Tuple2 = (543,)   #Tuple with 1 element needs a , at the end else it'll consider the element as an entry and not a tuple element
Tuple3 = ()   # Valid

print(Tuple1)

# Tuple1[2] = 3   # this is invalid as typles are immutable

print("Count the occurance of 2 in the tuple - ", Tuple1.count(2))  #Counts all the occurances of a number
print("Index of 4 in Tuple - ", Tuple1.index(4))  #Returns the 1st index of occurance of 2. 


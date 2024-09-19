List1 = ["Nandit", "Shalu", 2, 56, 4.8]      # Indexing starts at 0
List2 = [1, 2, 5, 76, 85, 85]

print("List 1 -",List1)
print("List 2 -",List2)

print("\n")

List1[2] = 34
print("Adding 34 at index 2", List1)  #Adds 34 at index 2.

List2.sort()
print ('Sorted List - ', List2 )

List2.reverse()
print ('Reversed List - ', List2)

List2.append(45)
print ('Append 45 to List - ', List2)   # this will add 45 to the end of the list

List2.insert(2, 56)
print ('Inserted 56 at 2nd index - ', List2)   #inserted 56 at index 2.

List2.pop(2)
print("Deletes the value at index 2", List2)   #Deletes the value at index 2

List2.remove(85)
print("Removes 85 from the list", List2)  #Removes 85 from the list, but only 1 occurance not multiple

a = sum(List2)
print(a)   #Prints the sum of elements of the list

myDict = {
    "Name" : "Nandit Srivastava",
    "Profession": "Programmer",
    "Marks": [81, 62],
    "AnotherDict": {"Nandit" : "Coder", "Shalu" : "Talent Acquisition"},
    1: 2,
    4: [3,56,4,3]

}

print(myDict) 
# print(myDict["Name"])
# print(myDict['AnotherDict'])
# print(myDict['AnotherDict']['Shalu'])


#Dictionary is mutable as well, we can change any key and its value as well

# myDict["Marks"] = "One Hundered"

# myDict["Marks"] = [23, 54, 34, 100, 123]

myDict["AnotherDict"]["Shalu"] = "BestFriend"

print(myDict)

#Dictionary Mathods

print(myDict.keys())  #Prints the keys in the form of dict_keys (check with type()) class, not list, we can typecast it to list as below

print(list(myDict.keys()))  #Typecasted to list

print(myDict.values()) #Prints the values of the keys

print(myDict.items())  #Returns a tuple (key, value) in the form of dict_item object, kind of list but not list

myDict.update({"Cellphone" : "63*******4"})

print("\n")
print("\n")
print("\n")

#Another way is through defining a new dictionary and passing it to update function

Update_Dict = {

    "Cell Phone" : "63******4",
    "Old Phone": "70*******3"
}

myDict.update(Update_Dict)

print(myDict)

print(myDict.get['Profession'])     # Return the value of the key, 
                                    # this is same as myDict["Profession"] 
                                    # but incase of an error or in-existance of a key .get() returns "None" and not an error 
                                    # whereas [""] will return an error.



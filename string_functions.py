a = "nandit is a Python programmer"
b = input ('Enter what is his qualifications? ')

print(b)

# Slicing

print(a[1:3]) 
print(a[:3])
print(a[1:2:1])
print(a[::2])
print(a[1::3])

# String Functions

print(a.count('c'))
print(a.find('nandit'))
print(a.replace('nandit', 'Shalu'))
print(a.endswith('er'))
print(len('a'))
print(a.capitalize())

# Escape Sequence

Story = "Nandit is a Data Scientist.\n He\t is very good at \\ Python programming.\\"
print(Story)

# \n --> New Line
# \t --> Tab
#  \'--> Apostrophe (')
# \\ --> Single Slash   and many more....


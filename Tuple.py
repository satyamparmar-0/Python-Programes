tup = (1, 4, 56, 35, 54, 34, 43)

# Accessing elements
print(tup[0])  # Output: 1
print(tup[1])  # Output: 4
print(tup[-1])  # Output: 43

# Slicing
print(tup[1:5])  # Output: (4, 56, 35, 54)

# Length
print(len(tup))  # Output: 7

# Count
print(tup.count(4))  # Output: 1

# Index
print(tup.index(56))  # Output: 2

# Membership
print(4 in tup)  # Output: True
print(100 in tup)  # Output: False

# Immutability
# tup[0] = 10  # This will raise a TypeError

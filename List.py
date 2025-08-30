lst = ["Michael", "Jordan", "Basketball", 23]
# This is a list containing mixed data types
print(lst)

# Accessing elements
print(lst[0])  # Output: Michael
print(lst[1])  # Output: Jordan
print(lst[2])  # Output: Basketball
print(lst[3])  # Output: 23

# Modifying elements
lst[3] = 24
print(lst)  # Output: ['Michael', 'Jordan', 'Basketball', 24]

# Deleting elements
del lst[2]
print(lst)  # Output: ['Michael', 'Jordan', 24]

# Clearing the list
lst.clear()
print(lst)  # Output: []

# Reinitializing the list
lst = ["Michael", "Jordan", "Basketball", 23]
print(lst)  # Output: ['Michael', 'Jordan', 'Basketball', 23]

# Adding elements
lst.append("New Player")
print(lst)  # Output: ['Michael', 'Jordan', 'Basketball', 23, 'New Player']

# Inserting elements
lst.insert(1, "Shooting Guard")
print(lst)  # Output: ['Michael', 'Shooting Guard', 'Jordan', 'Basketball', 23, 'New Player']

# Finding elements
print(lst.index("Jordan"))  # Output: 2
print("Basketball" in lst)  # Output: True

# Checking the length of the list
print(len(lst))  # Output: 6

# remove element from the list
lst.remove("New Player")
print(lst)  # Output: ['Michael', 'Shooting Guard', 'Jordan', 'Basketball', 23]

# pop element from the list
popped_element = lst.pop()
print(popped_element)  # Output: 23
print(lst)  # Output: ['Michael', 'Shooting Guard', 'Jordan', 'Basketball']

# reverse the list
lst.reverse()
print(lst)  # Output: ['Basketball', 'Jordan', 'Shooting Guard', 'Michael']

# sort the list
lst.sort()
print(lst)  # Output: ['Basketball', 'Jordan', 'Michael', 'Shooting Guard']

# Custom sorting (by length of strings)
lst.sort(key=len)
print(lst)  # Output: ['23', 'Jordan', 'Michael', 'Basketball', 'Shooting Guard']

# list comprehension
lst = [x for x in lst if isinstance(x, str)]
print(lst)  # Output: ['Jordan', 'Michael', 'Basketball', 'Shooting Guard']

new_lst = [x.upper() for x in lst]
print(new_lst)  # Output: ['JORDAN', 'MICHAEL', 'BASKETBALL', 'SHOOTING GUARD']

squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

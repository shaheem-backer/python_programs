# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 25
my_dict['city'] = 'New York'

# Accessing values using keys
print(my_dict['name'])  # Output: John
print(my_dict['age'])  # Output: 25

# Check if a key exists in the dictionary
if 'name' in my_dict:
    print("Key 'name' exists in the dictionary")

# Update the value of a key
my_dict['age'] = 26

# Iterating over keys
for key in my_dict:
    print(key)  # Output: name, age, city

# Iterating over values
for value in my_dict.values():
    print(value)  # Output: John, 26, New York

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)  # Output: name John, age 26, city New York

# Remove a key-value pair from the dictionary
del my_dict['city']

# Check the length of the dictionary
print(len(my_dict))  # Output: 2

#print(my_dict)

# Clear all the key-value pairs from the dictionary
my_dict.clear()

# Check if the dictionary is empty
if not my_dict:
    print("The dictionary is empty")

#print(my_dict)



#get mothod to retrieve the value associated with a given key

# Create a dictionary
my_dict = {'name': 'John', 'age': 25}

# Access values using get()
name = my_dict.get('name')
print(name)  # Output: John

age = my_dict.get('age')
print(age)  # Output: 25

# Access a non-existing key
city = my_dict.get('city') # if default value is not given to non existent key, None will be displayed
print(city)  # Output: None

# Specify a default value for non-existing keys
city = my_dict.get('city', 'Unknown') #unknown is default value if the key city doesnt exists
print(city)  # Output: Unknown

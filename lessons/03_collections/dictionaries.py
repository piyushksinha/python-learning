#| Type    | Ordered | Mutable | Duplicates  | Use Case                   |
#| ------- | ------- | ------- | ----------- | -------------------------- |          |
#| `dict`  | ✅*      | ✅      | Keys unique | Key → Value mapping        |

# *Dictionaries preserve insertion order in Python 3.7+.


person = {
    "name": "Piyush",
    "age": 30,
    "country": "India",
}

print(person["name"])

print("\n")

print(person.get("name"))

print("\n")

#print(person["sal"])       # error

print("\n")

print(person.get("sal"))    # None

print("\n")

# Update
person["age"] = 31
# Add
person["city"] = "Bengaluru"

print(person) 

# Un-packing
for key, value in person.items():
    print(f"{key} : {value}")


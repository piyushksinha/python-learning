first_name = "Piyush"
last_name = 'Sinha'

print(first_name)
print(last_name)

address = """
123 MG Road
Bangalore
India
"""

print(address)


### Indexing
language = 'Python'

print(language[0])
print(language[1])
print(language[4])
print(language[-1])
# In Python, strings support negative indexing, which counts from the end of the string.

print("\n")

### Slicing
print(language[:2])     # py
print(language[1:4])    # yth
print(language[2:])     # thon
print(language[:-1])    # pytho
print(language[-6:-1])  # pytho
print(language[::-1])   # nohtyP -> You'll use slicing constantly in -ve.


# language[0] = 'J'
# print(language) # not allowed as string is idempotent

print("\n")

sentence = "  Python is Awesome  "

print(sentence.upper())
print(sentence.lower())
print(sentence.strip())
print(sentence.replace("Awesome", "fun"))
print(sentence.startswith("Python"))
print(sentence.endswith("Awesome"))
print(sentence.split())

print("\n")

names = ["Alice", "Bob", "Charlie"]

result = ""

for name in names:
    result += name

print(", ".join(names))

# Beter to use .join and concat with +
print("\n")

names = ["Alice", "Bob", "Charlie"]

print(", ".join(names))
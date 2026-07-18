### Comparison Operators

print(5 == 5)

print(5 != 5)

print(10 > 2)

print(10 >= 10)

print("\n")

### Logical Operators
is_admin = True
is_active = False

print(is_admin and is_active)

print(is_admin or is_active)

print(not is_admin)

print("\n")

### Membership Operator
languages = ["Python", "Java", "Go"]

print("Python" in languages)

print("Rust" in languages)

print("Rust" not in languages)

print("\n")

### None
### In Python, there is no null keyword; instead, 
# the concept of a null value is represented by the built-in singleton object None. 
# It belongs to its own data type, NoneType.
user = None

print(user)

print("\n")

print(bool(""))

print(bool("Hello"))

print(bool(0))

print(bool(10))

print(bool([]))

print(bool([1]))

print(bool(None))

print("\n")

a = [1, 2]

b = [1, 2]

print(a == b)

print("\n")

print(a is b)
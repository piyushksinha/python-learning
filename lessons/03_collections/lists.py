# Type	Ordered     Mutable	    Duplicates	    Use Case
#list	   ✅	      ✅	            ✅	      General-purpose collection

languages = ["Python", "Java", "Go"]

print(languages)        # ['Python', 'Java', 'Go']
print(languages[1])     # Java
print(languages[-2])    # Java

print("\n")

print(languages[:2])    # ['Python', 'Java']
print(languages[1:])    # ['Java', 'Go']
print(languages[::-1])  # ['Go', 'Java', 'Python']

print("\n")

languages.append("Rust")

print(languages)        # ['Python', 'Java', 'Go', 'Rust']

print("\n")

languages.extend(["C", "C++"])

print(languages)        # ['Python', 'Java', 'Go', 'Rust', 'C', 'C++']


print("\n")

languages.append(["Golang"])

print(languages)        # ['Python', 'Java', 'Go', 'Rust', 'C', 'C++', ['Golang']]

print("\n")

languages.insert(1, "JavaScript")

print(languages)        # ['Python', 'JavaScript', 'Java', 'Go', 'Rust', 'C', 'C++', ['Golang']]

print("\n")

languages.remove("Java")

print(languages)        # ['Python', 'JavaScript', 'Go', 'Rust', 'C', 'C++', ['Golang']]

print("\n")

languages.pop()

print(languages)        # ['Python', 'JavaScript', 'Go', 'Rust', 'C', 'C++']

print("\n")

languages.pop(2)

print(languages)        # ['Python', 'JavaScript', 'Rust', 'C', 'C++']

print("\n")

#Sorting

numbers = [5, 1, 8, 2]

numbers.sort()

print(numbers)

print("\n")

numbers.sort(reverse=True)

print(numbers)

print("\n")

numbers = [5, 1, 8, 2]

my_sorted = sorted(numbers)

print(numbers)
print(my_sorted)

print("\n")


#Copying

a = [1, 2, 3]

b = a

b.append(4)

print(a)        # [1, 2, 3, 4]
print(b)        # [1, 2, 3, 4]

print("\n")

a = [1, 2, 3]

b = a.copy()

b.append(4)

print(a)        # [1, 2, 3]
print(b)        # [1, 2, 3, 4]

print("\n")
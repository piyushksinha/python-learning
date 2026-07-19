numbers = []

for i in range(5):
    numbers.append(i)
print(numbers)

print("\n")

# better to use
numbers = []
numbers = [i for i in range(5)]
print(numbers)

print("\n")


evens = [i for i in range(10) if i%2 == 0]
print(evens)

print("\n")

names = ["alice", "bob", "charlie"]
upper = [name.upper() for name in names]
print(upper)

print("\n")
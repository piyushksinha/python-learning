count = 1

while count < 10:
    print (count)
    count += 1

print("\n")

# break
for i in range(10):
    if i == 5:
        break

    print(i)

print("\n")

for i in range(10):
    if i == 5:
        continue

    print(i)
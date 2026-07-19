languages = ["Python", "Go", "Rust"]
for i in range(len(languages)):
    print(i, languages[i])

print("\n")

# Better way
for i, lang in enumerate(languages):
    print(i, lang)

print("\n")

# zip
# extra items are not zipped
names = ["Alice", "Bob", "Charlie"]

scores = [90, 85, 70]

for name, score in zip(names, scores):
    print(name, score)
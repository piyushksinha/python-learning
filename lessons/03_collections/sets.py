#Type	Ordered	    Mutable	    Duplicates	    Use Case
#set	   ❌	      ✅	           ❌	      Unique values

languages = {"Python", "Java", "Python"}

print(languages)        # {'Python', 'Java'}

print("\n")

backend = {"Python", "Java", "Go"}

frontend = {"JavaScript", "TypeScript", "Python"}

print(backend | frontend)   # {'Go', 'Python', 'JavaScript', 'TypeScript', 'Java'}

print("\n")

print(backend & frontend)   # {'Python'}

print("\n")

# - : Return the elements that are in the left set but not in the right set.
print(backend - frontend)   # {'Java', 'Go'}
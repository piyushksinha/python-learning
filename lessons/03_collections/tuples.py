# Type	    Ordered	    Mutable	    Duplicates	    Use Case
# tuple	       ✅	      ❌	           ✅          Fixed data

point = (10, 20)

print(point)

#point[0] = 100     # tuple cannot be modified
#print(point)

print("\n")

x, y = point

# unpacking
print(x)
print(y)

print("\n")
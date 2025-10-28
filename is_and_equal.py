a = [1,2]
b = [1,2]

print(a is b)
print(a==b)

print(id(a)) #1823335538880
print(id(b)) #1823335687360

# is checks if the two variables refer to same but in this two variables are different
# thats why it gives False (1823335538880 equals 1823335687360) -> False


# But == functions checks both the value thats whu it gives True ([1,2] equals [1,2]) -> True

c = 1
d = 1

print(id(c)) #140733775168424
print(id(d)) #140733775168424

print(c is d )
print(c == d)
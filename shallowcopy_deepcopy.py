import copy

# Shallow Copy -> Copies references of nested Objects.

a = [[9,10],[11,2]]
b = copy.copy(a) #shallow copy

b[0] = [1,2] # outer list modified in the shallow copy will not affect both copy of a, b it will modify only on the according space
# b[0][0] = 11 #inner list modifed will affect the both copy of a, b

print(a)
print(b)

# Deep Copy -> Creates a Complete independent Copy.

c = [[1,3],[5,7]]
d = copy.deepcopy(c) # deepcopy

d[0][0] = 6

print(c) 
print(d) 

# in this deepcopy it will completely creates a independent copy by which if we change anything in child copy (d variable)
# it doesnot affect the parent copy (c variable)
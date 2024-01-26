

l1 = [3, 5, [1, 2, 3], 10, (6, 7, 8)]
print('l1: ', l1)
# The easiest way to copy a list(or most built-in mutable types) is with the constructor for the type
# Important note: this is a shallow copy - the outermost container is copied, but the copy is filled with
# references to the same items held by the original container
l2 = list(l1)
print('l2: ', l2)
print('l1==l2: ', l1==l2)
print('l1 is l2: ', l1 is l2)

# Another way to make a shallow copy is with [:] for mutable sequences
l3 = l1[:]
print('l3: ', l3)
print('l3==l1: ', l3==l1)
print('l3 is l1: ', l3 is l1)

print('l2[2].append(5)')
l2[2].append(5)
print('l1: ', l1)
l2[2] += [20, 40]
l3[4] += (10, 20) # IMPORTNAT: this creates a new tuple and rebinds the variable l3[4] here!!!
print('l1: ', l1)
print('l2: ', l2)
print('l3: ', l3)

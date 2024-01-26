"""
Immutability in tuples is only refering to the physical contents of the tuple - the reference it holds. If the
reference is a mutable data structure, the data in it can be changed.
"""

t1 = (1, 2, [10, 20])
t2 = (1, 2, [10, 20])
print('t1: ', t1)
print('t2: ', t2)
print('t1==t2: ', t1==t2)
print('id(t1[-1]): ', id(t1[-1]))
t1[-1].append(100)
print('t1: ', t1)
print('id(t1[-1]): ', id(t1[-1]))
print('t1==t2: ', t1==t2)

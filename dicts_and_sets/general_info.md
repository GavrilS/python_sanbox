### Dicts:
# Overview of common dict methods:
d.clear()
d.__contains__(x)
d.copy()
d.default_factory
d.__delitem__(k) 
d.fromkeys(it, [initial])
d.get(k, [default])
d.__getitem__(k)
d.items() 
d.__iter__() 
d.keys() 
d.__len__() 
d.__missing__(k)
d.move_to_end(k, [last])
d.pop(k, [default])
d.popitem() 
d.__reversed__()
d.setdefault(k, [default]) 
d.__setitem__(k, v)
d.update(m, [**kargs])
d.values()


# Mappings with Flexible Key Lookup:
- collections.defaultdict
- the __missing__ method(if implemented can provide more flexible implementation) on a custom dict class


# Variations of dict:
- collections.OrederedDict
- collections.ChainMap
- collections.Counter
- collections.UserDict


### SETS:
# Set operations:
s.__and__(z)
s.__rand__(z)
s.intersection(it, ...)
s.__iand__(z)
s.intersection_update(it, …)
s.__or__(z)
s.__ror__(z)
s.union(it, …)
s.__ior__(z) 
s.update(it, …)
s.__sub__(z) 
s.__rsub__(z)
s.difference(it, …)
s.__isub__(z)
s.difference_update(it, …)
s.symmetric_difference(it)
s.__xor__(z) 
s.__rxor__(z)
s.symmetric_difference_update(it, …)
s.__ixor__(z)
s.isdisjoint(z)
s.__contains__(e)
s.__le__(z) 
s.issubset(it)
s.__lt__(z)
s.__ge__(z)
s.issuperset(it)
s.__gt__(z)

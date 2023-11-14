l = ['spam', 'spam', 'eggs', 'spam']
l_set = set(l)
print('l_set: ', l_set)
s_list = list(l_set)
print('s_list: ', s_list)

needles = ['abc', 'def', 'abd', 'def']
haystack = ['cba', 'abc', 'def']
found = len(set(needles) & set(haystack))
print('found: ', found)
found_inter = len(set(needles).intersection(haystack))
print('found_inter: ', found_inter)


# Set initialization
s = {1, 2}
print('s: ', s)
pop_oper = s.pop()
print('pop: ', pop_oper)
s.pop()
print('s: ', s)

# frozenset init
fr_set = frozenset(range(10))
print('fr_set: ', fr_set)


# set comprehension
from unicodedata import name
set_compr = {chr(i) for i in range(23, 256) if 'SIGN' in name(chr(i), '')}
print('set_compr: ', set_compr)

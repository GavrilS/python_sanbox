"""
== compares the values of the 2 variables
is compares whether the 2 variables are the same object(whether their identity is the same)
"""

alex = {
    'name': 'ABC',
    'age': 18,
    'profession': 'student'
}

charles = alex

derek = {
    'name': 'ABC',
    'age': 18,
    'profession': 'student'
}

print('alex == charles: ', alex==charles)
print('alex is charles: ', alex is charles)
print('alex == derek: ', alex==derek)
print('charles is derek: ', charles is derek)

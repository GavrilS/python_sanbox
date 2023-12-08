# Closure: a closure is a function with an extended scope that encompasses non global variables referenced 
# in the body of the function but not defined there. In other words a closure is a function that retains the
# the bindings of the free variables that exist when the function is defined, so they can be used later, when
# the function is invoked and the defining scope is no longer available.


## The nonlocal declaration allows us to flag a variable as a free variable even when it is assigned a new value within the function

### Example: ./averager.py & ./averager2.py & .averager3.py

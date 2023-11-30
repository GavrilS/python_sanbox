# The call operator - (), can be applied to other objects beyond user-defined functions. The Python Data Model documentation lists seven callable types:
    - User-defined functions -> created with def statements or lambda expressions.
    - Built-in functions
    - Built-in methods -> like dict.get
    - Methods -> functions defined in the body of a class
    - Classes
    - Class instances -> if a class defines the __call__ method
    - Generator functions -> functions or methods that use the yield keyword; when called they return a generator object

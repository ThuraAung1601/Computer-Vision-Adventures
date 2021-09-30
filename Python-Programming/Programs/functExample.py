def sq(x):
    return x**2

def cube(x):
    return x**3

def print_table(f): #higher order functions
    print(" x  |  f(x) \n")
    for x in range(1,6):
        print(" {}  |  {} ".format(x,f(x)))
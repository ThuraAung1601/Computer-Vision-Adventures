def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def test(n):
    for i in range(n+1):
        print("Fib of ",i,"is ",fib(i))

test(5)
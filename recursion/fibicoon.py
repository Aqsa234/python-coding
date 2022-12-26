def fib_n(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    return fib_n(n-1) + fib_n(n-2)   
n = int(input("enter the number of series"))
print("sum of series", fib_n(n))
for i in range(n):
    print(fib_n(i), end=" ")    

    


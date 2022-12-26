first = 0
second = 1
n = 5
if n == first:
    print('your request series is',first)
else:
    print(first,second, end =" ")
    for x in range(2,n):
        next = first+second
        print(next, end = " ")
        first = second
        second = next  

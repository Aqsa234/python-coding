


# return 1+2+3 ..... (n-1) +n 

def sum_n(n):
    if n == 0:
        return 0  
    left_part = sum_n(n-1)
    return n + left_part
print(sum_n(5))

# for i in range(1,4):
#     fact =  fact*i
# print(fact)    

from numpy import rint

# fact = 1
def fact_n(n):
    if n == 0:
        return 1
    return n * fact_n(n-1)

print(fact_n(3))

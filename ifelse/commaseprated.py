# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and print the numbers that are divisible by 5 in a comma separated sequence.

list = [x for x in input().split(',')]
items = []
for i in list:
    x = int(i, 2)
    if not x%5:
        items.append(i)
print(','.join(items),"hello")

# list=[1010,1001,1100,1001]
# for i in list:
#     if i%5==0:
#         print(i)

list = []
rows = int(3)
column = int(4)
for i in range(rows):
    y=[]
    for j in range(column):
        y.append(i*j)
        # print(y)
    list.append(y)
print(list)
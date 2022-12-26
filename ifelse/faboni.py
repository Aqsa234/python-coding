from tracemalloc import stop


first = 0
second = 1
n = 50

while first<50:
      print(first)
      first,second = second,first+second
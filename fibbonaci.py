import sys

def Fibbonaci(number):
    x , y = 0, 1
    for _ in range(number):
        x, y  = y, x + y
        yield x

for i in Fibbonaci(10):
    print(i)

print(sys.getsizeof(Fibbonaci(10)))

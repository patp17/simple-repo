import sys


parzysteGenerator = (element
                     for element in range(0, 100)
                     if element %2 ==0
)

parzyste = [element
                     for element in range(0, 100)
                     if element %2 ==0
]
print('Generator: ', parzysteGenerator)
print('Lista: ', parzyste)

for item in parzysteGenerator:
    print(item)

print('Wielkość generatora:', sys.getsizeof(parzysteGenerator))
print('Wielkość listy:', sys.getsizeof(parzyste))

def liczbyParzyste():
    for element in range(100):
        if element %2 ==0:
            yield element

a = liczbyParzyste()
print(a)
print(next(a))
print(next(a))

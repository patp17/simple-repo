import random

talia = ['9', '9', '9', '9',
         '10', '10', '10', '10',
         'J', 'J', 'J', 'J',
         'D', 'D', 'D', 'D',
         'K', 'K', 'K', 'K',
         'A', 'A', 'A', 'A'
         ]

print('Przed tasowaniem', talia)
# print('Bez duplikatow', set(talia))
print('5 kart:', random.sample(talia, 5))
random.shuffle(talia)
print('Po tasowaniu', talia)
print('Przed rozdaniem jest kart: ', len(talia))
# print(talia.pop())
# print(talia.pop())
# print(talia.pop())
# print(talia.pop())
# print(talia.pop())
#
# print('Po rozdaniu jest kart: ', len(talia))

gracz1= []
gracz2= []

for i in range(5):
    gracz1.append(talia.pop())
    gracz2.append(talia.pop())

print('karty gracza 1:', gracz1)
print('karty gracza 2:', gracz2)
print('Po rozdaniu jest kart:', len(talia))
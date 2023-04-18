import random

def wylosuj_liczby(ile, zakres):
    szczesliwe_numery = []
    while ile > 0:
        numerek = random.randint(0, zakres)

        if numerek in szczesliwe_numery:
            numerek = random.randint(0, zakres)
        else:
            szczesliwe_numery.append(numerek)
            ile -= 1


    return szczesliwe_numery


print(wylosuj_liczby(6, 49))


def wylosuj_liczby_lepiej(ile, zakres):
    return random.sample(range(zakres + 1), ile)
print(wylosuj_liczby_lepiej(6, 49))
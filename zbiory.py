NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

print('Liczba wszystkich chorych:', len(NFZ))

print('Liczba osob mieszkajacych na Krzykach i  chorujacych w ostatnim roku: ' ,len(chorzy_rok.intersection(krzyki)))
print('Liczba osob mieszkajacych na Centrum i  chorujacych w ostatnim roku: ' ,len(chorzy_rok.intersection(centrum)))

print('Liczba osob mieszkajacych na Krzykach i  chorujacych w ostatnim miesiacu: ' ,len(chorzy_miesiac.intersection(krzyki)))

print('Liczba osob mieszkajace w Centrum i na Krzykach: ' ,len(centrum.intersection(krzyki)))
print('Liczba osob mieszkajace w Centrum i na Krzykach: ' ,len(centrum.union(krzyki)))
print('Liczba osob mieszkajace w Centrum: ' ,len(centrum))
print('Liczba osob mieszkajace na Krzykach: ' ,len(krzyki))

print('Liczba osob mieszkajace w Centrum i na Krzykach: ' ,len(krzyki)+len(centrum))

print('Sprawdzanie danych')
if len(chorzy_miesiac.difference(chorzy_rok))==0:
    print('Jest w porzaku')
else:
    print('Cos sie nie zgadza')

if len(krzyki.intersection(centrum)) !=0:
    wybor=input('Są osoby które mieszkają w dwóch miejscach. Kogo chcesz usunąć? Z Krzyków - K czy z Centum -C')
    duplikaty = krzyki.intersection(centrum)
    if wybor =='K':
        for duplikat in duplikaty:
            krzyki.remove(duplikat)
            print('Usunieto z Krzykow')
    elif wybor =='C':
        for duplikat in duplikaty:
            centrum.remove(duplikat)
            print('Usunieto z Centrum')

NFZ_kobiety= set()
NFZ_mezczyzni = set()

for pacjent in NFZ:
    if pacjent % 2==0:
        NFZ_kobiety.add(pacjent)
    else:
        NFZ_mezczyzni.add(pacjent)
print('Panie :', NFZ_kobiety, 'i panowie: ', NFZ_mezczyzni)
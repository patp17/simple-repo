numerki1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numerki2 = [1, 3, 5, 7, 9]

numerki3 = [2, 4, 6, 8, 10]

def czy_element_parzysty(lista):
    for element in lista:
        if element %2 == 0:
             return  True
    return False

# print(czy_element_parzysty(numerki1))
# print(czy_element_parzysty(numerki2))
# print(czy_element_parzysty(numerki3))

# print(any(numerki1))
# print(any(numerki2))
# print(any(numerki3))

numerki_parzyste = [element % 2 == 0 for element in numerki1]
print(any(numerki_parzyste))
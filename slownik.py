definicje= {}
choice = None
while choice !='0':
    print(
        '''
        0 - zakończ
        1 - dodaj
        2 - znajdz
        3 - usun
        4 - wyswietl
        ''')
    choice = input('Podaj swoj wybor: ')
    print()
    if choice =='0':
        print('Zegnaj. ')
    elif choice =='1':
        klucz= input('Jakie wyrazenie chcesz dodac? ')
        definicja = input('Podaj definicje: ')
        definicje[klucz]=definicja
        print('Ok, wyrazenie zostalo dodane do slownika.')
    elif choice == '2':
        klucz=input('Jakie wyrazenie chcesz znalezc? ')
        if klucz in definicje:
            print(definicje[klucz])
            print('Wyrazenie' , klucz, 'oznacza', definicja)
        else:
            print('Nie ma takiego slowa')
    elif choice == '3':
        klucz=input('Jakie wyrazenie usunac? ')
        if klucz in definicje:
            del definicje[klucz]
            print('Usunieto. ')
        else:
            print('Nie ma takiego slowa')
    elif choice =='4':
        print('Wyyyswietlam slownik', definicje)
    else:
        print('Blad, nierozpoznany wybor')
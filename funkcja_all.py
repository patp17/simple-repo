def spelnia_wymagania(kandydat, skills):
    return all(skill in kandydat['skills'] for skill in skills)

kandydat1 = {
    'name': 'Adam',
    'email' : 'adam@gmail.com',
    'skills': ['Python', 'PHP', 'Java']
    }

kandydat2 = {
    'name': 'Ania',
    'email' : 'ania@gmail.com',
    'skills': ['Python', 'Java']
    }

kandydat3 = {
    'name': 'Bogan',
    'email' : 'bogdan@gmail.com',
    'skills': ['Python', 'PHP', 'C++']
    }
kandydat4 = {
    'name': 'Mieciu',
    'email' : 'mieciu@gmail.com',
    'skills': ['Python', 'C++']
    }

skills = ['Python', 'C++']
kandydaci = []
kandydaci.append(kandydat1)
kandydaci.append(kandydat2)
kandydaci.append(kandydat3)
kandydaci.append(kandydat4)

print(kandydaci)
print(skills)


for kandydat in kandydaci:
    if spelnia_wymagania(kandydat, skills):
        print(kandydat['name'], 'spelnia wymagania')
    else:
        print(kandydat['name'], 'nie spelnia wymagania')

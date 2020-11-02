# SET ------> (tip dannyh kotoriy zapisiyvaet kak je v slovar na kruglymy skopkami)(unikalnost) (neuporyadochnyi, i hranitsa tolko odin znacheie)

# 1) 
# a = set()
# print(type(a))

# 2)
# a = set('string')       (raznye otvety)
# print(a)

# 3)
# a = set([1, 2, 1, 2, 3, 4, 'a', 'a', 'b', 'cd'])        (sotirovka sdelaet)
# print(a)

# 4)
# a = {'a', 'b', 'c'}
# a.add('d')   (tolko dobovlyayet odin element)
# a.update({'f', 'l'}, 'a')        (dobovlyayem skolko my hotim)               
# print(a)

# 5)
# a = {'a', 'b', 'c'}
# a.remove('d')      # udalyayet vyzyvaemyi element
# a.discard('d')         #  udalyayet vyzyvaemyi element, esli net to oshibka ne vyhodit
# 
# a.pop()          #  udalyayet po rondomno
# print(a)

# 6)
# a = {'a', 'b', 'c'}
# length = len(a)                 #  vozvrashaet kolichestvo elementov
# print(lenght)

# 7) 
# a = {'a', 'b', 'c', 'd'}
# print('c' not in a)               #  sdelaet True or False
# if 'd' not in a:
#     a.remove('d')
# print(a)

# 8)
dancing = {'Masha', 'Sasha', 'Nikita', 'Aiperi', 'Syimyk'}
singing = {'Syimyk', 'Masha', 'Adilet' }
guitar = {'Mirbek', 'Syimyk', 'Sasha'}
# print(dancing.issuperset(singing))        # nad munojestvo, ot kudo ono beretsya, budet TRUE or FALSE
# print(dancing.issubset(singing))       # pod munojestvo


# b = dancing.intersection(singing)                 # Peresecheniye odinakovyh dannyh
# print(b)
# b = dancing & singing & guitar
# print(b)

# b = dancing.difference(singing)      ----->            #  Naidet raznye elementy
# b = singing - dancing
# b = dancing - singing - guitar
# print(b)
# print(b)

# b = singing.symmetric_difference(dancing)   ----->       # Ekoonno katyshpagan adam       
# b = dancing ^ singing ^ guitar
# print(b)

# b = dancing.union(singing)      ----->     #  Obedinyaet
# print(b)
# print(dir(dancing))
# b = dancing | singing | guitar
# print(b)
# '-' ----> raznost
# '^' ----> simmetrichnaya raznost
# '&' ----> peresechenie
# '|' ----> obedinenie

# 9)       FROZENSET   -----> NE IZMENYAYET      (MY NE MOJEM DOBAVLYAT METODY, TOLKO DIFFERENCE etc)
# frozen_dancing = frozenset(dancing)
# print(type(frozen_dancing))

b = frozenset(dancing)
print(type(b))















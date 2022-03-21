import termios


text = "foo, bar, baz"
splitted_text = text.split(' ')

print(splitted_text)
print(len(splitted_text))
print(splitted_text[0])
print(splitted_text[1])
print(splitted_text[2])
# print(splitted_text[3]) #erreur
# splitted_text[3] = 123 #erreur

splitted_text.append(123)
print(splitted_text)

# help(splitted_text.append)

# [start:end:step]
# start inclus
# end exclus
result = splitted_text[0:2]
print(result)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# replacement des points par un caractère vide
text = text.replace('.', '')

# supression des virgules (remplacement par un caractère vide)
splitted_text = text.split(',')
text = ''.join(splitted_text)

# supression des points (remplacement par un caractère vide)
splitted_text = text.split('.')
text = ''.join(splitted_text)

splitted_text = text.split(' ')
print(len(splitted_text))

# tous les mots de l'index 10 inclus à l'index 20 exclus
partial_list = splitted_text[10:20]

# print(partial_list)
# print(splitted_text)

# tous les mots de l'index 3 inclus à l'index 7 exclus
partial_list = splitted_text[3:7]

# print(partial_list)
# print(splitted_text)

# tous les mots de l'index 3 inclus à l'index 7 exclus avec un pas de 2
partial_list = splitted_text[3:7:2]

# print(partial_list)
# print(splitted_text)

# ATTENTION ne fonctionne pas dans l'autre sens
# tous les mots de l'index 7 inclus à l'index 3 exclus
# l'index start doit être strictement inférieur à l'index end
partial_list = splitted_text[7:3]

print(partial_list)
print(splitted_text)

start = 7
end = 3
if start > end:
    start, end = end, start

print(start, end)
partial_list = splitted_text[start:end]

partial_list = splitted_text[-7:-3]

partial_list = splitted_text[-7:-3:2]

print(splitted_text)
print(partial_list)

# -------------------------------------------------------------
# exo
# 1. réccupérez dans splitted_text les mots de l'index 35 à 49 inclus
print(splitted_text[35:50])

# 2. affichez le numéro du dernier index
print(len(splitted_text) - 1)

# 3. récupérez 1 mot sur 2 de l'index 0 au dernier index
# ATTENTION utilisez le dernier index calculé dans l'étape 2

last_index = len(splitted_text) - 1

print(splitted_text[0:last_index + 1:2])

# 4. créez trois liste contenant :
# - le premier mot sur trois
# - le deuxième mot sur trois
# - le troisième mot sur trois

# Exemple :
# liste_originale = ['foo', 'bar', 'baz', 'lorem', 'ipsum']
# liste_partielle1 == ['foo', 'lorem']
# liste_partielle2 == ['bar', 'ipsum']
# liste_partielle3 == ['baz']

liste_partielle1 = splitted_text[0:last_index + 1:3]
liste_partielle2 = splitted_text[1:last_index + 1:3]
liste_partielle3 = splitted_text[2:last_index + 1:3]

print(liste_partielle1)
print(liste_partielle2)
print(liste_partielle3)

# copie de tous les éléments
# valeur par défaut :
# - start = 0
# - end = len()
# - step = 1
result = splitted_text[::]

# copie de tous les éléments en ordre inverse
result = splitted_text[::-1]

# copie de tous les éléments à partir de start jusqu'à la fin
start = 3
result = splitted_text[start:]

# copie de tous les éléments du début jusqu'à end
end = 10
result = splitted_text[:end]

# intervertion de valeur dans une liste (version python)
index = 0
splitted_text[index] = 42
splitted_text[index + 1] = 123

splitted_text[index], splitted_text[index + 1] = splitted_text[index + 1], splitted_text[index]

# intervertion de valeur dans une liste (version classique)
splitted_text[index] = 42
splitted_text[index + 1] = 123

tmp = splitted_text[index]
splitted_text[index] = splitted_text[index + 1]
splitted_text[index + 1] = tmp

my_list = []
print(my_list)

# mode pile
my_list.append("foo") # équivalent d'un push()
print(my_list)

my_list.append(123)
print(my_list)

my_list.append(3.14)
print(my_list)

last_element = my_list.pop() # retire le dernier élément de la liste
print(my_list)
print(last_element)

# mode file
my_list = ["toto", "titi", "tata", "tutu"]
client = my_list.pop(0)
print(my_list)
print(client)

# mode liste
del(my_list[0])
print(my_list)

my_list.insert(0, "mémé")
print(my_list)
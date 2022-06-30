import random

# les type de boucle (générale pour tout language):
# - while
# - do while
# - for classique
# - for each

# reproduction d'une boucle for classique avec une boucle while
# condition d'initialisation
counter = 0
# taille de la boucle
limit = 10

# condition de continuation
while counter < limit:
    # action à répéter
    print("for classique:", counter)

    # incrément / décrement
    counter += 1
# ------------------------------------------------------------------------------
# reproduction d'une boucle do while avec une boucle while
# condition d'initialisation
counter = 0
# taille de la boucle
limit = 10

while True:
    # action à répéter
    print("do while:", counter)

    # incrément / décrement
    counter += 1

    # condition de continuation
    if not (counter < limit):
        break
# ------------------------------------------------------------------------------
# for de python
for counter in range(0, 10):
    # action à répéter
    print('for python:', counter)

# for de python
mots = ['foo', 'bar', 'baz']

# méthode non recommandée pour boucler sur tous les éléments de la liste
for i in range(0, len(mots)):
    # action à répéter
    print(f'mot (non reco) {i}:', mots[i])

# méthode recommandée pour boucler sur tous les éléments de la liste
for mot in mots:
    # action à répéter
    print("mot (reco):", mot)

# destructured assigment
for i, mot in enumerate(mots):
    # action à répéter
    print(f"mot (reco) {i}:", mot)

# affichage des nombres de 0 à 10 avec un "pas" de 2
# ------------------------------------------------------------------------------
# exo : affichez les nombres de 100 à 999 inclus avec une boucle for
start = 100
end = 999
for n in range(start, end + 1):
    print(n)

# exo : affichez les nombres de 0 à 20 inclus qui sont multiple de 3 (2 méthodes)
# 1ère méthode
start = 0
end = 20
step = 3
for n in range(start, end + 1, step):
    print(n)
# 2ème méthode
start = 0
end = 20
for n in range(start, end + 1):
    if n % 3 == 0:
        print(n)

# exo : affichez les nombre de 10 à 1 inclus à rebours
start = 10
end = 0
step = -1
for n in range(start, end, step):
    print(n)
# info : la fonction range() prend un troisième paramètre qui indique le "pas" step
# ------------------------------------------------------------------------------
# algo : tirage de 2 nombres différents parmi 5
numbers = []

# 1er tirage
n = random.randint(1, 5)
numbers.append(n)

# 2ème tirage
n = random.randint(1, 5)

while True:
    n = random.randint(1, 5)
    # condition d'arrêt
    if n not in numbers:
        # le nombre n'a pas encore été tiré au hasard
        # on peut sortir de la boucle
        break

numbers.append(n)
print(numbers)
# ------------------------------------------------------------------------------
# algo : tirage de 4 nombres différents parmi 5
numbers = []

# 1er tirage
n = random.randint(1, 5)
numbers.append(n)

# 2ème, 3ème, 4ème tirage
start = 2  # ou 0
end = 4  # ou 3
for i in range(start, end + 1):  # for i in range(start, end) # ou sans varaible mettre 3
    while True:
        n = random.randint(1, 5)
        # condition d'arrêt
        if n not in numbers:
            # le nombre n'a pas encore été tiré au hasard
            # on peut sortir de la boucle
            break
    numbers.append(n)

print(numbers)

# algo : tirage de 4 nombres différents parmi 5 (variante)
numbers = []

# 1er, 2ème, 3ème, 4ème tirage
for i in range(4):
    while True:
        n = random.randint(1, 5)

        # condition d'arrêt
        if n not in numbers:
            # le nombre n'a pas encore été tiré au hasard
            # on peut sortir de la boucle
            break
    numbers.append(n)

print(numbers)
import random

# Exo 1.1
# Affichez le type de donnée des variables a et b.

a = 3.14
b = 3

# Réponse 1.1
print(type(a))
print(type(b))

# Exo 1.2
# En utilisant les variables a et b, affichez les chiffres après la virgule de la variable a.

a = 3.14
b = 3

# Réponse 1.2
print(a - b)

# Exo 1.3
# Affichez le type de données de la variable n.

n = random.randint(10, 99) / 10

# Réponse 1.3
print(type(n))

# Exo 1.4
# Convertissez n en un nombre entier, stockez le résultat dans une variable et affichez le résultat.

n = random.randint(10, 99) / 10

# Réponse 1.4
nbr = int(n)
print(nbr)

# Exo 1.5
# Affichez :
# - les nombres avant la virgule de la variable n
# - les nombres après la virgule de la variable n

n = random.randint(10, 99) / 10

# Réponse 1.5
print(n)

sans_virgule = int(n)
print(sans_virgule)

print(n - sans_virgule)

# Exo 1.6
# Stockez dans une variable si la variable n est "mathématiquement" un nombre entier ou non.

n = random.randint(10, 99) / 10

# Réponse 1.6
print(n)
number = n == int(n)
print("est-ce un entier?", number)


# Exo 2.1
# Affichez le texte "foo", si la variable n est inférieure à 5.

n = random.randint(0, 9)

# Réponse 2.1
if n < 5:
    print("foo")

# Exo 2.2
# Tirez un nombre au hasard compris entre 0 et 9 inclus sans le stocker dans une variable et affichez le texte "foo", si le nombre est inférieure à 5.

# Réponse 2.2
if random.randint(0, 9) < 5:
    print("foo")

# Exo 2.3
# Affichez le texte "foo" tant que vous tirez au hasard un nombre compris entre 0 et 9 inclus plus petit que 5.
# Vous pouvez utilisez random.randint(0, 9) pour tirer le nombre au hasard

# Réponse 2.3

while random.randint(0, 9) < 5 :
    print("foo")

# ou

while True:
    # Avec une condition d'arrêt
    if random.randint(0, 9) < 5:
        print("foo")
    else:
        break

# ou
# Méthode avec tirage avant la boucle
n = random.randint(0, 9)

# Avec une condition de continuation
while n < 5:
    print("foo")
    n = random.randint(0, 9)
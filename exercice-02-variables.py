# exercice-02-variables.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
nbr = 42
print(nbr)

nbr_dor = 1.61
print(nbr_dor)

name = "Bernon nicolas"
print(name)

is_morning = True
print(is_morning)

is_not_morning = False
print(is_not_morning)

get_number = None
print(get_number)
# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez le valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
number = 2
number = float(number)
print(number)
print(type(number))

number_float1 = 1.62
number_float1 = int(number_float1)
print(number_float1)
print(type(number_float1))

number_float2 = 1.62
number_float2 = int(round(number_float2, 0))
print(number_float2)
print(type(number_float2))

number_float3 = 1.62
number_float3 = round(number_float3, 1)
print(number_float3)
print(type(number_float3))
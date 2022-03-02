# + - * / 
result = 123 + 4.14
print(result)

# ()
result = (1 + 2) * 3
print(result)

# // % **
# Division entière
result = 1 // 3
print(result)

# Modulo (reste de la division)
result = 10 % 3
print(result)

# Vérification de la divisibilité
result = 7685923 % 7
print(result)

# Puissance
# Dans certains language c'est : ^, pow()
result = 3 ** 2
print(result)

# Racine carré
result = 3 ** (1 / 2)
print(result)

# Racine cubique
result = 3 ** (1 / 3)
print(result)

# Opérateur booléen "and"
result = True and True # True
result = False and True # False
result = True and False # False
result = False and False # False

# S'il n'y a que de "and", l'ordre n'est pas important
result = True and False and True and False # False

# Opérateur booléen "or"
result = True or True # True
result = False or True # True
result = True or False # True
result = False or False # False

# S'il n'y a que des "or", l'ordre n'est pas important
result = True and False and True and False # True

# Opérateur booléen "xor", le "ou excusif"
result = True ^ True # False
result = False ^ True # True
result = True ^ False # True
result = False ^ False # False

# Opérateurs composés

# N'existe pas en python
# c++ <=> c = c + 1

number = 42
#number = number + 1
n = 1
number += n
# exercice-10-fonctions.py

# exo 10.1
# Créer une fonction nommée `my_sum()` qui :
# - prend deux paramètres
# - additionne ces deux paramètres
# - renvoit le résultat
# Appelez la fonction et affichez le résultat

# réponse 10.1
def my_sum(a, b):
    return a + b

a = 2
b = 3

resultat = my_sum(a, b)
print(resultat)

# exo 10.2
# Créer une fonction nommée `my_diff()` qui :
# - prend deux paramètres de type `int`
# - soustrait `b` de `a`
# - renvoit le résultat de type `int`
# Notez bien le type hinting dans la déclaration de la fonction
# Appelez la fonction et affichez le résultat

# réponse 10.2
def my_diff(a: int, b: int) -> int:
    return a - b

a = 15
b = 7

resultat = my_diff(a, b)
print(resultat)

# exo 10.3
# Créer une fonction nommée `oui_non()` qui :
# - prend un paramètre booléen
# - renvoit `oui` si le booléen est égal à True
# - renvoit `non` si le booléen est égal à False
# Appelez la fonction avec la valeur True et affichez le résultat
# Appelez la fonction avec la valeur False et affichez le résultat

# réponse 10.3
def oui_non(a: bool):
    if a == True:
        return "oui"
    else:
        return "non"

a = 1

resultat = oui_non(a)
print(resultat)

# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit True si `a` est plus grand que `b`
# - renvoit False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
def is_greater(a: float, b: float):
    if a > b:
        return True
    else:
        return False

a = 1.72
b = 1.73

resultat = is_greater(a, b)
print(resultat)
# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoit 1 si `a` est plus grand que `b`
# - renvoit -1 si `a` est plus petit que `b`
# - renvoit 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare(a: float, b: float):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0

a = 1.72
b = 1.71

resultat = compare(a, b)
print(resultat)
# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
def meters_to_miles(meters):
    return meters / 1609.344

def miles_to_meters(miles):
    return miles * 1609.344

reslt_miles = meters_to_miles(1000)
print(str(reslt_miles) + " miles")

resut_meters = miles_to_meters(10)
print(str(resut_meters) + " meters")
# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoit le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7
def compute_tax(price: float, tax_type: int):
    if tax_type == 1:
        return price * (1 + (2 / 100))
    elif tax_type == 2:
        return price * (1 + (5.5 / 100))
    elif tax_type == 3:
        return price * (1 + (10 / 100))
    elif tax_type == 4:
        return price * (1 + (20 / 100))
    else:
        return price

result1 = compute_tax(100, 1)
print(result1)

result2 = compute_tax(100, 2)
print(result2)

result3 = compute_tax(100, 3)
print(result3)

result4 = compute_tax(100, 4)
print(result4)

result5 = compute_tax(100, 5)
print(result5)


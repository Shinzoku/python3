# le score de 5 joueurs
scores = [433, 562, 574, 800, 953]

# données en entrée : une liste int
# données en sorties : un int

def int_average(numers: list) -> int:

    """
    Cette fonction renvoie un arrondi de la moyenne des nombres passés en 
    paramètre.

        numbers :   list | Cette liste contient les nombres (int ou float) dont 
                    il faut calculer la moyenne.

        return :    int | La fonction renvoie une moyenne arrondie au format int.
    """

    # le nombre d'élément
    n = len(scores)

    # initialisation de l'accumulateur
    total = 0

    # existe mais pas pédagogique !
    # total = som(scores)

    for score in scores:
        total += score

    # moyenne = total / nombre d'éléments
    average = total / n

    # arrondi du résultat
    average = round(average)

    return average

average = int_average(scores)
print(average)

# le score de 5 joueurs
scores = [302, 102, 956, 987, 931]

average = int_average(scores)
print(average)

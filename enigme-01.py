# 1. Trois carrés pour le prix d'un

# 49 est un carré à deux chiffres. Si on le découpe en deux nombres
# 4 et 9, on obtient deux carrés à un chiffre. 49 est le seul carré a deux
# chiffres possédant cette particularité.
# Trouver 1'unique carré à quatre chiffres tel que ses deux premiers
# chiffres et ses deux derniers représentent deux carrés à deux chiffres.

# la liste qui contiendra nos réponse
resultat = []

# carré de 2 chiffres : 4 à 9
carres_2_chiffres = []

for i in range(4, 10):
    carres_2_chiffres.append(i ** 2)

# carré de 4 chiffres : 32 à 99
carres_4_chiffres = []

for i in range(32, 100):
    carres_4_chiffres.append(i ** 2)

# construisons des nombre à 4 chiffres
for i in carres_2_chiffres:
    for j in carres_2_chiffres:
        nombre = i * 100 + j

        if nombre in carres_4_chiffres:
            resultat.append(nombre)

print(resultat)

# ------------------------------------------------------------------------------
# ou (code de maxence)

L1 = [n**2 for n in range(4, 9+1)]  # liste des carrés à 2 chiffres
L2 = [n**2 for n in range(32, 99+1)]  # liste des carrés à 4 chiffres


reponse = []

for i in L2:
    i = str(i)
    if int(i[:2]) in L1 and int(i[2:4]) in L1:
        reponse.append(int(i))
print(reponse)

# ------------------------------------------------------------------------------
# ou (code de quentin f)

for i in range(1000, 9999):
    if (int(i**(1/2)) == (i**(1/2))) and (int((i//100)**(1/2))) == ((i//100)**(1/2)) and int((i % 100)**(1/2)) == (i % 100)**(1/2) and i % 100 != 0:
        print(i)

# ------------------------------------------------------------------------------
# ou (code de Donatien)

carreDeuxChiffres = []
i = 1
while i**2 < 100:
    if len(str(i**2)) == 2:
        carreDeuxChiffres.append(str(i**2))
    i += 1

listeCarré = []
for i in carreDeuxChiffres:
    for j in carreDeuxChiffres:
        if (int(i+j)**0.5) == int(int(i+j)**0.5):
            listeCarré.append(int(i+j))

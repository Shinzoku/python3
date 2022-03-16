import random

firstname = 'toto'
lastname = 'pop'
number =  random.randint(2, 10)

email = firstname + '.' + lastname + str(number) + '@exemple.com'
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("Vous n'avez pas de nouveaux mails")
elif new_emails == 1:
    print("Vous avez reçu <strong>1</strong> nouveaux mail")
else:
    print("Vous avez reçu <strong>" + str(new_emails) + "</strong> nouveaux mail")

# ------------------------------------------------------------------------------------------------
stock = random.randint(0, 15)

if stock  == 0:
    print("stock épuisé")
elif stock == 1:
    print("stock en tension : 1 pièce")
elif 1 < stock < 5:
    print(f"stock en tension : {stock} pièces")
elif 5 <= stock < 10:
    print(f"stock en confortable : {stock} pièces")
elif 10 <= stock:
    print(f"stock en surnombre : {stock} pièces")

# ------------------------------------------------------------------------------------------------
temperature = 10.1 + 0.1 + 0.1
print(temperature)

print(f"La température actuelle est de {temperature:.2f}° C") # interpolation de la temperature avec :.2f

# ------------------------------------------------------------------------------------------------
electricite = True

if electricite:
    print('electricite: vrai')
else:
    print('electricite: faux')

# -------------------------------------------------------------------------------------------------
print(f"le nombre dtiré au hazard est : {random.randint(0, 10)}")

# -------------------------------------------------------------------------------------------------
texte = "foo bar baz"

# len == length == longueur
print(len(texte))

print(texte.find("baz"))
print(texte.find("banana"))

print(texte.find("ba"))

# find() -> int
# find() -> int >= 0 si le texte est trouvé
# find() -> int == -1 si le texte n'est pas trouvé

# recherche à partir du caractère 5 inclus
print(texte.find("ba", 5))

# -------------------------------------------------------------------------------------------------
texte = "Bonjour Toto"

# Rédigez un if qui indique si le keyword est présent ou non dans la chaine de caractères
# Affichez "trouvé" si le keyword est présent
# Sinon affichez "non trouvé"

keyword = "Toto"

if texte.find(keyword) >= 0:
    print("trouvé")
else:
    print("non trouvé")

# Rédigez un if qui indique si le keyword est présent ou non dans la chaine de caractères
# Affichez "trouvé" si le keyword est présent
# Sinon affichez "non trouvé"

keyword = "Titi"

if texte.find(keyword) != -1:
    print("trouvé")
else:
    print("non trouvé")

# -------------------------------------------------------------------------------------------------
texte = "bjour  Toto"
texte = texte.replace('bjour', 'Boujour')
texte = texte.replace('  ', ' ')
texte = texte.replace('Toto', 'Titi')
print(texte)
import random

if True:
    print("ce message sera toujours affiché")

if False:
    print("ce message ne sera jamais affiché")

# ---------------------------------------------------------
if True:
    print("ce message sera toujours affiché (if True)")
else:
    print("ce message ne sera jamais affiché (if True)")

if False:
    print("ce message ne sera jamais affiché (if False)")
else:
    print("ce message sera toujours affiché (if False)")

# ----------------------------------------------------------
fruits = ['apples', 'bananas', 'cherries']

if 'apples' in fruits:
    print("Il y a des pommes")
else:
    print("Il n'y a pas de pommes")

if 'orange' in fruits:
    print("Il y a des oranges")
else:
    print("Il n'y a pas d'oranges")

# ----------------------------------------------------------
is_authenticated = True

if is_authenticated:
    print("L'utilisateur peut accéder au backoffice")

# ----------------------------------------------------------
user_password = "123"
user_password_in_db = "abc"

if user_password == user_password_in_db:
    print("L'utilisateur peut accéder aux backoffice")
else:
    print("Le mail ou le mot de passe est incorrect")

# ----------------------------------------------------------
is_authenticated = True
users_in_db =['toto','titi', 'tata', 'tutu']
tutu_password_in_db = "abc"

user_name_in_form = 'tutu'
user_password_in_form = '123'

if is_authenticated or (user_name_in_form in users_in_db and user_password_in_form == tutu_password_in_db):
    print("L'utilisateur peut accéder au backoffice")
else:
    print("Le login ou le mot de passe incorrect")

# -------------------------------------------------------
electricity = bool(random.randint(0, 1))
water = bool(random.randint(0, 1))
gas = bool(random.randint(0, 1))

print('electricity:', electricity)
print('water:', water)
print('gas:', gas)

# Vérifier que toutes les sources sont coupées
# si c'est le cas, affichez le message "Vous pouvez partir en WE"
# sinon, affichez le message "Vous ne pouvez pas partir en WE"

if not electricity and not water and not gas:
    print("Vous pouvez partir en WE")
else:
    print("Vous ne pouvez pas partir en WE")
    print("Il reste des sources à couper")
    
    if electricity:
        print("Coupez l'électricité")

    if water:
        print("Coupez l'eau")

    if gas:
        print("Coupez le gaz")

# -----------------------------------------------------------
has_cash = bool(random.randint(0, 1))
has_card = bool(random.randint(0, 1))
has_check = bool(random.randint(0, 1))

print('has_cash:', has_cash)
print('has_card:', has_card)
print('has_check:', has_check)

# Vérifier qu'au moins un moyen de paiement est disponible
# si c'est le cas, affichez le message "Vous pouvez partir faire des courses"
# sinon, affichez le message "Vous n'avez aucun moyenne de paiement"

if has_cash or has_card or has_check:
    print("Vous pouvez partir faire des courses")

    if has_cash:
        print("Vous avez de l'argent")

    if has_card:
        print("Vous avez une carte bancaire")

    if has_check:
        print("Vous avez un chèque")

else:
    print("Vous n'avez aucun moyenne de paiement")

# ------------------------------------------------------
age = random.randint(0, 100)

# 0-5   bébé
# 6-11  enfant
# 12-25 ado, jeune adult
# 26-59 adulte
# 60+   sénior

if age <= 5:
    print('bébé')

elif 6 <= age <= 11:
    print('enfant')

elif 12 <= age <= 25:
    print('ado, jeune adult')

elif 26 <= age <= 59:
    print('adulte')
    
# on peut aussi faire "else" pour intercepter les cas où l'age >= 60
elif age >= 60:
    print('sénior')

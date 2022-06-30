# ceci est un commentaire

from xxlimited import foo


# foo
# bar
# baz

nombre = 123
print(nombre)

nombre = 3.14
print(nombre)

nombre = "123"
print(nombre)

text = "lorem ipsum"
print(text)

is_day = True
print(is_day)

has_sugar = False
print(has_sugar)

has_accepted_ula = None
print(has_accepted_ula)

html_code = '<h1>Titre de mon blog</h1>'
print(html_code)

nickname = "John \"Dead\" Doe"
nickname = 'John O\'Connor'
print(nickname)

multiline_text = "foo\nbar\nbaz"
print(multiline_text)

multiline_text = """foo
bar
baz"""
print(multiline_text)

multiline_text = "\\foo\nbar\nbaz"
print(multiline_text)

number = "5"
print(number)
print(type(number))
number = int(number)
print(number)
print(type(number))

number = "2.71"
print(number)
print(type(number))
number = float(number)
print(number)
print(type(number))

nombre = 3.14
print(nombre)
print(type(nombre))
nombre = int(nombre)
print(nombre)
print(type(nombre))

texte = str(nombre)
print(texte)
print(type(texte))

my_var = 0
my_var = bool(my_var)
print(my_var)

my_var = 1
my_var = bool(my_var)
print(my_var)

my_var = -1
my_var = bool(my_var)
print(my_var)

my_var = 123
my_var = bool(my_var)
print(my_var)

my_var = -123
my_var = bool(my_var)
print(my_var)

my_var = 0.0
my_var = bool(my_var)
print(my_var)

my_var = 0.000001
my_var = bool(my_var)
print(my_var)

my_var = ""
my_var = bool(my_var)
print(my_var)

my_var = " "
my_var = bool(my_var)
print(my_var)

my_var = "0"
my_var = bool(my_var)
print(my_var)

my_var = "123"
my_var = bool(my_var)
print(my_var)

my_var = "-123"
my_var = bool(my_var)
print(my_var)

my_var = [123, "abc", False]
my_var = bool(my_var)
print(my_var)

my_var = [False]
my_var = bool(my_var)
print(my_var)

my_var = []
my_var = bool(my_var)
print(my_var)


my_var = [[]]
my_var = bool(my_var)
print(my_var)

my_var = [None]
my_var = bool(my_var)
print(my_var)


my_var = None
my_var = bool(my_var)
print(my_var)

n = 34.14
n = bool(int(n))
print(n)

# swap (inverser les valeurs)
a = 42
b = 123

# Méthode classique
x = a
a = b
b = x

# Méthode arithmétique
# a = a + b
# b = a - b
# a = a - b

# Destructured assignment
# Python, Js, Mais pas PHP
# a, b = b, a

if a == 123 and b == 42:
    print("Vous avez réussi à inverser les valeurs des variables")

# arrondi
import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

print(Decimal("0.5").quantize(Decimal("1"))) # Decimal('1')
print(Decimal("1.5").quantize(Decimal("1"))) # Decimal('2')
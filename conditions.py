#Job 1
valeur1 =10
valeur2 = 10

if valeur1 == valeur2:
    print("Valeurs1 est égale à Valeur2")
else: 
    print("Les deux valeurs ne sont pas égales")






#Job 2
age= 20
if age >= 18:
    print("Vous pouvez votez")
else:
    print("Vous nepouvez pas votez")






#Job 3
for i in range(101):
    if i ==26 or i == 37 or i == 88:
        continue
    print(i)

#ou 

for i in range(101):
    if i != 26 and i != 37 and i != 88:
        print(i)

#ou 
for i in range(101):
    if i not in [26, 37, 88]:
        print(i)








#Job 4
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)








#Job 5
for i in range(2, 1001):
    est_premier = True

    for diviseur in range(2, i):
        if i % diviseur == 0:
            est_premier = False
            break

    if est_premier:
        print(i)

#ou 
i = 2
while i < 1001:
    est_premier = True

    for diviseur in range(2, i):
        if i % diviseur == 0:
            est_premier = False
            break

    if est_premier:
        print(i)
    i += 1







#Job 6
I =int(input("Entrez un nombre entier positif : "))
while I <= 0:
    print("Veuillez entrer un nombre entier positif.")
    I = int(input("Entrez un nombre entier positif : "))


if I % 2 == 0:
    print(f"Le nombre {I} est pair")
else:
    print(f"Le nombre {I} est impair")
    







#Job 7
alphabet = "abcdefghijklmnopqrstuvwxyz"*10
ligne = ""

for lettre in alphabet:
    ligne = ligne + lettre
    print(ligne)







#Job 8
import math

a =float(input("Entrez la 1er longueur du triangle : "))
b =float(input("Entrez la 2ème longueur du triangle : "))
c =float(input("Entrez la 3ème longueur du triangle : "))

while a <= 0 or b <= 0 or c <= 0:
    print("Veuillez entrer des longueurs de triangle positives.")
    a = float(input("Entrez la 1er longueur du triangle : "))
    b = float(input("Entrez la 2ème longueur du triangle : "))
    c = float(input("Entrez la 3ème longueur du triangle : "))

rectangle = math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2)
isocele = a == b or b == c or a == c
equilateral = a == b == c
quelconque = a != b and b != c and a != c

if a+b>c and a+c>b and b+c>a:
    print("Le triangle est valide")
    if rectangle and isocele:
        print("Le triangle est rectangle et isocèle")
    elif rectangle:
        print("Le triangle est rectangle")
    elif equilateral:
        print("Le triangle est équilatéral")
    elif isocele:
        print("Le triangle est isocèle")
    elif quelconque:
        print("Le triangle est quelconque")
else:
    print("Le triangle n'est pas valide")


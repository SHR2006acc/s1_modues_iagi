# Objectif Relier les valeurs d’une boucle à une somme.
# total = 0
# for i in range(1, 6):
# total = total + i
# print(total)
# 1. Indiquez chaque valeur prise par i et total après chaque tour, puis la sortie exacte.
# 2. Modifiez ce programme pour lire un entier n ≥ 0 et calculer la somme des entiers de 1 à n inclus. Que
# donne n = 0 ?

# Question 1 :
# pour i = 1 : total = 0+1
# pour i = 2 : total = 1+2
# pour i = 3 : total = 3+3
# pour i = 4 : total = 6+4 
# pour i = 5 : total = 10+5

# result : total = 15

# Question 2 :
n=-1
while n<0 :
    n=int(input("Enter N : "))

total = 0
for i in range(1, n+1):
        total = total + i
print(total)


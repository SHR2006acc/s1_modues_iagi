# Objectif Travailler les indices, la moyenne et les cas limites.
# releves = [21, 23, 19, 25, 22]
# 1. Indiquez len(releves), releves[0], releves[-1] et le résultat d’un accès à releves[5].
# 2. Sans utiliser sum(), calculez la somme avec for, puis la moyenne. Donnez l’évolution de total après
# chaque relevé.
# 3. Parcourez à nouveau la liste pour afficher uniquement les valeurs strictement supérieures à la moyenne.
# Quelles valeurs apparaissent ?
# 4. Précisez ce qu’il faut vérifier avant de diviser par len(releves) si la liste peut être vide.

# Question 1 : 
print("Question 1 : ")
# releves = [21, 23, 19, 25, 22]

def rangeOutMessage():
    print("this line  will return an error , because the index is out of range ")    
    
releves = []
print(f" len(releves) : {len(releves)}")


try :
  print(f" releves[0] : {releves[0]}")
except : 
   rangeOutMessage()
   
try :
  print(f" releves[5] : {releves[5]}")
except : 
   rangeOutMessage()
   
try :
  print(f" releves[-1] : {releves[-1]}")
except : 
   rangeOutMessage()
 
print("Question 2 : ")
   
#Question 2 : 
somme = 0 
for releve in releves :
    somme += releve 
    
print(f"Somme : {somme}")
try :
  moyenne = somme / len(releves)
  print(f"Moyenne : {moyenne}")
except :
    print("Division Par 0 est interdit")
    

#Question 3 
print("Question 3 : ")

if not releves :
    print("Tableau vide ")
else :
    print("Valeurs Plus Grand Que La Moyenne : ")
    for releve in releves :
        if releve > moyenne :
            print(releve)

    





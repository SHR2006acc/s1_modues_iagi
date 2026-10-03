def affichage(temp,seuil):
    for i in range(0,len(temp),2):
        print("*"*20)
        print(f"temp : {temp[i]}")
        print(f"ecart : {temp[i]-seuil}")
        print(f"index : {temp[i+1]}")
    print("*"*20)
    print("\n")
    print(f" nombre de depassement : {len(temp)/2}")
    
def affichageParSeuil(temp,seuil):
    exist =0
    horsSeuil=[]
    count=0
    for i in range(len(temp)):
       if temp[i] > seuil :
           horsSeuil.append(temp[i])
           horsSeuil.append(i)
           count += 1
    if count == 0 : 
        print("-"*20)
        print("Aucun valeur est sepurieur au seuil")
        print("-"*20)
    else : 
        print(f"Temperature qui ont depasse le seuil {seuil} sont : \n")
        
        affichage(horsSeuil,seuil)
temp=[10,20,30,40,50]
print(temp)
seuil=int(input("Enter the seuil : "))
print('\n')
affichageParSeuil(temp,seuil)
print("\n")

# Composition et agrecation | ilistrer la deffirence 
#scraping d un site | collect de data from Sites
# streamlit example de base 

#
# 2 On se basant sur les 3 presentations (Fichier , exception et Heritage , proposer une activite de votre choix , simple et pedagogique )
class Personne :
    def __init__(self,nom,adresse):
          self.nom = nom
          self.adresse = adresse
    def afficher(self):
        print(f"| Nom : {self.nom} | Adresse : {self.adresse}")
        

class Employe (Personne) : 
    
    def __init__(self,nom,adresse,cnss):
        Personne.__init__(self,nom,adresse)
        self.cnss = cnss

    def afficher(self):
        print(f"| Nom : {self.nom} | Adresse : {self.adresse} | Id : {self.cnss}")
            
class Enseignant  (Personne) : 
    
    def __init__(self,nom,adresse,cnops):
        Personne.__init__(self,nom,adresse)
        self.cnops = cnops

    def afficher(self):
        print(f"| Nom : {self.nom} | Adresse : {self.adresse} | Id : {self.cnops}")
            
class Etudiant  (Personne) : 
    
    def __init__(self,nom,adresse,cne):
        Personne.__init__(self,nom,adresse)
        self.cne = cne

    def afficher(self):
        print(f"| Nom : {self.nom} | Adresse : {self.adresse} | Id : {self.cne}")
        
        
# Etudiant    
print("*"*50)    
print("|\\______________________________________________________")   

student1 = Etudiant("rayan","agadir","745jek")
print(">> Using Class Etudiant Directly")
student1.afficher()
print(">> Using Class Person Directly")
Personne.afficher(student1)
print("|\\______________________________________________________")   


   
# Enseignant 
print("*"*50)  
print("|\\______________________________________________________")   
     
prof = Enseignant("hamza","casa","ijef")
print(">> Using Class Enseignant Directly")
prof.afficher()
print(">> Using Class Enseignant  Directly")
Personne.afficher(prof)
print("|\\______________________________________________________")   
   

   
# Employee       
print("*"*50)     
print("|\\______________________________________________________")   
 
emp = Employe("khalid","asfi","jdwdjek")

print(">> Using Class Employe Directly")
emp.afficher()
print(">> Using Class Person Directly")
Personne.afficher(emp)
print("|\\______________________________________________________")   
     
print("*"*50)  




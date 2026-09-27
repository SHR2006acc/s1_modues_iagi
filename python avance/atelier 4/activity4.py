class Personne : 
    personList=[[],[],[]]
    def __init__(self,nom,adress):
        self.nom=nom
        self.adress=adress


class Employee(Personne):
    def __init__(self,nom,adress,identifier):
        super().__init__(nom,adress)

        self.identifier=identifier
        
    def afficher(self):
        print(f" Etudiant | Nom : {self.nom} | Adress : {self.adress} | Identifier : {self.identifier}")
    
class Enseignant(Personne):
    def __init__(self,nom,adress,identifier):
        super().__init__(nom,adress)
        self.identifier=identifier
    def afficher(self):
        print(f" Etudiant | Nom : {self.nom} | Adress : {self.adress} | Identifier : {self.identifier}")   
class Etudiant(Personne):
    def __init__(self,nom,adress,identifier):
        super().__init__(nom,adress)
        self.identifier=identifier
    def afficher(self):
        print(f" Etudiant | Nom : {self.nom} | Adress : {self.adress} | Identifier : {self.identifier}")
        
        
        
student1=Etudiant("Rayan","Casa","R63623")      
student1.afficher()

emp1=Employee("Lora","Usa","uwe8238")
emp1.afficher()

ens=Enseignant("Achraf","Agadir","8921482")
ens.afficher()
  
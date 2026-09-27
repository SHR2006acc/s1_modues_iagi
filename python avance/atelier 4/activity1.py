class Voiture :
    def __init__(self,code,marque,kilometrage):
        self.code=code
        self.marque=marque
        self.kilometrage=kilometrage
    def mod_kilo(self,newKilo):
        self.kilometrage=newKilo
    def afficher(self):
        print(f"Marque : {self.marque} | Code : {self.code}| Kilometrage : {self.kilometrage}")
    
    

ford=Voiture(123,"ford",290)
ford.afficher()
ford.mod_kilo(120)
ford.afficher()
    

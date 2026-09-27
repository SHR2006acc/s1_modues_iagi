class Etudiant :
    students=[]
    def __init__(self,matricule="Undefined",nom="Undefined",prenom="Undefined",note="Undefined"):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.note=note
    def afficher(self):
        print(f"Matricule : {self.matricule} | Full Name : {self.nom} {self.prenom} | Grade : {self.note }")
    def totalGrade():
        somme = 0
        for student in Etudiant.students :
            somme+=student.note
        return somme 
            
    def average():
        return Etudiant.totalGrade()/len(Etudiant.students)
print(f"\n {"-"*20}")    
print("Students :")

student1=Etudiant(3674,"Htalal","Mohamed",18)  #define student 1
Etudiant.students.append(student1) # add student to table
student1.afficher() #Show it to console

student2=Etudiant(8348,"Aymane","Lora",15) #define student 2
Etudiant.students.append(student2) # add student to table
student2.afficher() #Show it to console
print(f"\n {"-"*20}")
print(f"Total grades : {Etudiant.totalGrade()}")
print(f"Class's Average : {Etudiant.average()}")







import os
import time
from datetime import date


class Employe:  # employee Class :  identifiant,nom, prenom, dateNaissance, dateEmbauche, salaire
    employeList = []

    def __init__(self, identifiant, nom, prenom, dateNaissance, dateEmbauche, salaire):
        self.id = identifiant
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance
        self.dateEmbauche = dateEmbauche
        self.salaire = salaire

    class Date:  # Date Class , We will need this in dateNaissance, dateEmbauche
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

    def getId(self):
        return self.id

    def getSalaire(self):
        return self.salaire

    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getDateNaissance(self):
        return self.dateNaissance

    def getDateEmbauche(self):
        return self.dateEmbauche

    @staticmethod
    def addEmploye():  # function to add New Employees
        print(f"Welcome to addEmplee Form Section \n{"_"*20}")
        os.system("cls")
        id = int(input("Id : "))
        nom = input("Nom : ")
        prenom = input("Prenom : ")

        dayBirth = int(input("Day of Birth : "))
        monthBirth = int(input("Month of Birth : "))
        yearBirth = int(input("Year of Birth : "))
        dateNaissance = Employe.Date(dayBirth, monthBirth, yearBirth)

        dayEmbauche = int(input("Day of Embauche : "))
        monthEmbauche = int(input("Month of Embauche : "))
        yearEmbauche = int(input("Year of Embauche: "))

        salaire = int(input("Salaire : "))
        dateEmbauche = Employe.Date(dayEmbauche, monthEmbauche, yearEmbauche)

        # newEmployee =Employe(id,nom,prenom,dateNaissance,dateEmbauche)
        # Employe.employeList.append(newEmployee)

        newEmployee = Employe(
            id, nom, prenom, dateNaissance, dateEmbauche, salaire)
        Employe.employeList.append(newEmployee)

    def getEmployeeById(id):  # this function will return the employee obj by id
        for emp in Employe.employeList:
            if emp.id == id:
                return emp

        return None

    def printAge():  # this function will print the age of employee using his ID
        os.system("cls")
        print("Menu > Display Employees's Age \n")
        print("\n")
        EmpNumber = len(Employe.employeList)
        if EmpNumber == 0:

            print("0 Employee on Company")

        else:
            id = 0
            # we suppose that the id numbers is squetial id
            while (id > len(Employe.employeList) or id <= 0):
                os.system("cls")
                print("Menu > Display Employees's Age \n")
                print("\n")
                id = int(
                    input(f"Choose Id from ( 1 - {len(Employe.employeList)} ) : "))

                emp = Employe.getEmployeeById(id)
                print("\n\n")
                if (emp is None):
                    print("Something went wrong")
                else:
                    today = date.today()
                    print(
                        f" Id : {id} | age : {today.year - emp.dateNaissance.year} years old")
        print("\n")
        input("Click Enter Key to go back to the menu ")

    def getAnciente():
        os.system("cls")
        print("Menu > Display Employees's Anciente \n")
        print("\n")
        EmpNumber = len(Employe.employeList)
        if EmpNumber == 0:

            print("0 Employee on Company")

        else:
            id = 0
            # we suppose that the id numbers is squetial id
            while (id > len(Employe.employeList) or id <= 0):
                os.system("cls")
                print("Menu > Display Employees's Age \n")
                print("\n")
                id = int(
                    input(f"Choose Id from ( 1 - {len(Employe.employeList)} ) : "))

                emp = Employe.getEmployeeById(id)
                print("\n\n")
                if (emp is None):
                    print("Something went wrong")
                else:
                    today = date.today()
                    print(
                        f" Id : {id} | Anciente : {today.year - emp.dateEmbauche.year} years")
        print("\n")
        input("Click Enter Key to go back to the menu ")

    @staticmethod
    def displayEmployees():
        os.system("cls")
        print("Menu > Display Employees\n")
        EmpNumber = len(Employe.employeList)
        if EmpNumber == 0:
            print("0 Employee on Company")
        else:
            print("Employees Database : ")
            for employee in Employe.employeList:
                print("-"*10)
                print(f"\nId : {employee.id}  \nnom : {employee.nom}  \nprenom : {employee.prenom}  \ndate Naissance : {employee.dateNaissance.day}/{employee.dateNaissance.month}/{employee.dateNaissance.year} \ndate Embauche : {employee.dateEmbauche.day}/{employee.dateEmbauche.month}/{employee.dateEmbauche.year} \nSalaire : {employee.salaire}")
            print("\n")
            print("-"*10)
        print("\n")
        input("Click Enter Key to go back to the menu ")


def menu():
    print("-"*20)
    print("Type [1] : Display Employees")
    print("Type [2] : Add Employee")
    print("Type [3] : Employee's Age")
    print("Type [4] : Employee's Anciente")
    print("Type [5] : Quit")
    print("-"*20)


while True:

    choice = 0
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5):
        os.system("cls")
        print("Menu > \n")
        menu()
        choice = int(input("\n ||    "))

    if choice == 1:
        Employe.displayEmployees()  # display the employees

    elif choice == 2:
        Employe.addEmploye()  # add an employee
    elif choice == 3:
        Employe.printAge()  # display the age of employee using iD
    elif choice == 4:
        Employe.getAnciente()  # display the Seniority

    else:
        break  # break when u click 5 , mean quit the program


print("Thank you for the test !")

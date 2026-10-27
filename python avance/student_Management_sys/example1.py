
import os

class Student :
    students=[]
    def __init__(self,name,roll_number,marks): # Constructor 
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def add(self): # Add Student 
        Student.students.append(self)
    def update(self,choice,value): # Update Student Object
        if choice  == "name":
            Student.updateName(self,value)
        elif choice == "roll" :
            Student.updateRoll(self,value)
        else : Student.updateMarks(self,value)
    def updateName(self,newName):
        self.name=newName;   
    def updateRoll(self,newRoll):
        self.roll_number=newRoll;   
    def updateMarks(self,newMarks):
        self.marks=newMarks;   
    def view(self):
        print(self)
    def get(self,choice):
        if choice == "name" :
           return self.name
        elif choice == "roll":
            return self.roll_number
        else  : return self.marks
    
    def __str__(self):
        return f"Student : {self.name} . Number : {self.roll_number} . Marks : {self.marks}"

    def menu():
        print("1 -> Add Student")
        print("2 -> Update Student")
        print("3 -> Display All Students")
        print("4 -> Search Student By Roll Number")
        print("5 -> Search Student By Name")
        print("6 -> Delete Student")
        print("7 -> Exit")

def main():
    std1 : Student = Student("rayan","7841384",[12,18,10])
    std2 : Student = Student("hamza","78418935384",[12,18,10,11])
    print(    Student.students)

    Student.add(std1)
    Student.add(std2)
    print( Student.students)
    [print(f"Student : {Student.students[i].name} . Number : {Student.students[i].roll_number} . Marks : {Student.students[i].marks}") for i in range(len(Student.students)) ]


if __name__=="__main__":
    main()
       
   
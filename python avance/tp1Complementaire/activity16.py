import os

# Activité 16
# Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


def printNumbers(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(n-j,end="  ")
        n-=1 # without this line , we would stack on 5 , but we need to erase it , that s why i did n=n-1
        print("\n")
    
def menu():
    print("Type [1] To Try Again")
    print("Type [2] To Try Exit")

def chooseN(): # choose the N 
    n=0
    while(n<=0):
        os.system("cls")
        n=int(input("Enter N (None Null Positive Integer) : "))    
    return n

while(True):
    n=chooseN()
    printNumbers(n)
    input("\n\n<- Click Enter ->")
    choice= 0 # to enter to loop and choose choice
    while(choice!=1 and choice!=2):
        os.system("cls")
        menu()
        choice = int(input("\n\n || "))
    if choice==2 : break

print("Good Test")
    
    
    



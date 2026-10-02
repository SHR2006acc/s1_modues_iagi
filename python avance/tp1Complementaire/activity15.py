import os

# Activité 15
# Print the following pattern
# 1
# 3 2
# 6 5 4
# 10 9 8 7

def printNumbers(n):
    count =1
    for i in range(1,n+1):
        for j in range(i):
            print(count,end="  ")
            count+=1
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
    
    
    



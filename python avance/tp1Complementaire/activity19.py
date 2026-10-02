# Activité 19
# Print the following pattern
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# NOT DONE 

import os

def firstHalf(n):
  pass 
            
        
    

def secondHalf(n):
    for i in range(n-1):
       for j in range(n-i-1): # for j in range(i+1) for the fiest part
           print("*",end =" ")
       print("\n")        
def printStars(n):
    # for n = 2 : the number of lines is 3 / for n = 3 the number of lines is 5 . that s why i get :
    # the number of lines = 2 * n - 1 
    #
    #        *              =>  0
    #        *   *         
    #        *   *    *     =>  n-1
    #        *   *         
    #        *              =>  2n-2
    #
    
    firstHalf(n)
    
    
           
    
           
       
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
    printStars(n)
    input("\n\n<- Click Enter ->")
    choice= 0 # to enter to loop and choose choice
    while(choice!=1 and choice!=2):
        os.system("cls")
        menu()
        choice = int(input("\n\n || "))
    if choice==2 : break

print("Good Test")
    
    
    






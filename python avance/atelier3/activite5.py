
import os


def f1(number):
    print("Bonjour \n"*number)


def f2(number):  # isDivisibleBy 10
    if number % 10 == 0:
        return True
    else:
        return False


def f3(sentnce):  # nomber de voyelle
    count = 0
    for char in sentnce:
        if char == 'a' or char == 'u' or char == 'e' or char == 'o' or char == 'i':
            count += 1

    return count


def f4(number):  # factoriel

    produit = 1
    for i in range(1, number+1):
        produit *= i
    return produit


def f5(number):

    print(f"tableau de multiplication de : {number} de 1-10")
    for i in range(11):
        print(f" {number} * {i} = {number*i}")


def first_function():
    os.system("cls")
    n = int(input("Enter the number of bonjour : "))
    f1(n)
    input("Click enter ")


def second_function():
    os.system("cls")
    n = int(input(" Enter N to check if it s divisble by 10 : "))
    if f2(n) == True:
        print(f"{n} est divisible par 10 ")
    else:
        print(f"{n} n est pas  divisible par 10 ")
    input("Click Enter ")


def third_function():
    os.system("cls")
    sentence = input("Enter a Sentence : ")
    print(f"The sentence contain : {f3(sentence)} voyelles")
    input("Click Enter")


def fourth_function():
    os.system("cls")
    n = int(input("Enter N for factriel :"))
    print(f" !{n} = {f4(n)}")
    input("Click Enter")


def fifth_function():
    os.system("cls")
    n = int(input("Enter n for tableau de multiplication"))
    f5(n)
    input("Click Enter ")


def menu():
    print("-"*40)
    print("| Type [1] : Affiche Bonjour")
    print("| Type [2] : divisibilite par 10")
    print("| Type [3] : Compte les voyelles")
    print("| Type [4] : Factoriell")
    print("| Type [5] : Table Multiplication")
    print("| Type [6] : Sortie")
    print("-"*40)


print("Welcome to the classroom world ")
while True:

    choice = 0
    while (choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6):
        os.system("cls")
        print("Menu > \n")
        menu()
        choice = int(input("\n ||    "))

    if choice == 1:

        first_function()

    elif choice == 2:
        second_function()
    elif choice == 3:
        third_function()
    elif choice == 4:
        fourth_function()  # display the Seniority
    elif choice == 5:
        fifth_function()

    else:
        break  # break when u click 5 , mean quit the program


print("Thank you for the test !")

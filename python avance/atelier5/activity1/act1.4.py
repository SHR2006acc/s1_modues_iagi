

# 4 table de multiplication 
n=0
while n<=0 :
    n=int(input("Enter n (None Null Positive Integer) : "))

file = open(r"C:\Users\user\Desktop\S1\python avance\atelier5\activity1\Table_de_multiplication.txt","w")
file.write(f"Table de Multiplication de {n} ")
for i in range (1,11):
    file.write(f"\n {n} * {i} = {n*i} ")

file.close()
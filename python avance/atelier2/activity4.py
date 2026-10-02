

t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ["Janvier","Février","Mars","Avril","Mai","Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
"Décembre"]


    
# First Algorithme
monthPosition = 0
for i in range(12):
    t2.insert(2*i-1,t1[i]) 
print(t2)
   #Last Algorithme 
# monthPosition = 0
# for i in range(12):
#     indexNewPosition=monthPosition+i+1
#     t2.insert(indexNewPosition,t1[i])
#     monthPosition+=1
# print(t2)


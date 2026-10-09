
#3 lire fichier txt2

file =  open(r"C:\Users\user\Desktop\S1\python avance\atelier5\activity1\text2.txt","r")

try :
  for line in file.readlines():
     print(f"\n {line}")

except FileNotFoundError :

  print("File Not Found")

file.close()

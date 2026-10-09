import shutil

locationA = r"C:\Users\user\Desktop\S1\python avance\atelier5\activity2\from A\exercices.txt"

locationB = r"C:\Users\user\Desktop\S1\python avance\atelier5\activity2\to B\exercices.txt"

tmpLocation = r"C:\Users\user\Desktop\S1\python avance\atelier5\activity2\to B\tmp.txt"


fileRead = open(locationA,"r")
fileWrite = open(tmpLocation,"w")

//content 

shutil.move(locationA, locationB)
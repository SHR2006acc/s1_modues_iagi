import pandas as pd


filename = r"C:\Users\user\Desktop\S1\python avance\atelier7\maintenance.csv"
df = pd.read_csv(filename) 


# print(df)# display table

# #1
# print(df.shape) # display dimentions 

#2
# print(df.head()) # affiche les 5 premiers lignes

# #3
# index = df.columns
# print(index[0]) # return a list of column names 
# print(index[1]) # return a list of column names 
# print(index[3]) # return a list of column names 


# #4 
# print(df.info()) # Informations about the table 


# ## 5 
# # print(df.isnull()) # Count the number of None Values
# print(df.isnull().sum()) # Count the number of None Values



#  df.isnull : 
#      Nom    Age
# 0  False  False
# 1   True  False
# 2  False   True
# puis on va faire la somme 



## 6 
# print(df.duplicated().sum()) # Display le nombre de ligne dupliquer 


 
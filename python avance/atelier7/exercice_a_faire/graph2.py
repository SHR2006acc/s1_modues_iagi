from exercice import df 
from matplotlib import pyplot as plt

# Graph 1 : ID de controle en fonction de Cout_Non_Qualite_DH

plt.bar(df["ID_Controle"].head(10),df["Temperature_C"].head(10))
# plt.xticks(range(0,len(df["ID_Controle"]),5),rotation=45)
# plt.tight_layout()

plt.title(" ID de controle en fonction de Temperature_C")
plt.xlabel("ID de controle")
plt.ylabel("Temperature_C")
plt.legend()

plt.show()
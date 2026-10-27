from exercice import df 
from matplotlib import pyplot as plt

# Graph 1 : ID de controle en fonction de Cout_Non_Qualite_DH

plt.plot(df["ID_Controle"],df["Cout_Non_Qualite_DH"])
plt.xticks(range(0,len(df["ID_Controle"]),5),rotation=45)
plt.tight_layout()

plt.title(" ID de controle en fonction de Cout_Non_Qualite_DH")
plt.xlabel("ID de controle")
plt.ylabel("Cout_Non_Qualite_DH")
plt.legend()

plt.show()
from exercice import df 
from matplotlib import pyplot as plt

# Graph 1 : ID de controle en fonction de Cout_Non_Qualite_DH

plt.scatter(df["ID_Controle"].head(10),df["Temps_Controle_min"].head(10))
# plt.xticks(range(0,len(df["ID_Controle"]),5),rotation=45)
# plt.tight_layout()

plt.title(" ID de controle en fonction de Temps_Controle_min")
plt.xlabel("ID de controle")
plt.ylabel("Temps_Controle_min")
plt.legend()

plt.show()
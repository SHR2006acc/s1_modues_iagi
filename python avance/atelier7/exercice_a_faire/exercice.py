import pandas as pd



# 1. Question  : Importer le fichier CSV
filename = r"C:\Users\user\Desktop\S1\python avance\atelier7\qualite_industrielle.csv"
df = pd.read_csv(filename)

# 2. Question : structure et les données
# print(df.head())
# print("Dimensions :", df.shape)
# df.info()
# print(df.describe(include="all"))

# # 3. Question : valeurs manquantes et les doublons
# print("Valeurs manquantes :")
# print(df.isnull().sum())
# print("Nombre de doublons :", df.duplicated().sum())

# # 4. Question :  les variables liées à la qualité
# print("Colonnes :", df.columns)
# print(df.corr(numeric_only=True))

# 5. Nettoyer les données si nécessaire
df = df.drop_duplicates()
df = df.dropna(how="all")

# # 6. Sauvegarder le fichier nettoyé
# newFile = r"C:\Users\user\Desktop\S1\python avance\atelier7\qualite_industrielle_New.csv"
# df.to_csv(newFile, index=False)

# -----------------------------
# 7 :  un graphique avec Pandas
# -----------------------------

# Voir les fichiers de Graph



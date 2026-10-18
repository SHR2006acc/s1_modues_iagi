# 1. Écrivez une condition qui reconnaît une valeur invalide avec or, puis une condition équivalente qui
# reconnaît une valeur valide avec and.
# 2. Écrivez un programme qui redemande une mesure tant qu’elle est hors de l’intervalle, puis affiche «
# Mesure acceptée : X °C ».





temperature = float(input("Entrez une mesure : "))

while temperature < -50 or temperature > 60:
    temperature = float(input("Entrez une mesure : "))

print(f"Mesure acceptée : {temperature} °C")
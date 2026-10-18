temperature = float(input("Entrez la température : "))

if temperature < 5:
    print("Froid")
elif temperature > 30:
    print("Chaud")
else:
    print("Normal")
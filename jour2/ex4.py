temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]

# 1. tem > 25
temp_25 = []

for temp in temperatures:
    if temp > 25:
        temp_25.append(temp)

print("temperature > 25 :", temp_25)


# 2. temperature <= 25
temperatures_moins_ou_egal_25 = []

for temp in temperatures:
    if temp <= 25:
        temperatures_moins_ou_egal_25.append(temp)

print("temperature <= 25 :", temperatures_moins_ou_egal_25)


# 3. temperature entre 20 et 30 inclus
temperatures_entre_20_30 = []

for temp in temperatures:
    if 20 <= temp <= 30:
        temperatures_entre_20_30.append(temp)

print("temperature entre 20 et 30 :", temperatures_entre_20_30)


# 4 Compter les temperature > 30
compteur = 0

for temp in temperatures:
    if temp > 30:
        compteur = compteur + 1

print("Nombre de temperature > 30 :", compteur)
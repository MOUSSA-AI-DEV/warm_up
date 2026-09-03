notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
# afficher les notes
print("Toutes les notes :")
for note in notes:
    print(note)


# 2  Calculer la moyenne
moyenne = sum(notes) / len(notes)

print("moyenne:", moyenne)


# 3 notes sup la moyenne
notes_superieures = []

for note in notes:
    if note > moyenne:
        notes_superieures.append(note)

print("Notes supérieures à la moyenne :", notes_superieures)


# 4 note inf a la moyenne
notes_inferieures = []

for note in notes:
    if note < moyenne:
        notes_inferieures.append(note)

print("Notes inférieures à la moyenne :", notes_inferieures)


# 5 l bonne note  et la mauvaise note
meilleure_note = max(notes)
plus_mauvaise_note = min(notes)

print("meilleure note :", meilleure_note)
print("plus mauvaise note :", plus_mauvaise_note)


# 6 note >= 10
compteur = 0

for note in notes:
    if note >= 10:
        compteur = compteur + 1

print("Nombre de notes >= 10 :", compteur)


# 7. pourcentage de reaussite
pourcentage = (compteur / len(notes)) * 100

print("le porcentzge c est :", pourcentage, "%")
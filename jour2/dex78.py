etudiants = [
    {"nom": "Omar", "age": 22, "note": 15},
    {"nom": "Sara", "age": 21, "note": 17},
    {"nom": "Yassine", "age": 23, "note": 9},
    {"nom": "Imane", "age": 20, "note": 13},
    {"nom": "Hamza", "age": 24, "note": 7}
]

somme = 0
meilleure_note = 0
meilleur_etudiant = ""

for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"], "admis")
    else:
        print(etudiant["nom"], "echec")

    somme = somme + etudiant["note"]

    if etudiant["note"]>meilleure_note:
        meilleure_note=etudiant["note"]
        meilleur_etudiant=etudiant["nom"]

moyenne=somme/len(etudiants)

print("moyenne de classe :", moyenne)
print("meilleur etudiant :", meilleur_etudiant)
print("meilleure note :", meilleure_note)
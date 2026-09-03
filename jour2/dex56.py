
# 5
noms = ["Python", "SQL", "Pandas", "NumPy"]
niveaux = [5, 4, 3, 4]

resultat = dict(zip(noms, niveaux))

print(resultat)
# 6

etudiant = {
    "nom": "Omar",
    "age": 22,
    "formation": {
        "nom": "Développement IA",
        "niveau": "Avancé",
        "duree": 12
    }
}

print(etudiant["formation"]["nom"])

etudiant["formation"]["niveau"] = "Expert"

etudiant["technologies"] = {
    "Python",
    "SQL",
    "Pandas",
    "Machine Learning"
}

print(etudiant)
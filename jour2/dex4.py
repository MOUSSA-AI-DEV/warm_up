notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia": 14}
# Séparer les étudiants ayant une note ≥ 10 et < 10.
# Calculer le pourcentage de réussite et identifier le meilleur étudiant.



note_sup={}
note_inf={}

for key ,vlaue in notes_etudiants.items():
    if vlaue <10:
       note_inf[key]=vlaue
print (note_inf)
for key ,vlaue in notes_etudiants.items():
    if vlaue >10:
       note_sup[key]=vlaue
print(note_sup)
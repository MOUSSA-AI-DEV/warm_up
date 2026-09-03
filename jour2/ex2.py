langages = ["Python", "Java", "JavaScript", "C++"]


langages.append("PHP")
langages.append("SQL")
langages.insert(1, "C")
print("Après les ajouts :", langages)
langages.remove("Java")
langages.pop()
print("Liste finale :", langages)
print("Nombre d'éléments :", len(langages))
donnees = ["Omar", 25, "Casablanca", 15.5, True]
type_donnes={}
for mots in donnees:
    type_donnes[type(mots)]=mots
print(type_donnes)

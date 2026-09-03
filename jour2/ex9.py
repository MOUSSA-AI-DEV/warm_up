texte1 = "Python est un langage de programmation très populaire"
texte2 = "Java est un langage de programmation très utilisé"

liste1 = texte1.split()
liste2 = texte2.split()
print(liste1)
print(liste2)
liste1=[mots.lower() for mots in liste1]
liste2=[mots.lower() for mots in liste2]

liste1=[ mots for mots in liste1 if len(mots)>3]
liste2=[ mot for mot in liste2 if len(mot)>3]
print(liste1 ,liste2)
mots_commun=[]
for mots in liste1:
    for mo in liste2:
        if mots ==mo:
                mots_commun.append(mots)
                print(mots ,mo)
                break
print(mots_commun)



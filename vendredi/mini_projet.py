
import math
def chemin(chem):
    with open(f"{chem}","r") as file :
        result=file.readlines()
        print (f"  {result}")

# ch=input("enter the link of the file ")
# chemin(ch)


# 2. Calcul des distances



def calcule_distance(ville1, ville2):

    with open("ville.txt", "r") as file:

        x1 = y1 = x2 = y2 = None

        for line in file:
            nom, x, y = line.rsplit(maxsplit=2)
            nom = nom.strip('"')

            if nom == ville1:
                x1 = float(x)
                y1 = float(y)

            if nom == ville2:
                x2 = float(x)
                y2 = float(y)

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance
    # print(distance)


# calcule_distance("Bordeaux", "Paris")
# la premier ville
def trouver_coordonnees(ville):
    with open("ville.txt", "r") as file:
        for line in file:
            elements = line.split()

            if elements[0] == ville:
                x = float(elements[1])
                y = float(elements[2])
                return x, y

def ville_plus_proche(ville_actuelle, villes_non_visitees):

    distance_min = float("inf")
    prochaine_ville = None

    for ville in villes_non_visitees:

        distance = calcule_distance(ville_actuelle, ville)
# plus proche 
        if distance < distance_min:
            distance_min = distance
            prochaine_ville = ville

    return prochaine_ville

def itineraire_greedy(villes):

    itineraire = [villes[0]]
    non_visitees = villes[1:].copy()

    ville_actuelle = villes[0]

    while non_visitees:
# la plus proche 
        prochaine_ville = ville_plus_proche(
            ville_actuelle,
            non_visitees
        )

        itineraire.append(prochaine_ville)

        non_visitees.remove(prochaine_ville)

        ville_actuelle = prochaine_ville

    return itineraire
villes = []

with open("ville.txt", "r") as file:
    for line in file:
        ville, x, y = line.rsplit(maxsplit=2)
        ville = ville.strip('"')
        villes.append(ville)

# print(villes)
# villes = ["Paris", "Lyon", "Marseille", "Nice"]
re=itineraire_greedy(villes)
def distance_totale(itineraire):
    total = 0

    for i in range(len(itineraire) - 1):
        distance = calcule_distance(
            itineraire[i],
            itineraire[i + 1]
        )

        total = total + distance

    return total
t=distance_totale(re)
print(t)
# print(f"sssssssssss{re}")
print("Nombre total de villes :", len(villes))
# print("Itinéraire trouvé :", re)
print("Distance totale :", t)
# print(calcule_distance("Paris", "Lyon"))
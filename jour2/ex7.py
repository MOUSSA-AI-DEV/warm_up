L = [7, 23, 5, 23, 7, 19, 23, 12, 29]

def compter_occurrences(element, liste):

    compteur = 0

    for valeur in liste:
        if valeur == element:
            compteur += 1

    return compteur


print(compter_occurrences(23, L))
print(compter_occurrences(7, L))
print(compter_occurrences(100, L))
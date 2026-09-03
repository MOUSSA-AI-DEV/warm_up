L = [10, 20, 30, 40, 50]
def recherche_element(element,L):
    for i in range (len(L)) :
        if L[i]==element:
            return i 
    return False


L = [10, 20, 30, 40, 50]

print(recherche_element(30, L))
print(recherche_element(100, L))
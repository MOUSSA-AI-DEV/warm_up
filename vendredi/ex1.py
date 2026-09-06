import math

# CHALLENGE : ALGORITHMIQUES REGROUPÉS
# Objectif : Développer plusieurs petites fonctions indépendantes, chacune ciblant une compétence précise
# Travail à faire :
# • Demander à l’utilisateur de saisir un nombre entier n et afficher la factorielle de ce nombre ( n! ).
# • Demander à l’utilisateur un nombre entier m et afficher sa table de multiplication de 1 à 10.
# • Demander à l’utilisateur un nombre entier L et indiquer s’il s’agit d’un carré parfait.
# • Demander une chaîne de caractères à l’utilisateur, puis afficher chaque caractère un par un.
# • Demander une phrase à l’utilisateur et afficher le mot le plus long de cette phrase.
# • Demander une chaîne de caractères Ch et afficher le nombre d’occurrences de chaque caractère.
# Exemple : Pour Ch = “artificial intelligence developer”
# Le programme doit afficher : Le caractère "i" figure 5 fois dans la chaîne Ch.

#  Demander à l’utsilisateur de saisir un nombre entier n et afficher la factorielle de ce nombre ( n! ).
def factorielle ():
    N=int( input("enter nombre entier\n"))
    factorielle=1
    for i in range(1,N+1):
        factorielle=factorielle*i
    print( factorielle )
# factorielle()

# • Demander à l’utilisateur un nombre entier m et afficher sa table de multiplication de 1 à 10.
def multiplication():
    number=int(input("enter the number de multiplication \n"))
    table_de_multiplication=[]
    for i in range (1,11):
        m=number*i
        table_de_multiplication.append(m)
    print(table_de_multiplication)
# multiplication()
# • Demander à l’utilisateur un nombre entier L et indiquer s’il s’agit d’un carré parfait.
def carre_parfait():
    number=int (input("enter your number"))
    result = math.sqrt(number)
    if result*result==number:
        print("is caree parfait ")
    else :
        print ( "is not carre parfait ")


# carre_parfait()

# • Demander une chaîne de caractères à l’utilisateur, puis afficher chaque caractère un par un.
def par_caractere():
    charactere=input("enter the word please ")
    for i in range (0,len(charactere)):
        print(charactere[i])

# par_caractere()
# • Demander une chaîne de caractères Ch et afficher le nombre d’occurrences de chaque caractère.

def occurence_caracter():
    word=input("enter the word ")
    les_occurence={}
    for i in range(len(word)):
        count=0
        for j in range(len(word)):
            if word[i]==word[j]:
                count =count+1
        les_occurence[word[i]]=count
    print(les_occurence)


occurence_caracter()

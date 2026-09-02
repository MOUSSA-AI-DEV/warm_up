# 1__

# print("helol give me your name ")
# first_name=input(str("enter your firstname_name "))
# last_name=input(str("enter your laast_name "))

# print (f"hello mr   {first_name}   {last_name}")

# 2___
# return il faut utiliser  alinterne du fonction on pas fait return h=g

# print("hello we have to calcule somthing ")
# nom =input("enter your full name ")
# salaire = float( input ("enter your salaire "))
# houres= float(input("enter your hours in work"))
# print(salaire*2)
# print (houres)
# if houres>40 :
#     salaire_is=salaire * 1.5
#     print(f"salaire is {salaire_is}")
# else :
#     #  salaire_is=salaire
#     #  return salaire_is 
#     print(f"salaire is {salaire_is}")



#  3__ Contrôle d'accès à un club privé

# age = int(input("Entrez votre age  : "))

# if age < 18:
#     print("entre refuse.")

# elif age <= 25:
#     print("Entrée gratuite.")

# else:
#     membre = input(" membre du club  oui : ")
#     accompagne = input(" accompagne par un membre  oui non : ")

#     if membre == "oui" or accompagne == "oui":
#         print("autorise .")
#     else:
#         print("refuse")




# partie de les boucles 2
# Écrivez un programme Python qui demande à l'utilisateur de saisir un nombre entier N, puis calcule et 
# affiche la somme de tous les entiers compris entre 1 et N

# nombre_n=int(input("entez un nombre entier "))
# s=0
# for i in range(nombre_n):
#     s=s+i
#     print(s)

#  2—Inverser une chaîne
# Écrivez un programme Python qui demande à l'utilisateur de saisir une chaîne de caractères, puis 
# affiche cette chaîne inversée.

chaine_de_caractere=str(input("entre une chaine de caractere\n"))
le_mots_reverser=""


print(len(chaine_de_caractere))
N=len(chaine_de_caractere)-1
while N>=0 : 
    le_mots_reverser=le_mots_reverser+chaine_de_caractere[N]
    N-=1


print (le_mots_reverser)
     


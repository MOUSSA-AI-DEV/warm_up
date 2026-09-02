numbers = [-3, -2, 0, 1, 2, 3]

positive =[x for x in numbers if x>0]

print(positive)
numbers = [-3, -2, 0, 1, 2, 3]

positive = [x for x in numbers if x >= 0]

print(positive)

# Permet d'avoir l'index + la valeur.

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

    # crud sur les fichier 
    # ********writing *********
f = open("test.txt", "w", encoding="utf-8")
f.write("Bonjour Moussa")
f.close()

# reading **********
f = open("test.txt", "r", encoding="utf-8")

content = f.read()

print(content)

f.close()






#********** memorise ******

# 1. f-string
name = "Moussa"
print(f"Bonjour {name}")

# 2. format()
print("Bonjour {}".format(name))

# 3. écrire
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Bonjour")

# 4. lire
with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()



#    ******** exception ******
#  except RuntimeError, TypeError, NameError:
#    pass
while true :
    try :
        x=int(input("please enter a number "))
    except valueError :
        print("oops ! that no valid number . try again ...")
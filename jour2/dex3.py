notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}
for key in notes:
    print (key)


for value in notes.values():
    print(value)

count=0
for value in notes.items():
    count=count+1
    print(value)
print(count)


# Calculer la moyenne, la meilleure et la plus mauvaise note.

somme =0

for value in notes.values():
    somme = somme + value
moyenne = somme / count
print(f"moyenneis {moyenne}")   

# meilleure

meilleure = 0

for value in notes.values():
    if value > meilleure:
        meilleure = value

print(f"meilleure note : {meilleure}")


#mauvaise note
mauvaise = 20

for value in notes.values():
    if value < mauvaise:
        mauvaise = value

print(f"plus mauvaise note : {mauvaise}")
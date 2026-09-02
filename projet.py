def add_contact():
    name=str(input("enter your name\n"))
    email=str(input("enter your email\n"))
    phone=input("enetr your phone\n")
    if name == "" or email == "" or phone == "":
            print("Please enter all the information")
            return
    print(name)
    print(email)
    print(phone)
    with open("contact.txt", "a") as fichier:
           fichier.write(name + " | " + phone + " | " + email + "\n")

    print("the infomation are adedd succesfuly")

# add_contact()

def show_contact():
    with open("contact.txt", "r") as fil :
          contenu=fil.read()
    if contenu == "":
            print("There are no contacts")

    else:
            print("\n===== MY CONTACTS =====")
            print(contenu)

# show_contact()
def delete_contac():
    delete_user=input("enter the user that you want to delete ")
    
    if delete_user == "":
        print("Please enter a name")
        return


    with open("contact.txt") as lines:
         users=lines.readlines()

    with open("contact.txt","w") as delete_action:
         for user in users :
            if not user.startswith(delete_user) :
                 delete_action.write(user)

    print("contact delted succcesfuly")
                 
# delete_contac()


def update_contact():
    name_to_update = input("Enter the name to update: ")
    if name_to_update == "":
        print("Please enter a name")
        return
    new_email = input("Enter the new email: ")
    new_phone = input("Enter the new phone: ")
    if new_email == "" or new_phone == "":
        print("Email and phone cannot be empty")
        return
    with open("contact.txt", "r") as fichier:
        lignes = fichier.readlines()

    with open("contact.txt", "w") as fichier:
        for ligne in lignes:

            if ligne.startswith(name_to_update):
                fichier.write(name_to_update + " | " + new_phone + "|" + new_email + "\n" )
            else:
                fichier.write(ligne)

    print("contact updated succefuly")
# update_contact()



while True:

    the_case = int(input("""


1 => Add contact
2 => Show contacts
3 => Delete contact
4 => Update contact
0 => Exit
Choose an option   """))

    match the_case:
        case 1:
            add_contact()
        case 2:
            show_contact()
        case 3:
            delete_contact()
        case 4:
            update_contact()
        case 0:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice!")
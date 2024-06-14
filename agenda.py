import os

def menu_agenda():
    o=0
    while o<1 or o>4:
        print("""
            Agenda
            1. Veure contactes
            2. Afegir contacte
            3. Eliminar contacte
            4. Sortir
            """)
        o=int(input("Introdueixi una opció: "))
        if o<1 or o>6:
            print("Opció no vàlida, torni a triar una opció \n")
        else:
            return o

def veure_contactes():
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", "r") as arxiu:
            contactes = arxiu.readlines()
            if contactes:
                print("\nLlista de contactes:")
                for contacte in contactes:
                    print(contacte.strip())
            else:
                print("\nLa agenda està buida.")
    else:
        print("\nLa agenda està buida.")

def afegir_contacte():
    nom = input("Ingresa el nom del contacte: ")
    telefon = input("Ingresa el nombre de telèfon del contacte: ")
    with open("agenda.txt", "a") as arxiu:
        arxiu.write("{}: {}\n".format(nom, telefon))
    print("\nS'ha afegit el contacte {}.".format(nom))

def eliminar_contacte():
    veure_contactes()
    nom = input("\nIngrese el nom del contacte que vol eliminar: ")
    with open("agenda.txt", "r") as arxiu:
        contactes = arxiu.readlines()
    with open("agenda.txt", "w") as arxiu:
        eliminat = False
        for contacte in contactes:
            if nom not in contacte:
                arxiu.write(contacte)
            else:
                eliminat = True
        if eliminat:
            print("\nS'ha eliminat el contacte {}.".format(nom))
        else:
            print("\nEl contacte especificado no se encontró en la agenda.")


def pagenda():
    o = 1
    while o!= 4:
        o=menu_agenda()
        match(o):
            case 1:
                veure_contactes()
            case 2:
                afegir_contacte()
            case 3:
                eliminar_contacte()
            case other:
                print("Has sortit d'aquest programa")

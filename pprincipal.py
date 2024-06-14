import os
import mastermind
import agenda
import tictactoe
import classes
import poke
import Ex_servidor

def menu():
    op=0
    while op<1 or op>7:
        print("""
        Programa principal
              1. Llistes, numeros aleatoris
              2. Agenda
              3. 3 en raya
              4. Objectes, classe, herència, polimorfisme
              5. Scrapping
              6. Servei web
              7. Sortir
            """)
        op=int(input("Introdueixi una opció: "))
        if op<1 or op>7:
            print("Opció no vàlida, torni a elegir una opció \n")
        else:
            return op
        

def objectes():
    print("Has entrat en el quart exercici")

def scrapping():
    print("Has entrat en el cinquè exercici")

def servei_web():
    print("Has entrat en el sisè exercici")
            
#Programa principal
op=1
while op!=7:
    op=menu()
    match(op):
        case 1:
            mastermind.ppmastermind()
        case 2:
            agenda.pagenda()
        case 3:
            tictactoe.pptictactoe()
        case 4:
            classes.pclasses()
        case 5:
            poke.ppokemon()
        case 6:
            Ex_servidor.iniciar_servidor()
        case other:
            print("Has sortit del programa")
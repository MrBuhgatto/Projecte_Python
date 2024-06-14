from random import randint as ri

def genera_llista():
    l = []
    for i in range(3):
        l.append(ri(0, 9))
    return l
    
def genera_resposta():
    l = []
    for i in range(3):
        a=int(input("Introdueix el numero: "))
        l.append(a)
    return l

def compara(l,n):
    a=[0,0,0]
    for i in range(3):
        if l[i]==n[i]:
            a[i]=10
    if a[0]==10 and a[1]==10 and a[2]==10:
        print("Enhorabona, ho has trobat tot!")
        return 0
    for i in range(3):
        if a[i] == 0:
            if n[i] in l:
                a[i] = 5
    for i in range(3):
        if a[i]==10:
            print("L'element {} és correcte".format(n[i]))
        elif a[i]==5:
            print("L'element és correcte però no està en el seu lloc".format(n[i]))
        else:
            print("L'element no existeix".format(n[i]))

def ppmastermind():
    op = 1
    l = genera_llista()
    while op != 0:
        n = genera_resposta()
        op=compara(l,n)
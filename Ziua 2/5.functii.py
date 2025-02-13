def adunare(a,b):
    return a+b

def scadere(a,b):
    return a-b

def inmultire(a,b):
    return a*b

o_noua_functie = scadere


def calcul(a,b,func):
    return func(a,b)

print(o_noua_functie(2,3))
print(adunare)

calcul(10,3,scadere)

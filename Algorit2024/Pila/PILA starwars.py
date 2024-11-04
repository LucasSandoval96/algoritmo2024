from pila import Stack

starwars5=["luke skywalter","dart vader","yoda","han solo","chewbaca","C-3PO","R2-D2","bossk","lobot","boba fett"]
starwars7=["han solo","kylo ren","rey","luke skywalter","chewbacca","finn","BB-8","C-3PO","R2-D2","leia organa"]
#starwars5=["luke skywalter","chewbacca","boba fett"]
#starwars7=["chewbacca","luke skywalter","yoda"]

pila_starwars5=Stack()
pila_starwars7=Stack()
pila_aux=Stack()
pila_ambas=Stack()

for personajes in range (len(starwars5)):
    print(personajes)
    pila_starwars5.push(starwars5[personajes])
    pila_starwars7.push(starwars7[personajes])
    print(pila_starwars5.on_top())
    print(pila_starwars7.on_top())
    print()
    

while pila_starwars5.size()>0:
    personaje=pila_starwars5.pop()
    x=input("---------")
    while pila_starwars7.size()>0:
        print("entro al ciclo 2")
        if personaje == pila_starwars7.on_top():
            print(personaje, "es igual a", pila_starwars7.on_top())
            pila_ambas.push(personaje)
            print(pila_starwars7.on_top())
            pila_starwars7.pop()
            print(pila_starwars7.on_top())
            x=input("el personaje es el mismo")
        else:
            print(personaje, "no es igual a", pila_starwars7.on_top())
            pila_aux.push(pila_starwars7.pop())
            print("ahora la pila aux tiene a: ",pila_aux.on_top())
            print("ahora la pila 7 tiene a: ",pila_starwars7.on_top())
            x=input("no es igual")
    print("------------------")
    while pila_aux.size()>0:
        pila_starwars7.push(pila_aux.pop())
        print(pila_starwars7.on_top())


print("la cantidad de personajes que aparecen en ambas peliculas son: ",pila_ambas.size())
for personajes in range (pila_ambas.size()):
    print(pila_ambas.on_top())
    pila_ambas.pop()


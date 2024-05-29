from pila import Stack
def devolver_pila (heros,pila_aux):
    while pila_aux.size()>0:
        heros.push(pila_aux.pop())
    

class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad_peliculas}"
    
superheroes = [
    {'hero': 'Capitan America','peliculas':11},
    {'hero':'Iron Man','peliculas':9},
    {'hero':'Rocket Racoon','peliculas':6},
    {'hero':'Thor','peliculas':8},
    {'hero':'Black Widow','peliculas':9},
    {'hero':'Hulk','peliculas':9},
    {'hero':'Ant-Man','peliculas':5},
    {'hero':'Groot','peliculas':5},
    {'hero':'Bruja Escarlata','peliculas':7},
    {'hero':'Daredevil','peliculas':5},
    {'hero':'Doctor Strange','peliculas':6},
    {'hero':'Nick fury','peliculas':11},
]
    

heros=Stack()
pila_aux=Stack()

for heroe in superheroes:
    heros.push(Personaje(heroe['hero'],heroe['peliculas']))
    
print("--------------------------------------------")
c=0
pos=0
while heros.size()>0:
    pos+=1
    comparacion=heros.pop()
    if comparacion.nombre =="Groot":
        print("Groot se encuentra en la posicion:",pos)
    elif comparacion.nombre == "Rocket Racoon" :
        print("Rocket Racoon se encuentra en la posicion",pos)
    pila_aux.push(comparacion)

x=devolver_pila(heros,pila_aux)

print("--------------------------------------------")
print("los heroes que aparecen en mas de 5 peliculas son:")
while heros.size()>0:
    comparacion=heros.pop()
    if (comparacion.cantidad_peliculas > 5):
        print (comparacion.nombre,"aparece en ", comparacion.cantidad_peliculas)
    pila_aux.push(comparacion)
x=devolver_pila(heros,pila_aux)
print("--------------------------------------------")
     
while heros.size()>0:
    comparacion=heros.pop()
    if (comparacion.nombre == "Black Widow"):
         print("Black Widow participo en: ",comparacion.cantidad_peliculas)
    pila_aux.push(comparacion)

x=devolver_pila(heros,pila_aux)
print("--------------------------------------------")
while heros.size()>0:
    comparacion=heros.pop()
    if (comparacion.nombre[0] == "C") or (comparacion.nombre[0] == "D") or (comparacion.nombre[0] == "G"):
        print("el personaje contiene c,d o g. Estos son sus datos:",comparacion)
    pila_aux.push(comparacion)    

x=devolver_pila(heros,pila_aux)
print("--------------------------------------------")
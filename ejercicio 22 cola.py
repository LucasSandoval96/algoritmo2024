#ejercicio 22   
from cola import Queue
def devolver_pila (heros,pila_aux):
    while pila_aux.size()>0:
        heros.push(pila_aux.pop())

def buscar(cola,buscado,criterio):
    for personaje in range (cola.size()):
        comparacion=cola.on_front()
        print()
        if comparacion.criterio == buscado:
            print("{buscado} esta en la cola")



    

class Personaje:
    def __init__(self, nombre, heroe,sexo):
        self.nombre = nombre
        self.heroe = heroe
        self.sexo = sexo
    
    def __str__(self):
        return f"{self.nombre} {self.heroe} {self.sexo}"
    
Personajes = [
    {'nombre': '89P13', 'heroe': 'Rocket Raccoon', 'sexo': 'm'},
    {'nombre': 'Tony Stark', 'heroe': 'Iron Man', 'sexo': 'm'},
    {'nombre': 'Steve Rogers', 'heroe': 'Capitan America', 'sexo': 'm'},
    {'nombre': 'Natasha Romanoff', 'heroe': 'Black Widow', 'sexo': 'f'},
    {'nombre': 'Loki', 'heroe': 'Loki', 'sexo': 'm'},
    {'nombre': 'Thor', 'heroe': 'Thor', 'sexo': 'm'},
    {'nombre': 'Bruce Banner', 'heroe': 'Hulk', 'sexo': 'm'},
    {'nombre': 'Nicholas Joseph Fury', 'heroe': 'Nick fury', 'sexo': 'm'},
    {'nombre': 'Peter Parker', 'heroe': 'Spider-Man', 'sexo': 'm'},
    {'nombre': 'Carol Danvers', 'heroe': 'Capitana Marvel', 'sexo': 'f'},
    {'nombre': 'Scott Lang', 'heroe': 'Ant-Man', 'sexo': 'm'},
]

cola=Queue()

print("--------------------------------------------")
for per in Personajes:
    cola.arrive(Personaje(per['nombre'],per['heroe'],per['sexo']))

for per in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()

print("--------------------------------------------")

for per in range (cola.size()):
    comparacion=cola.on_front()
    if (comparacion.sexo == 'm'):
        print(cola.on_front())
        cola.move_to_end()
    else:
        cola.move_to_end()
print("--------------------------------------------")
for per in range (cola.size()):
    comparacion=cola.on_front()
    if (comparacion.sexo == 'f'):
        print(cola.on_front())
        cola.move_to_end()
    else:
        cola.move_to_end()
print("--------------------------------------------")
buscado='Capitana Marvel'
#criterio='heroe'
#x=buscar(cola,buscado,criterio)
print("--------------------------------------------")
for per in range (cola.size()):
    comparacion=cola.on_front()
    if (comparacion.heroe == buscado):
        print(f"{buscado} es {comparacion.nombre}")
        cola.move_to_end()
    else:
        cola.move_to_end()
print("--------------------------------------------")
buscado='Carol Danvers'
for per in range (cola.size()):
    comparacion=cola.on_front()
    if (comparacion.nombre == buscado):
        print(f"{buscado} es {comparacion.heroe}")
        cola.move_to_end()
    else:
        cola.move_to_end()
print("--------------------------------------------")
buscado='Scott Lang'
for per in range (cola.size()):
    comparacion=cola.on_front()
    if (comparacion.nombre == buscado):
        print(f"{buscado} es {comparacion.heroe}")
        cola.move_to_end()
    else:
        cola.move_to_end()
print("--------------------------------------------")
for per in range (cola.size()):
    comparacion=cola.on_front()
    if comparacion.nombre[0] == 'S' or comparacion.heroe[0] == 'S':
        print(f"nombre de heroe o nombre con s {comparacion}")
        cola.move_to_end()
    else:
        cola.move_to_end()

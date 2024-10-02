
from cola import Queue

class Personaje:

    def __init__ (self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__ (self):
        return f' {self.nombre} - {self.planeta} '

Personajes = [
    {'nombre': 'Yoda', 'planeta': 'Dagobah'},
    {'nombre': 'Luke Skywalker', 'planeta': 'Tatooine'},
    {'nombre': 'Han Solo', 'planeta': 'Corellia'},
    {'nombre': 'Jar Jar Binks', 'planeta': 'Naboo'},
    {'nombre': 'Ahsoka Tano', 'planeta': 'Shili'},
    {'nombre': 'Anakin Skywalker', 'planeta': 'Tatooine'},
    {'nombre': 'Chewbacca', 'planeta': 'Kashyyyk'},
    {'nombre': 'Leia Organa', 'planeta': 'Alderaan'},
    {'nombre': 'Boba Fett', 'planeta': 'Kamino'},
    {'nombre': 'Jan Ors', 'planeta': 'Alderaan'},
    {'nombre': 'Mercurial Swift', 'planeta': 'Corellia'},
    {'nombre': 'Vane', 'planeta': 'Shili'},
    {'nombre': 'Almirante Ackbar', 'planeta': 'Endor'},
    {'nombre': 'Wicket W. Warrick', 'planeta': 'Endor'},
    {'nombre': 'Teek', 'planeta': 'Endor'},
]

cola=Queue()

def planeta(cola,buscado):
    for per in range (cola.size()):
        if cola.on_front().planeta == buscado :
            print(cola.on_front())
            cola.move_to_end()
        else:
            cola.move_to_end() 

def buscarpersonaje(cola,buscado):
    for per in range (cola.size()):
        if cola.on_front().nombre == buscado :
            print(cola.on_front())
            cola.move_to_end()
        else:
            cola.move_to_end()

def separar():
    print("--------------------------------------------")

for per in Personajes:
    cola.arrive(Personaje(per['nombre'],per['planeta']))

for per in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()

#mostrar los personajes del planeta Alderaan, Endor y Tatooine
separar()
print('personajes de Alderaan:')
buscado = 'Alderaan'
planeta(cola,buscado)
separar()
print('personajes de Endor:')
buscado = 'Endor'
planeta(cola,buscado)
separar()
print('personajes de Tatooine:')
buscado = 'Tatooine'
planeta(cola,buscado)
separar()

#indicar el plantea natal de Luke Skywalker y Han Solo
buscado= 'Luke Skywalker'
buscarpersonaje(cola,buscado)
separar()
buscado= 'Han Solo'
buscarpersonaje(cola,buscado)
separar()

#insertar un nuevo personaje antes del maestro Yoda
buscado= 'Yoda'
for per in range (cola.size()):
        if cola.on_front().nombre == buscado:
            cola.arrive(Personaje('Onyx Cinder','Shili'))
            cola.move_to_end()
        else:
            cola.move_to_end()

for per in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()

separar()

#eliminar el personaje ubicado después de Jar Jar Binks
buscado= 'Jar Jar Binks'
for per in range (cola.size()-1):
        if cola.on_front().nombre == buscado:
            cola.move_to_end()
            cola.attention()
        else:
            cola.move_to_end()

for per in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()






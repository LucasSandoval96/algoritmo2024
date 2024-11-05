from heap2 import HeapMax
from random import randint,choice
from datetime import time
#El general Hux es la persona encargada de administrar todas las operaciones de la base Starkiller,
#para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que se realizan, contemplando lo siguiente:
# a- debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguiente criterio: 
# pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma nivel dos y 
# el resto de las operaciones nivel a cargo de los generales de la base de nivel uno
# b- de cada actividad se conoce quien es el encargado, una descripción, la hora y opcionalmente la cantidad de Stormtroopers requeridos
# c- utilizar una cola de prioridad para administrar las distintas operaciones, 
# debe cargar al menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno
# d- opcionalmente se podrán agregar operaciones luego de atender una
# e- realizar la atención de las operaciones de la cola
# f- luego de atender la quinta operación, agregar una operación solicitada por 
# capitán Phasma para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers
# g- luego de atender la sexta operación, agregar una operación solicitada por el líder supremo Snoke para destruir el planeta Takodana.

class Misionclas:
    def __init__(self, nivel_atencion, encargado,descripcion,hora,cant_storm):
        self.nivel_atencion = nivel_atencion
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.cant_storm = cant_storm

    
    def __lt__(self, other):
        return self.nivel_atencion < other.nivel_atencion

    def __le__(self, other):
        return self.nivel_atencion <= other.nivel_atencion

    def __gt__(self, other):
        return self.nivel_atencion > other.nivel_atencion

    def __ge__(self, other):
        return self.nivel_atencion >= other.nivel_atencion

    def __repr__(self):
        return f"{self.nivel_atencion} {self.encargado} {self.descripcion} {self.hora} {self.cant_storm}"
    
def separar ():
    print('-----------------------------------------------------------------------------------------')

misiones = []

h = HeapMax()
listaencargado = ['generales random nivel bajo','capitan phasma','kylo ren','lider supremo Snoke']
listadescripcion = ['ataque','reconocimiento','defensa','revision','limpieza']

#prioridad lider supremo snoke y kylo ren nivel 3, capitan phasma nivel 2 y el resto nivel 1
#h.elements = [[3, 'lider supremo Snoke'], [3, 'kylo ren'], [2, 'capitan phasma'], [3, 'generales']]
#encargado, descripcion, hora y cant stormtroopers (opcional)

for i in range (15):
    nivel = randint(1,3)
    if nivel == 3:
        encargado = listaencargado[randint(2,3)]
    else:
        encargado = listaencargado[nivel-1]

    descripcion = choice(listadescripcion)
    hora = time(randint(0,23),randint(0,59))
    cant_storm = (randint(0,100))
    print(hora)
    separar()
    mision = Misionclas(nivel, encargado, descripcion, hora, cant_storm)
    # mision = Misionclas(nivel, encargado, descripcion, hora, cant_storm)
    # h.add(mision)
    misiones.append([nivel,{'nivel_atencion': nivel,'encargado':encargado,'descripcion':descripcion,"hora":hora,"cant_storm":cant_storm}])
    h.add(mision)


separar()
print("esto es la lista")
for mision in misiones:
    print(mision)
print("termino la lista")
separar()

h.heapify(misiones)

separar()
print("Contenido del heap:")
for elem in h.elements:
    print(elem)
separar()
separar()
print("atention")
h.atention()
for elem in h.elements:
    print(elem)

separar()
separar()
print("soy el sort")
h.sort()





# for mision in misiones:
#     #misionparacargar= tuple(mision)
#     prioridad = misiones[mision['nivel_atencion']]
#     print(prioridad)
#     print(mision)
#     print("arriba de esto va la mision")
#     print(mision['nivel_atencion'])
#     #h.arrive(misionparacargar,prioridad)
#     separar()

# separar()
# separar()
# print(h.elements)
# separar()
# separar()


# while len(h.elements)>0:
#     print(h.atention())

from random import randint, choice
from datetime import time
from heap import HeapMax

class Mision:
    def __init__(self, nivel, encargado, descripcion, hora, cant_storm):
        self.nivel = nivel
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.cant_storm = cant_storm

    def __repr__(self):
        return (f"mision(Nivel: {self.nivel}, Encargado: {self.encargado}, "
                f"Descripción: {self.descripcion}, Hora: {self.hora}, "
                f"Cantidad de Storm: {self.cant_storm})")
    
    def __lt__(self, other):
        return self.nivel < other.nivel  
    
def separar ():
    print('-----------------------------------------------------------------------------------------')

misiones = []

h = HeapMax()
listaencargado = ['generales random nivel bajo','capitan phasma','kylo ren','lider supremo Snoke']
listadescripcion = ['ataque','reconocimiento','defensa','revision','limpieza']


for i in range(15):
    nivel = randint(1, 3)
    if nivel == 3:
        encargado = listaencargado[randint(2, 3)]
    else:
        encargado = listaencargado[nivel - 1]

    descripcion = choice(listadescripcion)
    hora = time(randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)

    mision = Mision(nivel, encargado, descripcion, hora, cant_storm)
    # misiones.append(mision)
    h.add(mision)

# for mision in misiones:
#     print(mision)

for element in h.elements:
    print(element)

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


for i in range(8):  # Atender las primeras ocho operaciones
    operacion_atendida = cola.atender()
    if operacion_atendida:
        print(f"Atendiendo: {operacion_atendida}")
        
        # Agregar nueva operación después de la quinta
        if i == 4:
            cola.agregar(Operacion(2, 'Capitán Phasma', 'Revisión de intrusos en el hangar B7', 25))
            print("Se agregó una nueva operación solicitada por Capitán Phasma.")
        
        # Agregar nueva operación después de la sexta
        if i == 5:
            cola.agregar(Operacion(3, 'Líder supremo Snoke', 'Destruir el planeta Takodana', 100))
            print("Se agregó una nueva operación solicitada por el líder supremo Snoke.")



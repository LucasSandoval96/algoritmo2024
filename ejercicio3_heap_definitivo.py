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
    
def separar():
    print('-----------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------')

#El general Hux es la persona encargada de administrar todas las operaciones de la base Starkiller,
#para lo cual nos solicita desarrollar un algoritmo que permita controlar las actividades que se realizan, contemplando lo siguiente:
# a- debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguiente criterio: 
# pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma nivel dos y 
# el resto de las operaciones nivel a cargo de los generales de la base de nivel uno
# b- de cada actividad se conoce quien es el encargado, una descripción, la hora y opcionalmente la cantidad de Stormtroopers requeridos
# c- utilizar una cola de prioridad para administrar las distintas operaciones, 
# debe cargar al menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno
# d- opcionalmente se podrán agregar operaciones luego de atender una

misiones = []
h = HeapMax()
listaencargado = ['generales random nivel bajo', 'capitan phasma', 'kylo ren', 'lider supremo Snoke']
listadescripcion = ['ataque', 'reconocimiento', 'defensa', 'revision', 'limpieza']

separar()
for _ in range(2):
    nivel = 3
    encargado = listaencargado[3]  # lider supremo Snoke
    descripcion = choice(listadescripcion)
    hora = time(randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)
    misiones.append(Mision(nivel, encargado, descripcion, hora, cant_storm))

for _ in range(4):
    nivel = 2
    encargado = listaencargado[2]  # kylo ren
    descripcion = choice(listadescripcion)
    hora = time(randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)
    misiones.append(Mision(nivel, encargado, descripcion, hora, cant_storm))

for _ in range(4):
    nivel = 1
    encargado = listaencargado[0]  # generales random nivel bajo
    descripcion = choice(listadescripcion)
    hora = time(randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)
    misiones.append(Mision(nivel, encargado, descripcion, hora, cant_storm))

# print('Agregar misiones al montículo:')
for mision in misiones:
    h.add(mision)

# for elemnt in h.elements:
#     print(elemnt)

#separar()
#e- realizar la atención de las operaciones de la cola
print('realizando la atención de todas operaciones de la cola: ')

for i in range(len(h.elements)):  
    print(f"Atendiendo misión {i + 1}: {h.atention()}")
    separar()
    
    #f-luego de atender la quinta operación, agregar una operación solicitada por 
    # capitán Phasma para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers
    if i == 4:
        print('Agregar misión solicitada por capitán Phasma')
        nueva_mision = Mision(2, 'capitan phasma', 'revisión de intrusos en el hangar B7', time(randint(0, 23), randint(0, 59)), 25)
        h.add(nueva_mision)
        print("Agregada misión: ",nueva_mision)
        separar()
    
    # g- luego de atender la sexta operación, agregar una operación solicitada 
    # por el líder supremo Snoke para destruir el planeta Takodana.
    if i == 5:
        print('Agregar misión solicitada por líder supremo Snoke')
        nueva_mision = Mision(3, 'lider supremo Snoke', 'destruir el planeta Takodana', time(randint(0, 23), randint(0, 59)), randint(0, 100))
        h.add(nueva_mision)
        print("Agregada misión: ", nueva_mision)
        separar()
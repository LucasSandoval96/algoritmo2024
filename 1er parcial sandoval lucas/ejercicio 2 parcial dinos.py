from pila import Stack
def devolver_pila (pilaprincipal,pila_aux):
    while pila_aux.size()>0:
        pilaprincipal.push(pila_aux.pop())

def copiarlista (pilaprincipal,pila_aux,pilacopia):
    guardo=pilaprincipal.on_top()
    while pilaprincipal()>0:
        pila_aux.push(pilaprincipal.pop())
        pilacopia.push(guardo)

    
def separar():
    print("--------------------------------------------")

class dino:
    def __init__(self, nombre, especie, peso, descubridor, ano_descubrimiento):
        self.nombre = nombre
        self.especie = especie
        self.peso = peso
        self.descubridor = descubridor
        self.ano_descubrimiento = ano_descubrimiento
    
    def __str__(self):
        return f"{self.nombre} - {self.especie} - {self.peso} kg- {self.descubridor} - {self.ano_descubrimiento}"
    
dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso":  7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000 ,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450 ,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

piladinos=Stack()
pila_aux=Stack()
pila_AQS=Stack()

for dinosaurio in dinosaurios:
    piladinos.push(dino(dinosaurio["nombre"],dinosaurio["especie"],dinosaurio["peso"],dinosaurio["descubridor"],dinosaurio["ano_descubrimiento"]))
    print (piladinos.on_top())
separar()
#punto a
c=0
while piladinos.size()>0:
    c+=1
    pila_aux.push(piladinos.pop())
print(f"la cantidad de especies es {c}")
x=devolver_pila(piladinos,pila_aux)
separar()
#punto b

        
#punto c
separar()
while piladinos.size()>0:
    comparacion=piladinos.pop()
    if (comparacion.nombre[0] == "T"):
        print("El dinosaurio empieza con T:",comparacion)
    pila_aux.push(comparacion)
devolver_pila(piladinos,pila_aux)
separar()
#punto d
print("dinosaurios que pesan menos de 275 kg")
while piladinos.size()>0:
    comparacion=piladinos.pop()
    if (comparacion.peso < 275 ):
        print(f"{comparacion.nombre} pesa {comparacion.peso}")
    pila_aux.push(comparacion)
devolver_pila(piladinos,pila_aux)
separar()
#punto e
while piladinos.size()>0:
    comparacion=piladinos.pop()
    if (comparacion.nombre[0] == "A") or (comparacion.nombre[0] == "Q") or (comparacion.nombre[0] == "S"):
        pila_AQS.push(comparacion)
    pila_aux.push(comparacion)
print("los dinosaurios que comienzan con A,Q O S son: ")
while pila_AQS.size()>0:
    print(pila_AQS.pop())

devolver_pila(piladinos,pila_aux)
print


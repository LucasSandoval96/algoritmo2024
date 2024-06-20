from random import choice
from lista import show_list_list, by_name, search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    },
    {
        "nombre": "Tyramtrum",
        "nivel": 66,
        "tipo": "Roca",
        "subtipo": "Dragon"
    },
    {
        "nombre": "Terrakion",
        "nivel": 72,
        "tipo": "Roca",
        "subtipo": "Lucha"
    },
    {
        "nombre": "Wingull",
        "nivel": 10,
        "tipo": "Agua",
        "subtipo": "Volador"
    }
]

def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

def separar():
    print("-------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------")

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')

lista_entrenadores.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)
separar()
#print(entrenadores[0]['sublist'][2]['nivel'])

#punto a
print("obtener la cantidad de pokemon de un determinado entrenador")
buscado="Raihan"
criterio='nombre'
posicion=search(entrenadores,criterio,buscado)
con=0
for i in range (len(entrenadores[posicion]['sublist'])):
    con+=1

print(f'Los cantidad de pokemons de {buscado} son: {con}' )
entrenadores.count(entrenadores[posicion]['sublist'])
separar()
#punto b
print("entrenadores con mas de 3 torneos ganados")
for i in range (len(entrenadores)):
    if entrenadores[i]["torneos_ganados"] > 3:
        print(f"{entrenadores[i]["nombre"]} gano {entrenadores[i]["torneos_ganados"]}")

separar()
#punto c
max=0
for i in range (len(entrenadores)):
    if entrenadores[i]["torneos_ganados"] > max:
        max=entrenadores[i]["torneos_ganados"]
        nombre=entrenadores[i]["nombre"]

criterio='nombre'
posicion=search(entrenadores,criterio,nombre)

maxnivel = 0
for i in range (len(entrenadores[posicion]['sublist'])):
    if entrenadores[posicion]['sublist'][i]['nivel'] > maxnivel:
        maxnivel = entrenadores[posicion]['sublist'][i]['nivel']

print(f"{nombre} es el entrenador con mas torneos ganados: {max} y el nivel mas alto es: {maxnivel}")

separar()
#punto d
buscado="Raihan"
criterio='nombre'
posicion=search(entrenadores,criterio,buscado)
print(f"{entrenadores[posicion]}")
separar()
#punto e
for i in range (len(entrenadores)):
    porcentaje=(entrenadores[i]["batallas_ganadas"]*100)/(entrenadores[i]["batallas_perdidas"] + entrenadores[i]["batallas_ganadas"])
    if porcentaje > 79:
        print(f"{entrenadores[i]["nombre"]} tiene mas de 79% de porcentaje de victoria: {porcentaje}")

separar()
#punto f los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
for i in range (len(entrenadores)):
    for j in range (len(entrenadores[i]['sublist'])):
        if ((entrenadores[i]['sublist'][j]['tipo'] == "Fuego") and (entrenadores[i]['sublist'][j]["subtipo"] == "Planta")) or ((entrenadores[i]['sublist'][j]['tipo'] == "Agua") and (entrenadores[i]['sublist'][j]["subtipo"] == "Volador")):
            print (f"{entrenadores[i]["nombre"]} tiene un {entrenadores[i]['sublist'][j]["nombre"]} tipo {entrenadores[i]['sublist'][j]['tipo']} / {entrenadores[i]['sublist'][j]["subtipo"]}")

separar()
#punto g el promedio de nivel de los Pokémons de un determinado entrenador;
buscado="Raihan"
criterio='nombre'
posicion=search(entrenadores,criterio,buscado)
con=0
levels = 0
for j in range (len(entrenadores[posicion]['sublist'])):
    con+=1
    levels = levels + (entrenadores[posicion]['sublist'][j]['nivel'])
print(f"el promedio de nivel de los pokemon de {buscado} es {(levels/con)}")
separar()
#punto h determinar cuántos entrenadores tienen a un determinado Pokémon;
buscado="Charizard"
for i in range (len(entrenadores)):
    for j in range (len(entrenadores[i]['sublist'])):
        if entrenadores[i]['sublist'][j]['nombre'] == buscado:
            print(f"{entrenadores[i]['nombre']} tiene a {buscado}")
separar()
#punto i mostrar los entrenadores que tienen Pokémons repetidos
listasinrepetir=[]

for i in range (len(entrenadores)):
    for j in range (len(entrenadores[i]['sublist'])):
        if entrenadores[i]['sublist'][j]['nombre'] not in listasinrepetir:
            listasinrepetir.append(entrenadores[i]['sublist'][j]['nombre'])
        con=+1
    print(f"la cantidad de pokemon repetidos de {entrenadores[i]["nombre"]} es {con-len(listasinrepetir)}")
    listasinrepetir.clear

#punto j determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
separar()
criterio='nombre'
for i in range (len(entrenadores)):
    for j in range (len(entrenadores[i]['sublist'])):
        if (entrenadores[i]['sublist'][j][criterio] == "Tyrantrum") or (entrenadores[i]['sublist'][j][criterio] == "Terrakion") or (entrenadores[i]['sublist'][j][criterio] == "Wingull"):
            print(f"{entrenadores[i]['nombre']} tiene a {entrenadores[i]['sublist'][j]['nombre']}")

separar()
#punto k determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
entrenadorbuscado = input("ingrese entrenador a buscar ")
pokemonbuscado = input("ingrese pokemon a buscar ")
separar()
criterio='nombre'
posicion=search(entrenadores,criterio,entrenadorbuscado)
for i in range (len(entrenadores[posicion]['sublist'])):
    if entrenadores[posicion]['sublist'][i][criterio] == pokemonbuscado:
        print(f"{entrenadores[posicion]} {entrenadores[posicion]['sublist'][i]}")

#mayor nivel de cada uno
# buscado="Raihan"
# criterio='nombre'
# posicion=0
# con=0

# for i in range (len(entrenadores)):
#     max=0
#     for j in range (len(entrenadores[i]['sublist'])):
#         if entrenadores[posicion]['sublist'][j]['nivel']>max:
#             max=entrenadores[posicion]['sublist'][j]['nivel']
#             nombrepoke=entrenadores[posicion]['sublist'][j]['nombre']
#     print(f"el pokemon de mayor nivel de {entrenadores[posicion]['nombre']} es {nombrepoke} nivel {max}")
#     posicion+=1

# separar()
# print(f'Los cantidad de pokemons de {buscado} son: {con+1}' )

# separar()
# #punto d

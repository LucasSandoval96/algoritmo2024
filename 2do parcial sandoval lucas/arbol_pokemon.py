# Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre para este 
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
from arbol_avl import BinaryTree
from random import randint


pokemons = [
    {
        "nombre": "Pikachu",
        "tipo": ["Eléctrico"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Charizard",
        "tipo": ["Fuego", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Bulbasaur",
        "tipo": ["Planta", "Veneno"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Starmie",
        "tipo": ["Agua", "Psíquico"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Psyduck",
        "tipo": ["Agua"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Gyarados",
        "tipo": ["Agua", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Onix",
        "tipo": ["Roca", "Tierra"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Geodude",
        "tipo": ["Roca", "Tierra"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Vulpix",
        "tipo": ["Fuego"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Blastoise",
        "tipo": ["Agua"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Umbreon",
        "tipo": ["Siniestro"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Nidoking",
        "tipo": ["Veneno", "Tierra"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Dragonite",
        "tipo": ["Dragón", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Aerodactyl",
        "tipo": ["Roca", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Tyramtrum",
        "tipo": ["Roca", "Dragón"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Kakuna",
        "tipo": ["Bicho", "Veneno"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Vivilon",
        "tipo": ["Bicho", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Slurpuff",
        "tipo": ["Hada"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Roserade",
        "tipo": ["Planta", "Veneno"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Gabyte",
        "tipo": ["Dragón", "Tierra"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Celebi",
        "tipo": ["Psíquico", "Planta"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Vibrava",
        "tipo": ["Tierra", "Dragón"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Oranguru",
        "tipo": ["Normal", "Psíquico"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Ho-oh",
        "tipo": ["Fuego", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Greninja",
        "tipo": ["Agua", "Siniestro"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Froslass",
        "tipo": ["Hielo", "Fantasma"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Surskit",
        "tipo": ["Bicho", "Agua"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Hoothoot",
        "tipo": ["Normal", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Yamask",
        "tipo": ["Fantasma"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Cosmog",
        "tipo": ["Psíquico"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Marril",
        "tipo": ["Agua", "Hada"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Arceus",
        "tipo": ["Normal"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Rampados",
        "tipo": ["Roca"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Toxapex",
        "tipo": ["Veneno", "Agua"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Electabuzz",
        "tipo": ["Eléctrico"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Terrakion",
        "tipo": ["Roca", "Lucha"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Wingull",
        "tipo": ["Agua", "Volador"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Jolteon",
        "tipo": ["Eléctrico"],
        "numero": randint(1,1300)
    },
    {
        "nombre": "Lycanroc",
        "tipo": ["Roca"],
        "numero": randint(1,1300)
    },
]

def separar():
    print('------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------')

treenombre = BinaryTree()
treetipo = BinaryTree()
treeid = BinaryTree()


# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
separar()

for pokemon in pokemons:
    treenombre.insert_node(pokemon['nombre'], pokemon)
    treetipo.insert_node(pokemon['tipo'], pokemon)
    treeid.insert_node(pokemon['numero'], pokemon)

# treenombre.preorden()
# separar()
# treenombre.inorden()
# separar()
# treenombre.postorden()

separar()

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre para este 
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres
print("punto b")
pos= treenombre.proximity_search_allinfo('G')
if pos is not None:
  print('Encontrado:', pos)

separar()
separar()

#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico
# no lo pude realizar, probe muchas formas
buscado="Agua"
treetipo.mostrarpor(buscado)
buscado="Fuego"
treetipo.mostrarpor(buscado)
buscado="Planta"
treetipo.mostrarpor("Planta")
buscado="Eléctrico"
treetipo.mostrarpor("Eléctrico")


# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("listado en orden ascendente por número: ")
treeid.inorden_datoscompletos()
separar()
print("listado en orden por nombre de Pokémon")
treenombre.inorden()
separar()
print("listado por nivel de nombre:")
treenombre.by_level()

separar()
#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyramtrum

print("El buscado es: Jolteon")
pos= treenombre.search("Jolteon")
if pos is not None:
    print("se encontro los datos de : ",pos.other_value)

print("El buscado es: Lycanro")
pos= treenombre.search("Lycanroc")
if pos is not None:
    print("se encontro los datos de : ",pos.other_value)

print("El buscado es: Tyramtrum")
pos= treenombre.search("Tyramtrum")
if pos is not None:
    print("se encontro los datos de : ",pos.other_value)

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
print('Cantidad de pokemon de tipo Eléctrico: ')
cantidad = treetipo.contar_tipo_inorden('Eléctrico')
print(cantidad)   

print('Cantidad de pokemon de tipo Acero: ')
cantidad = treetipo.contar_tipo_inorden('Acero')
print(cantidad) 
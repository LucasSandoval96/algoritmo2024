# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 
# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

from random import randint

class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos  # Lista de tipos
        self.nivel = nivel

    def __repr__(self):
        return f"Pokemon({self.numero}, {self.nombre}, {self.tipos}, {self.nivel})"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_tipo(self, tipo):
        return hash(tipo) % self.size

    def hash_numero(self, numero):
        return int(str(numero)[-1]) % self.size

    def hash_nivel(self, nivel):
        return nivel % self.size

    def insert(self, pokemon):
        # Insertar por tipo
        for tipo in pokemon.tipos:
            index = self.hash_tipo(tipo)
            self.table[index].append(pokemon)

        # Insertar por último dígito del número
        index = self.hash_numero(pokemon.numero)
        self.table[index].append(pokemon)

        # Insertar por nivel
        index = self.hash_nivel(pokemon.nivel)
        self.table[index].append(pokemon)

    # def mostrar_pokemons_por_numero(self, numeros):
    #     result = []
    #     for num in numeros:
    #         index = self.hash_numero(num)
    #         result.extend(self.table[index])
    #     return result

    # def mostrar_pokemons_por_nivel(self, niveles):
    #     result = []
    #     for nivel in niveles:
    #         index = self.hash_nivel(nivel)
    #         result.extend(self.table[index])
    #     return result
    
    # def mostrar_pokemons_por_tipos(self, tipos):
    #     result = []
    #     for tipo in tipos:
    #         index = self.hash_tipo(tipo)
    #         result.extend(self.table[index])
    #     print()
    #     return list(set(result))  

    def mostrar_pokemons_por_numero(self, numeros):
        for num in numeros:
            index = self.hash_numero(num)
            for pokemon in self.table[index]:
                print(pokemon)

    def mostrar_pokemons_por_nivel(self, niveles):
        for nivel in niveles:
            index = self.hash_nivel(nivel)
            for pokemon in self.table[index]:
                print(pokemon)

    def mostrar_pokemons_por_tipos(self, tipos):
        result = []
        for tipo in tipos:
            index = self.hash_tipo(tipo)
            for pokemon in self.table[index]:
                result.append(pokemon)
        # Eliminar duplicados
        result = list(set(result))
        for pokemon in result:
            print(pokemon)
    
def separar():
    print('------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------')

# pokemons = [
#     {
#         "nombre": "Pikachu",
#         "tipo": ["Eléctrico"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Charizard",
#         "tipo": ["Fuego", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Bulbasaur",
#         "tipo": ["Planta", "Veneno"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Starmie",
#         "tipo": ["Agua", "Psíquico"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Psyduck",
#         "tipo": ["Agua"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Gyarados",
#         "tipo": ["Agua", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Onix",
#         "tipo": ["Roca", "Tierra"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Geodude",
#         "tipo": ["Roca", "Tierra"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Vulpix",
#         "tipo": ["Fuego"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Blastoise",
#         "tipo": ["Agua"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Umbreon",
#         "tipo": ["Siniestro"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Nidoking",
#         "tipo": ["Veneno", "Tierra"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Dragonite",
#         "tipo": ["Dragón", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Aerodactyl",
#         "tipo": ["Roca", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Tyramtrum",
#         "tipo": ["Roca", "Dragón"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Kakuna",
#         "tipo": ["Bicho", "Veneno"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Vivilon",
#         "tipo": ["Bicho", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Slurpuff",
#         "tipo": ["Hada"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Roserade",
#         "tipo": ["Planta", "Veneno"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Gabyte",
#         "tipo": ["Dragón", "Tierra"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Celebi",
#         "tipo": ["Psíquico", "Planta"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Vibrava",
#         "tipo": ["Tierra", "Dragón"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Oranguru",
#         "tipo": ["Normal", "Psíquico"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Ho-oh",
#         "tipo": ["Fuego", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Greninja",
#         "tipo": ["Agua", "Siniestro"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Froslass",
#         "tipo": ["Hielo", "Fantasma"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Surskit",
#         "tipo": ["Bicho", "Agua"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Hoothoot",
#         "tipo": ["Normal", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Yamask",
#         "tipo": ["Fantasma"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Cosmog",
#         "tipo": ["Psíquico"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Marril",
#         "tipo": ["Agua", "Hada"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Arceus",
#         "tipo": ["Normal"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Rampados",
#         "tipo": ["Roca"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Toxapex",
#         "tipo": ["Veneno", "Agua"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Electabuzz",
#         "tipo": ["Eléctrico"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Terrakion",
#         "tipo": ["Roca", "Lucha"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Wingull",
#         "tipo": ["Agua", "Volador"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Jolteon",
#         "tipo": ["Eléctrico"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Lycanroc",
#         "tipo": ["Roca"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Registeel",
#         "tipo": ["Acero"],
#         "numero": randint(1,1300)
#     },
#     {
#         "nombre": "Aggron",
#         "tipo": ["Acero","Roca"],
#         "numero": randint(1,1300)
#     },
# ]


pokemons = [
    Pokemon(numero=randint(1,1300), nombre="Pikachu", tipos=["Eléctrico"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Charizard", tipos=["Fuego", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Bulbasaur", tipos=["Planta", "Veneno"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Starmie", tipos=["Agua", "Psíquico"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Psyduck", tipos=["Agua"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Gyarados", tipos=["Agua", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Onix", tipos=["Roca", "Tierra"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Geodude", tipos=["Roca", "Tierra"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Vulpix", tipos=["Fuego"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Blastoise", tipos=["Agua"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Umbreon", tipos=["Siniestro"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Nidoking", tipos=["Veneno", "Tierra"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Dragonite", tipos=["Dragón", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Aerodactyl", tipos=["Roca", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Tyrantrum", tipos=["Roca", "Dragón"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Kakuna", tipos=["Bicho", "Veneno"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Vivillon", tipos=["Bicho", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Slurpuff", tipos=["Hada"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Roserade", tipos=["Planta", "Veneno"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Gabite", tipos=["Dragón", "Tierra"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Celebi", tipos=["Psíquico", "Planta"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Vibrava", tipos=["Tierra", "Dragón"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Oranguru", tipos=["Normal", "Psíquico"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Ho-oh", tipos=["Fuego", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Greninja", tipos=["Agua", "Siniestro"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Froslass", tipos=["Hielo", "Fantasma"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Surskit", tipos=["Bicho", "Agua"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Hoothoot", tipos=["Normal", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Yamask", tipos=["Fantasma"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Cosmog", tipos=["Psíquico"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Marill", tipos=["Agua", "Hada"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Arceus", tipos=["Normal"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Rampardos", tipos=["Roca"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Toxapex", tipos=["Veneno", "Agua"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Electabuzz", tipos=["Eléctrico"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Terrakion", tipos=["Roca", "Lucha"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Wingull", tipos=["Agua", "Volador"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Jolteon", tipos=["Eléctrico"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Lycanroc", tipos=["Roca"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Registeel", tipos=["Acero"], nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Aggron", tipos=["Acero", "Roca"], nivel=randint(1,100)),
]



# for pokemon in pokemons:
#     pokemon["nivel"] = randint(1, 100)

# con=0
# for pokemon in pokemons:
#     print(pokemon)
#     con+=1

# print("contador:",con)



# for i in range(0, 2000):
#     trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
#     clave = hash_numerica(trooper)
#     if clave not in table_numerica:
#         table_numerica[clave] = []

#     table_numerica[clave].append(trooper)
#     tabla_legiones[hash_legion(trooper)].append(trooper)


# Inicializamos las tablas hash
tabla_hash = HashTable(50)

# Agregar Pokémons
# pokemons = [
#     Pokemon(numero=1, nombre="Bulbasaur", tipos=["Planta", "Veneno"], nivel=16),
#     Pokemon(numero=2, nombre="Ivysaur", tipos=["Planta", "Veneno"], nivel=32),
#     Pokemon(numero=3, nombre="Venusaur", tipos=["Planta", "Veneno"], nivel=64),
#     Pokemon(numero=4, nombre="Charmander", tipos=["Fuego"], nivel=16),
#     Pokemon(numero=5, nombre="Charmeleon", tipos=["Fuego"], nivel=36),
#     Pokemon(numero=6, nombre="Charizard", tipos=["Fuego", "Volador"], nivel=100),
#     Pokemon(numero=7, nombre="Squirtle", tipos=["Agua"], nivel=16),
#     Pokemon(numero=8, nombre="Wartortle", tipos=["Agua"], nivel=36),
#     Pokemon(numero=9, nombre="Blastoise", tipos=["Agua"], nivel=100),
#     Pokemon(numero=10, nombre="Caterpie", tipos=["Bicho"], nivel=10)
# ]

# for pokemon in pokemons:
#     tabla_hash.insert(pokemon)

# # Mostrar Pokémons cuyos números terminan en 3, 7 y 9
# numeros_a_buscar = [3, 7, 9]
# pokemons_con_numeros = tabla_hash.mostrar_pokemons_por_numero(numeros_a_buscar)
# print("Pokémons cuyos números terminan en 3, 7 y 9:")
# print(pokemons_con_numeros)

# # Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10
# niveles_a_buscar = [2, 5, 10]
# pokemons_con_niveles = []
# for nivel in range(1, 101):
#     if nivel % 2 == 0 or nivel % 5 == 0 or nivel % 10 == 0:
#         pokemons_con_niveles.append(nivel)

# pokemons_multiplos = tabla_hash.mostrar_pokemons_por_nivel(pokemons_con_niveles)
# print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
# print(pokemons_multiplos)



for pokemon in pokemons:
    tabla_hash.insert(pokemon)
separar()
print("Pokémons cuyos números terminan en 3, 7 y 9:")
# Mostrar Pokémons cuyos números terminan en 3, 7 y 9
numeros_a_buscar = [3, 7, 9]
pokemons_con_numeros = tabla_hash.mostrar_pokemons_por_numero(numeros_a_buscar)

separar()
print("Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10")
# Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10
niveles_a_buscar = []
for nivel in range(1, 101):
    if nivel % 2 == 0 or nivel % 5 == 0 or nivel % 10 == 0:
        niveles_a_buscar.append(nivel)

pokemons_multiplos = tabla_hash.mostrar_pokemons_por_nivel(niveles_a_buscar)

separar()
print("mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo")
tipos_a_buscar = ["Acero", "Fuego", "Eléctrico", "Hielo"]
pokemons_por_tipos = tabla_hash.mostrar_pokemons_por_tipos(tipos_a_buscar)


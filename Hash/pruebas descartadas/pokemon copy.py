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

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Tabla hash abierta

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, pokemon):
        index = self.hash_function(key)
        self.table[index].append(pokemon)

    def display(self):
        for index, pokemons in enumerate(self.table):
            if pokemons:
                print(f"Índice {index}: {[pokemon.nombre for pokemon in pokemons]}")

class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos.split('/')  # Soportar múltiples tipos
        self.nivel = nivel

class Pokedex:
    def __init__(self):
        self.tipo_table = HashTable(10)  # Tabla hash por tipo
        self.numero_table = HashTable(10)  # Tabla hash por último dígito del número
        self.nivel_table = HashTable(10)  # Tabla hash por nivel

    def add_pokemon(self, pokemon):
        # Cargar en la tabla por tipo
        for tipo in pokemon.tipos:
            self.tipo_table.insert(hash(tipo), pokemon)

        # Cargar en la tabla por último dígito del número
        self.numero_table.insert(pokemon.numero % 10, pokemon)

        # Cargar en la tabla por nivel
        self.nivel_table.insert(pokemon.nivel // 10, pokemon)

    def show_pokemons_ending_in(self, digits):
        print(f"Pokémons cuyos números terminan en {digits}:")
        for digit in digits:
            for pokemon in self.numero_table.table[digit]:
                print(f"- {pokemon.nombre} (Número: {pokemon.numero})")

    def show_pokemons_multiples_of(self):
        print("Pokémons cuyos niveles son múltiplos de:", 2, 5, 10)
        for index in range(len(self.nivel_table.table)):
            if index * 10 % 2 == 0 or index * 10 % 5 == 0 or index * 10 % 10 == 0:
                for pokemon in self.nivel_table.table[index]:
                    print(f"- {pokemon.nombre} (Nivel: {pokemon.nivel})")

    def show_pokemons_by_type(self, types):
        print(f"Pokémons de los tipos: {types}")
        for tipo in types:
            for pokemon in self.tipo_table.table[hash(tipo) % self.tipo_table.size]:
                if tipo in pokemon.tipos:
                    print(f"- {pokemon.nombre} (Tipo: {pokemon.tipos})")
    
def separar():
    print('------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------')


pokemons = [
    Pokemon(numero=randint(1,1300), nombre="Pikachu", tipos="Eléctrico", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Charizard", tipos="Fuego/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Bulbasaur", tipos="Planta/Veneno", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Starmie", tipos="Agua/Psíquico", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Psyduck", tipos="Agua", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Gyarados", tipos="Agua/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Onix", tipos="Roca/Tierra", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Geodude", tipos="Roca/Tierra", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Vulpix", tipos="Fuego", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Blastoise", tipos="Agua", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Umbreon", tipos="Siniestro", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Nidoking", tipos="Veneno/Tierra", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Dragonite", tipos="Dragón/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Aerodactyl", tipos="Roca/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Tyrantrum", tipos="Roca/Dragón", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Kakuna", tipos="Bicho/Veneno", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Vivillon", tipos="Bicho/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Slurpuff", tipos="Hada", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Roserade", tipos="Planta/Veneno", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Gabite", tipos="Dragón/Tierra", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Celebi", tipos="Psíquico/Planta", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Vibrava", tipos="Tierra/Dragón", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Oranguru", tipos="Normal/Psíquico", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Ho-oh", tipos="Fuego/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Greninja", tipos="Agua/Siniestro", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Froslass", tipos="Hielo/Fantasma", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Surskit", tipos="Bicho/Agua", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Hoothoot", tipos="Normal/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Yamask", tipos="Fantasma", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Cosmog", tipos="Psíquico", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Marill", tipos="Agua/Hada", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Arceus", tipos="Normal", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Rampardos", tipos="Roca", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Toxapex", tipos="Veneno/Agua", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Electabuzz", tipos="Eléctrico", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Terrakion", tipos="Roca/Lucha", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Wingull", tipos="Agua/Volador", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Jolteon", tipos="Eléctrico", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Lycanroc", tipos="Roca", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Registeel", tipos="Acero", nivel=randint(1,100)),
    Pokemon(numero=randint(1,1300), nombre="Aggron", tipos="Acero/Roca", nivel=randint(1,100)),
]

# Crear la Pokedex
pokedex = Pokedex()

for pokemon in pokemons:
    pokedex.add_pokemon(pokemon)

# Mostrar Pokémons cuyos números terminan en 3, 7 y 9
pokedex.show_pokemons_ending_in([3, 7, 9])

# Mostrar Pokémons cuyos niveles son múltiplos de 2, 5 y 10
pokedex.show_pokemons_multiples_of()

# Mostrar Pokémons de los tipos: Acero, Fuego, Electrifico, Hielo
pokedex.show_pokemons_by_type(["Acero", "Fuego", "Eléctrico", "Hielo"])

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
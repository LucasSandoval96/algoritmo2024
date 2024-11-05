class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero         
        self.nombre = nombre         
        self.tipos = tipos           
        self.nivel = nivel           

def agregar_poke(pokemon):
    # Tabla hash por tipo
    for tipo in pokemon.tipos:
        if tipo not in hash_tipo:
            hash_tipo[tipo] = []
        hash_tipo[tipo].append(pokemon)

    # Tabla hash por último dígito
    ultimo_digito = pokemon.numero % 10
    hash_digito[ultimo_digito].append(pokemon)

    # Tabla hash por nivel
    nivel_index = pokemon.nivel // 10
    if nivel_index < 10:  
        hash_nivel[nivel_index].append(pokemon)

def pokescondigito3_7_9():
    for i in range(10):
        for pokemon in hash_digito[i]:
            if i in [3, 7, 9]:
                print(pokemon.nombre)

def pokesmultiplos():
    for nivel_lista in hash_nivel:
        for pokemon in nivel_lista:
            if pokemon.nivel % 2 == 0 or pokemon.nivel % 5 == 0 or pokemon.nivel % 10 == 0:
                print(pokemon.nombre)

def pokestiposespec(tipos):
    for tipo in tipos:
        if tipo in hash_tipo:
            for pokemon in hash_tipo[tipo]:
                print(pokemon.nombre)

def separar():
    print('------------------------------------------------------------------------------')
    print('------------------------------------------------------------------------------')

hash_tipo = {}     
hash_digito = [[] for _ in range(10)]  
hash_nivel = [[] for _ in range(10)]    

pokemon1 = Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], 5)
pokemon2 = Pokemon(71, "Ivysaur", ["Planta", "Veneno"], 15)
pokemon3 = Pokemon(3, "Charmander", ["Fuego"], 9)
pokemon4 = Pokemon(3, "Squirtle", ["Agua"], 10)
pokemon5 = Pokemon(7, "Pidgey", ["Normal", "Volador"], 13)
pokemon6 = Pokemon(2, "Steelix", ["Acero", "Tierra"], 30)
pokemon7 = Pokemon(87, "Gengar",["fantasma","Veneno"],90)
pokemon8 = Pokemon(59, "Electabuzz",["Electrifico"],14)
pokemon9 = Pokemon(27, "Mamoswine",["Hielo","Tierra"],13)

agregar_poke(pokemon1)
agregar_poke(pokemon2)
agregar_poke(pokemon3)
agregar_poke(pokemon4)
agregar_poke(pokemon5)
agregar_poke(pokemon6)
agregar_poke(pokemon7)
agregar_poke(pokemon8)
agregar_poke(pokemon9)

separar()
print("Pokémons cuyos números terminan en 3, 7 y 9:")
pokescondigito3_7_9()

separar()
print("Pokémons cuyos niveles son múltiplos de 2, 5 y 10:")
pokesmultiplos()

separar()
print("Pokémons de tipos específicos (Acero, Fuego, Electrifico, Hielo):")
pokestiposespec(["Acero", "Fuego", "Electrifico", "Hielo"])
separar()
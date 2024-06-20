super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "DC Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]

def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)
    
def search(list_values, criterio, value):
    for index, element in enumerate(list_values):
        if element[criterio] == value:
            return index

for i in range(len(super_heroes)):
    if 'traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']:
        print(i, super_heroes[i]['nombre'], super_heroes[i]['biografia'])

print("--------------------------------------------")
print("Listado")
for elemento in super_heroes:
    print(elemento)
print("--------------------------------------------")
buscado="Linterna Verde"
criterio='nombre'
print("eliminar linterna verde:")
remove(super_heroes,criterio,buscado)

for elemento in super_heroes:
    print(elemento)
print("--------------------------------------------")
buscado="Wolverine"
criterio='nombre'
posicion=search(super_heroes,criterio,buscado)
print(f'el año de aparicion de {buscado} es {super_heroes[posicion]["año_aparicion"]}' )
print("--------------------------------------------")
buscado="Doctor Strange"
criterio='nombre'
posicion=search(super_heroes,criterio,buscado)
super_heroes[posicion]["casa_comic"] = "Marvel Comics"
print(super_heroes[posicion])
print("--------------------------------------------")
print("super heroes que contengan traje o armadura en su descripcion")
for i in range(len(super_heroes)):
    if 'traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']:
        print(i, super_heroes[i]['nombre'], super_heroes[i]['biografia'])
print("--------------------------------------------")
print("super heroes con fecha de aparicion mayor a 1963")
for i in range(len(super_heroes)):
    if super_heroes[i]["año_aparicion"] > 1963:
        print(f'{super_heroes[i]['nombre']} aparecio en {super_heroes[i]["año_aparicion"]}')
print("--------------------------------------------")
buscado="Capitana Marvel"
criterio='nombre'
posicion=search(super_heroes,criterio,buscado)
print(f"{buscado} pertenece a {super_heroes[posicion]["casa_comic"]}")
buscado="Mujer Maravilla"
criterio='nombre'
posicion=search(super_heroes,criterio,buscado)
print(f"{buscado} pertenece a {super_heroes[posicion]["casa_comic"]}")
print("--------------------------------------------")
buscado="Flash"
criterio='nombre'
posicion=search(super_heroes,criterio,buscado)
print(super_heroes[posicion])
buscado="Star-Lord"
criterio='nombre'
posicion=search(super_heroes,criterio,buscado)
print(super_heroes[posicion])
print("--------------------------------------------")
#listar los superhéroes que comienzan con la letra B, M y S
print("nombres que comienzan con B,M O S")
for superheroe in range (len(super_heroes)):
    if super_heroes[superheroe]["nombre"][0] == "B" or super_heroes[superheroe]["nombre"][0] == "M" or super_heroes[superheroe]["nombre"][0] == "S":
        print(super_heroes[superheroe])

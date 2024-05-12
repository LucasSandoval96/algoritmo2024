mochila_jedi=["sanguchito","blaster","mate","gameboy","sable de luz","llaves de tu nave"]

def contador(vector,buscado,con):
    if con==len(vector):
        return -1
    elif vector[con] == buscado:
        return con+1
    else:
        con=con+1
        return contador(vector,buscado,con)

def usar_lafuerza(vector,buscado):
    if vector[0]==buscado:
        print ("encontraste el sable de luz, que la fuerza te acompañe")
    else:
        print("sacaste un: ",vector[0])
        print()
        usar_lafuerza(vector[1:],buscado)

c= 0
buscado= "sable de luz"
x= contador(mochila_jedi,buscado,c)
if x==-1:
    print("el lado oscuro robo tu sable de luz, no se encuentra en tu mochila")
else:
    print("el sable de luz esta en la posicion:", x)
print()
y= usar_lafuerza(mochila_jedi,buscado)
print()


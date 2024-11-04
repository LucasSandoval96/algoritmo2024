class Stack:

    def __init__(self): #inicializar
        self.__elements = []

    def push(self, element): 
        self.__elements.append(element)

    def pop(self): #saca el ultimo
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):#muestra el que esta arriba de todo
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self): #tamaño
        return len(self.__elements)
    




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def show(self):
        print(f"Data = {self.data}")      
        print(f"Next = {self.next}")


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_last(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at(self,data,position):
        if (position == 0):
            self.insert_first(data)
        elif (position == self.size):
            self.insert_last(data)
        elif (position > self.size):
            print("the data can´t be inserted")
        else:
            previous = self.head
            k=0
            while k < position-1:
                previous = previous.next
            new_node = Node(data)
            new_node.next = previous.next
            previous.next = new_node
            self.size += 1

    def show_list(self):
        # print(f"Head = {self.head} --- Tail = {self.tail} --- Size = {self.size}")
        # print("Nodes: ")
        current = self.head
        while current is not None:
            print("*********")
            print(f"Titulo: {current.data[0]}\n Artista: {current.data[1]}\n Año: {current.data[2]}\n Genero: {current.data[3]}")
            current = current.next

new_list = Linked_list()

while True:
    print("\n-menu-nuevo-")
    print("1. Insertar cancion")
    print("2. Buscar cancion")
    print("3. Mostrar canciones")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Insertar cancion")
        titulo = input("Inserte el titulo de la cancion: ")
        artista = input("Inserte el nombre del artista: ")
        anio = input("Inserte el año de la canción: ")
        genero = input("Inserte el genero: ")
        new_list.insert_last([titulo, artista, anio, genero])
    elif opcion == "2":
        print("Buscar cancion")
    elif opcion == "3":
        print("Mostrar canciones")
        new_list.show_list()
    elif opcion == "4":
        print("Programa terminado")
        break
    else:
        print("Opcion no valida")
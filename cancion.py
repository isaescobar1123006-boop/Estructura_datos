class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at(self, data, position):
        if position < 0 or position > self.size:
            print("La posicion no es valida")
            return

        if position == 0:
            self.insert_first(data)
            return

        if position == self.size:
            self.insert_last(data)
            return

        previous = self.head
        k = 0
        while k < position - 1:
            previous = previous.next
            k += 1

        new_node = Node(data)
        new_node.next = previous.next
        previous.next = new_node
        self.size += 1

    def search_song(self, titulo):
        if self.head is None:
            print("La lista esta vacia")
            return False

        current = self.head
        position = 0
        matches = []
        busqueda = titulo.lower()

        while current is not None:
            titulo_actual = current.data[0].lower()
            artista_actual = current.data[1].lower()

            if titulo_actual == busqueda:
                print("*********")
                print(f"Cancion encontrada en posicion {position}")
                print(f"Titulo: {current.data[0]}\nArtista: {current.data[1]}\nAño: {current.data[2]}\nGenero: {current.data[3]}")
                print("*********")
                return True

            if artista_actual == busqueda:
                matches.append(current)

            current = current.next
            position += 1

        if matches:
            print(f"Se encontraron {len(matches)} canciones del artista '{titulo}':")
            for song in matches:
                print("*********")
                print(f"Titulo: {song.data[0]}\nArtista: {song.data[1]}\nAño: {song.data[2]}\nGenero: {song.data[3]}")
                print("*********")
            return True

        print(f"La cancion o artista '{titulo}' no fue encontrado")
        return False

    def delete_at(self, position):
        if self.head is None:
            print("La lista esta vacia")
            return

        if position < 0 or position >= self.size:
            print("La posicion no es valida")
            return

        if position == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            print("Cancion eliminada correctamente")
            return

        previous = self.head
        k = 0
        while k < position - 1:
            previous = previous.next
            k += 1

        current = previous.next
        previous.next = current.next

        if current == self.tail:
            self.tail = previous

        self.size -= 1
        print("Cancion eliminada correctamente")

    def delete_song(self, titulo):
        if self.head is None:
            print("La lista esta vacia")
            return

        titulo_busqueda = titulo.lower()

        if self.head.data[0].lower() == titulo_busqueda:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            print(f"Cancion '{titulo}' eliminada correctamente")
            return

        current = self.head
        previous = None
        found = False

        while current is not None:
            if current.data[0].lower() == titulo_busqueda:
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                self.size -= 1
                print(f"Cancion '{titulo}' eliminada correctamente")
                found = True
                break
            previous = current
            current = current.next

        if not found:
            print(f"La cancion '{titulo}' no fue encontrada")

    def show_list(self):
        if self.head is None:
            print("La lista esta vacia")
            return

        current = self.head
        while current is not None:
            print("*********")
            print(f"Titulo: {current.data[0]}\nArtista: {current.data[1]}\nAño: {current.data[2]}\nGenero: {current.data[3]}")
            current = current.next


new_list = Linked_list()

while True:
    print("\n-menu-nuevo-")
    print("1. Insertar cancion")
    print("2. Buscar cancion")
    print("3. Mostrar canciones")
    print("4. Eliminar cancion")
    print("5. Salir")

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
        titulo = input("Ingrese el titulo o el nombre del artista a buscar: ")
        new_list.search_song(titulo)

    elif opcion == "3":
        print("Mostrar canciones")
        new_list.show_list()

    elif opcion == "4":
        print("Eliminar cancion")
        titulo = input("Ingrese el titulo de la cancion a eliminar: ")
        new_list.delete_song(titulo)

    elif opcion == "5":
        print("Programa terminado")
        break

    else:
        print("Opcion no valida")

class Libro:
    def __init__(self, id:str, title:str, gender:str, isbn:str, editorial:str, author:list[str]):
        self.__id = id
        self.title = title
        self.gender = gender
        self.isbn = isbn
        self.editorial = editorial
        self.author = author

def convert_author_to_list(author: str):
    word = ""
    list_author = []

    for i in author:
        if i == ',':
            list_author.append(word)
            word=""
            continue
        word += i
    list_author.append(word)

    return list_author

validation = True

while(validation):
    print(
    """
        Opción 1: Leer archivo.
        Opción 2: Listar libros.
        Opción 3: Agregar libros.
        Opción 4: Eliminar libro.
        Opción 5: Buscar libros.
        Opción 6: Ordenar libros por título.
        Opción 7: Editar datos de un libro.
        Opción 8: Guardar libro.
        Opción 9: Salir.
    """)

    option = input("Ingresar el número de opción a realizar: ")
    while option not in ('1','2','3','4','5','6','7','8', '9'):
        print(
    """
        Opción 1: Leer archivo.
        Opción 2: Listar libros.
        Opción 3: Agregar libros.
        Opción 4: Eliminar libro.
        Opción 5: Buscar libros.
        Opción 6: Ordenar libros por título.
        Opción 7: Editar datos de un libro.
        Opción 8: Guardar libro.
        Opción 9: Salir.
    """)
        option = input("Opción Incorrecta. Ingresar nuevamente el número de opción a realizar: ")
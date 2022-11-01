import pandas as pd

class Libro:
    def __init__(self, id:str, title:str, gender:str, isbn:str, editorial:str, author:list[str]):
        self.__id = id
        self.title = title
        self.gender = gender
        self.isbn = isbn
        self.editorial = editorial
        self.author = author
    
    def list_books(self):
        show = f"""
        Title: 
                {self.title}

        Gender:
                {self.gender}

        ISBN:
                {self.isbn}

        Editorial:
                {self.editorial}

        Author(s):"""

        for i in self.author:
            show += "\n" + " "*16 + f"{i}"

        return show + "\n"

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

file_name = ""
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

    if option == '1':
        file_name = input("\nIngresar el nombre del archivo a leer [.csv]: ")
        while True:
            try:
                file = pd.read_csv(file_name + ".csv")
            except:
                file_name = input("\nNo se encontró el archivo. Ingresar un nombre de archivo a leer nuevamente [.csv]: ")
            else: break
        print("\nArchivo subido.")

    if option == '2':
        try:
            file = pd.read_csv(file_name + ".csv")
        except:
            print("\nNo se ha subido el archivo.")
        else:
            for i in range(file['Id'].count()):
                obj = Libro(file['Id'][i],file['Title'][i],file['Gender'][i],file['ISBN'][i],file['Editorial'][i],convert_author_to_list(file['Author(s)'][i]))
                print(obj.list_books())
            print("Listado completo.")
    
    if option == '9':
        validation = False
        print("\nSe cerró correctamente.\n")

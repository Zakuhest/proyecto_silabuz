from csv import *

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
                with open(file_name+".csv") as file:
                    newFile = reader(file)
                    data = [i for i in newFile]
                    print("\nArchivo subido.")
            except:
                file_name = input("\nNo se encontró el archivo. Ingresar un nombre de archivo a leer nuevamente [.csv]: ")
            else:
                break
    elif option == '2':
        try: 
            with open(file_name+".csv") as file:
                newFile = reader(file)
                data = [i for i in newFile]
                rows = [data[r] for r in range(1,len(data))]
        except:
            print("\nNo se ha subido el archivo.")
        else:
            for i in range(len(rows)):
                obj = Libro(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],convert_author_to_list(rows[i][5]))
                print(obj.list_books())
            print("Listado completo.")
    elif option == '3':
        try:
            with open(file_name+".csv", 'a', newline='\n') as file:
                Id = input("\nID: ").upper()
                title = input("Title: ").capitalize()
                gender = input("Gender: ").capitalize()
                isbn = input("ISBN: ")
                editorial = input("Editorial: ").title()
                author = input("Author(s): ").title()
                add_list = [Id, title, gender, isbn, editorial, author]
                
                add = writer(file)
                add.writerow(add_list)
                file.close()
        except:
            print("\nNo se ha subido el archivo.")
        else:
            print("\nAñadido correctamente.")

    elif option == '4':
        try:
            with open(file_name+".csv") as file:
                newFile = reader(file)
                data = [i for i in newFile]
            
            with open(file_name+".csv", "w", newline='') as file:
                Id = input("\nID: ").upper()
                new = writer(file)
                for r in data:
                    for c in r:
                        if c != Id:
                            new.writerow(r)
                        break
                file.close()
        except:
            print("\nNo se ha subido el archivo.")
        else:
            print("\nEliminado correctamente.")
    elif option == '5':
        pass
    elif option == '6':
        pass
    elif option == '7':
        pass
    elif option == '8':
        pass
    elif option == '9':
        validation = False
        print("\nSe cerró correctamente.\n")

from csv import *
import csv
# Creacion de clase libro y sus atributos
class Libro:
    def __init__(self, id:str, title:str, gender:str, isbn:str, editorial:str, author:list[str]):
        self.__id = id
        self.title = title
        self.gender = gender
        self.isbn = isbn
        self.editorial = editorial
        self.author = author
    
    # Funcion para listar libros
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

# Funcion para convertir valores de la columna autores a lista
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

# Declaracion de variable que valide entrada y salida al bucle while
validation = True

while(validation):
    # Estructura del menú interactivo
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
    # En caso sea ingresada una opcion incorrecta
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

    # Funcionalidad para las opciones
    if option == '1':
        file_name = input("\nIngresar el nombre del archivo a leer [.csv]: ")
        while True:
            # Capturando excepcion en caso no se encuentre el archivo
            try: 
                # Carga de archivo csv
                with open(file_name+".csv") as file:
                    newFile = reader(file)
                    data = [i for i in newFile]
                    print("\nArchivo subido.")
            except:
                file_name = input("\nNo se encontró el archivo. Ingresar un nombre de archivo a leer nuevamente [.csv]: ")
            else:
                break
    elif option == '2':
        # Capturando excepcion en caso no se encuentre el archivo subido
        try:
            # Carga actualizada del csv
            with open(file_name+".csv") as file:
                newFile = reader(file)
                data = [i for i in newFile]
                rows = [data[r] for r in range(1,len(data))]
        except:
            print("\nNo se ha subido el archivo.")
        else:
            # Recorre las filas del csv
            for i in range(len(rows)):
                # Instancia de clase Libro
                obj = Libro(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],convert_author_to_list(rows[i][5]))
                # Llamada a funcion listar libros, mediante instancia
                print(obj.list_books())
            print("Listado completo.")
    elif option == '3':
        # Capturando excepcion en caso no se encuentre el archivo subido
        try:
            # Carga actualizada del csv, con modo 'a' (add) y con un salto de línea se genera una nueva línea
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
        # Capturando excepcion en caso no se encuentre el archivo subido
        try:
            # Carga actualizada del csv
            with open(file_name+".csv") as file:
                newFile = reader(file)
                data = [i for i in newFile]
            # Sobreescritura del csv, con modo 'w' (write)
            with open(file_name+".csv", "w", newline='') as file:
                Id = input("\nID: ").upper()
                new = writer(file)
                for r in data:
                    for c in r:
                        if c != Id: # Si el identificador no es igual al elemento de la primera columna
                            new.writerow(r) # Se sobreescribe cada fila eliminando la que no cumpla la condicion
                        break
                file.close()
        except:
            print("\nNo se ha subido el archivo.")
        else:
            print("\nEliminado correctamente.")
    elif option == '5':

        with open("3-PROYECTO/libros.csv") as csv_file:
                var= csv.reader(csv_file)
                cont=0
                list_authors=[]
                list_books=[]
                for i in var:
                    hh=(i[5])
                    he=(i[1])
                    list_authors.append(hh)
                    list_books.append(he)
                try:
                    op=int(input("Ingresa la cantidad de números de autores\n>>>>"))
                    if op == 1:
                        print("\nEsta es la cantidad de libros con solo 1 autor\n")
                        for j in range(len(list_authors)):
                            for k in range(len(list_books)):
                                if "," not in list_authors[j]:
                                    print(list_books[j]," ",list_authors[j])
                                break

                    elif op ==2:
                        print("\nEsta es la cantidad de libros con 2 o más autores\n")
                        for j in range(len(list_authors)):
                            for k in range(len(list_books)):
                                if "," in list_authors[j]:
                                    print("Libro-> ",list_books[j]," De-> ",list_authors[j])
                                    break 
                    else:
                        print("\nNo se encontraron libros con esa cantidad de autores")                         
                except:
                    print("\nNo se reconoce el tipo de valor introducido\n")  
                    
    elif option == '6':
        pass
    elif option == '7':
        pass
    elif option == '8':
        pass
    elif option == '9':
        validation = False
        print("\nSe cerró correctamente.\n")

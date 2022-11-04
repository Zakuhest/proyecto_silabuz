from csv import *
import csv
import pandas as pd
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
        try:
            # Carga actualizada del csv
            with open(file_name+".csv") as file:
                newFile = reader(file)
                data = [i for i in newFile]
                rows = [data[r] for r in range(1,len(data))]
                   
        except:
            print("\nNo se ha subido el archivo.")
        else:
            search=input("¿De qué forma desea realizar su busqueda?\n1-ISBN o Título\n2-Autor, Editorial o Género\n3-Por número de autores\nIngrese un número>>> ")
            while search not in ("1","2","3"):
                search=input("Por favor, ingrese una opción valida\n1-ISBN o Título\n2-Autor, Editorial o Género\n3-Por número de autores\nIngrese un número>>> ")
            if search == "3":
                num_authors=int(input("Ingresa el número de autores\n>>>"))
                # Busqueda de libros por autor   
                for i in range(len(rows)):
                    list_author=convert_author_to_list(rows[i][5])
                    if len(list_author)==num_authors:
                        obj=Libro(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],convert_author_to_list(rows[i][5]))
                        print(obj.list_books()) 
                    elif  num_authors <len(list_author) or  num_authors > len(list_author):
                        pass
                print("\nBusqueda terminada\n")    
            elif search =="2":
                pass
            else:
                pass
                    
    elif option == '6':

        try:
            # Carga actualizada del csv
            with open(file_name+".csv") as file:
                newFile = reader(file)
                data = [i for i in newFile]
                rows = [data[r] for r in range(1,len(data))]
        except:
            print("\nNo se ha subido el archivo.")
        else:
            list_author = []
            print("Escogió la opción 6: Ordenar libros por títulos.\n")
            for i in range(len(rows)):
                    list_author.append(rows[i][1])
            list_author.sort()
            print("Libros ordenados alfabeticamente por títulos: \n")
            for i in list_author:
                print(i)

    elif option == '7':
        try:
            # Carga actualizada del csv
            with open(file_name+".csv") as file:
                newFile = reader(file)
        except:
            print("\nNo se ha subido el archivo")
        else:
            with open(file_name+".csv") as file:
                next(file)
                newFile = reader(file)
                update_list=[]
                id=(input("\nIngrese id de libro a actualizar\n>>> "))
                found=False
                for row in newFile:
                    if row[0]==id:
                        found=True
                        id_book=input("\nIngrese nueva ID del libro\n>>> ")
                        title=input("\nIngrese un nuevo título\n>>> ")
                        gender=input("\nIngrese un nuevo género\n>>> ")
                        isbn=input("\nIngrese un nuevo ISBN\n>>> ")
                        editor=input("\nIngrese nuevo editor\n>>> ")
                        author=input("\nIngrese nuevo autor\n>>> ")
                        row[0]=id_book
                        row[1]=title
                        row[2]=gender
                        row[3]=isbn
                        row[4]=editor
                        row[5]=author
                    update_list.append(row)
                if found:
                    with open(file_name+".csv","w+",newline='') as file:
                        header_row=["Id","Title","Gender","ISBN","Editorial","Author(s)"]
                        file.seek(0)
                        head_row=writer(file)
                        head_row.writerow(header_row)

                        upd=writer(file)
                        upd.writerows(update_list)
                        print("\n\n----------Se han actualizado los datos----------\n\n")    
                else:
                    print("\n\nNo se ha encontrado la id ingresada\n\n")

    elif option == '8':
        try:
            # Carga actualizada del csv
            with open(file_name+".csv") as file:
                newFile = reader(file)
        except:
            print("\nNo se ha subido el archivo.")
        else:
            save_books=input("¿En qué formato desea guardar el libro?\n1-csv\n2-txt\n>>>")
            while save_books not in("1","2"):
                save_books=input("Ingrese una opción válida.\n¿En qué formato desea guardar el libro?\n1-csv\n2-txt\n>>>")
            
            if save_books=="1":
                bookscsv= pd.read_csv(file_name+".csv")
                save_as_csv=input("Ingrese el nombre que desea darle al archivo\n>>> ")
                bookscsv.to_csv(f"{save_as_csv}.csv")
                print(f"El archivo de nombre {save_as_csv} se ha creado.")
    

            elif save_books=="2":
                bookstxt= pd.read_csv(file_name+".csv")
                save_as_txt=input("Ingrese el nombre que desea darle al archivo\n>>> ")
                bookstxt.to_csv(f"{save_as_txt}.txt")
                print(f"El archivo de nombre {save_as_txt} se ha creado.")

    elif option == '9':
        validation = False
        print("\nSe cerró correctamente.\n")

# Librerias usadas
from csv import *
import os
import pandas as pd
import time

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

# Creacion de una carpeta en la direccion actual, que guarde archivos, por defecto
try:
    current_directory = os.getcwd()
    saved_files = os.path.join(current_directory, "Saved Files")
    os.mkdir(saved_files)
except: 
    pass #En caso de existir la carpeta, solo seguir con el programa

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
                    time.sleep(0.5)
                    print("\nArchivo subido.")
                    time.sleep(0.5)
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
            print("\nCargando datos...")
            time.sleep(0.5)
            for i in range(len(rows)):
                # Instancia de clase Libro
                obj = Libro(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],convert_author_to_list(rows[i][5]))
                time.sleep(0.7)
                # Llamada a funcion listar libros, mediante instancia
                print(obj.list_books())
            print("Listado completo.")
    elif option == '3':
        # Capturando excepcion en caso no se encuentre el archivo subido
        try:
            print("\n\nIngresa los datos a registrar\n")
            time.sleep(1)
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
                rows = [data[r] for r in range(1,len(data))]
                val = False
                Id = input("\nID: ").upper()
                for i in range(len(rows)):
                    if Id == rows[i][0]:
                        val = True
                if val is True:
                    # Sobreescritura del csv, con modo 'w' (write)
                    with open(file_name+".csv", "w", newline='') as file:
                            new = writer(file)
                            for r in data:
                                for c in r:
                                    if c != Id: # Si el identificador no es igual al elemento de la primera columna
                                        new.writerow(r) # Se sobreescribe cada fila eliminando la que no cumpla la condicion
                                    break
                            file.close()
                else:
                    print("\nLa ID ingresada no existe.")
                    pass
        except:
            print("\nNo se ha subido el archivo.")
        else:
            if val is True:
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
            find=input("¿De qué forma desea realizar su busqueda?\n1-ISBN o Título\n2-Autor, Editorial o Género\n3-Por número de autores\nIngrese un número>>> ")
            while find not in ("1","2","3"):
                find=input("Por favor, ingrese una opción valida\n1-ISBN o Título\n2-Autor, Editorial o Género\n3-Por número de autores\nIngrese un número>>> ")
            if find == "3":
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
            elif find =="2":
                search1=input("¿De qué forma desea realizar su búsqueda?\n1-Autor\n2-Editorial\n3-Género\nIngrese un número>>> ")
                while search1 not in ("1","2","3"):
                    search1=input("Por favor, ingrese una opción válida\n1-Autor\n2-Editorial\n3-Género\nIngrese un número>>> ")
                if search1 == "3":
                    genders = []
                    for i in range(len(rows)):
                        genders.append(rows[i][2])
                    
                    print("Ingresaste la opción: Búsqueda por género\n¿Cuál de los siguientes género es el que buscas? ")
                    index3 =[]
                    for b, book2 in enumerate(genders):
                        print(str(b+1)+".", book2)
                        index3.append(str(b+1))

                    option_title3= input("Digite la opción del género del libro que buscas: ")
                    while option_title3 not in index3:
                        print("Por favor, ingrese una opción válida.")
                        for b, book2 in enumerate(genders):
                            print(str(b+1)+".", book2)
                        
                        option_title3= input("\nDigite la opción del género del libro que buscas: ")

                    index6 = int(option_title3)-1    
                    # Instancia de clase Libro
                    object3 = Libro(rows[index6][0],rows[index6][1],rows[index6][2],rows[index6][3],rows[index6][4],convert_author_to_list(rows[index6][5]))
                    # Llamada a funcion listar libros, mediante instancia
                    print(object3.list_books())
                    print("\nBúsqueda terminada\n")

                elif search1== "2":
                    editorials = []
                    for i in range(len(rows)):
                        editorials.append(rows[i][4])

                    print("Ingresaste la opción: Búsqueda por Editorial\n¿Cuál de las siguientes editoriales es el que buscas? ")
                    index7 =[]
                    for c, book3 in enumerate(editorials):
                        print(str(c+1)+".", book3)
                        index7.append(str(c+1))
                    
                    option_title4= input("Digite la opción de la editorial del libro que buscas: ")
                    while option_title4 not in index7:
                        print("Por favor, ingrese una opción válida.")
                        for c, book3 in enumerate(editorials):
                            print(str(c+1)+".", book3)
                        option_title4= input("Digite la opción de la editorial del libro que buscas: ")

                    index8 = int(option_title4)-1    
                    # Instancia de clase Libro
                    object4 = Libro(rows[index8][0],rows[index8][1],rows[index8][2],rows[index8][3],rows[index8][4],convert_author_to_list(rows[index8][5]))
                    # Llamada a funcion listar libros, mediante instancia
                    print(object4.list_books())
                    print("\nBúsqueda terminada\n")


                elif search1== "1":
                    autors =[]
                    for i in range(len(rows)):
                        autors.append(rows[i][5])
                    
                    print("Ingresaste la opción: Búsqueda por autores\n¿Cuál de las siguientes autores es el que buscas? ")
                    index9 = []
                    for d, book4 in enumerate(autors):
                        print(str(d+1)+".", book4)
                        index9.append(str(d+1))
                    
                    option_title5= input("Digite la opción del autor del libro que buscas: ")
                    while option_title5 not in index7:
                        print("Por favor, ingrese una opción válida.")
                        for d, book4 in enumerate(autors):
                            print(str(d+1)+".", book4)
                        option_title5= input("Digite la opción del autor del libro que buscas: ")

                    index10 = int(option_title5)-1    
                    # Instancia de clase Libro
                    object5 = Libro(rows[index10][0],rows[index10][1],rows[index10][2],rows[index10][3],rows[index10][4],convert_author_to_list(rows[index10][5]))
                    # Llamada a funcion listar libros, mediante instancia
                    print(object5.list_books())
                    print("\nBúsqueda terminada\n")

                
            elif find == "1":
                search=input("¿De qué forma desea realizar su busqueda?\n1-ISBN\n2-Título\nIngrese un número>>> ")
                while search not in ("1","2"):
                    search=input("Por favor, ingrese una opción válida\n1-ISBN\n2-Título\nIngrese un número>>> ")

                if search == "2":
                    titles = []
                    for i in range(len(rows)):
                        titles.append(rows[i][1])

                    print("Ingresaste la opción: Búsqueda por título\n¿Cuál de los siguientes títulos buscas? ")
                    index1 =[]
                    for a, book1 in enumerate(titles):
                        print(str(a+1)+".", book1)
                        index1.append(str(a+1))

                    option_title= input("Digite la opción del título del libro que busca: ")
                    while option_title not in index1:
                        print("Por favor, ingrese una opción válida.")
                        for a, book1 in enumerate(titles):
                            print(str(a+1)+".", book1)

                        option_title= input("\nDigite la opción del título del libro que busca: ")

                    index4 = int(option_title)-1    
                    # Instancia de clase Libro
                    object1 = Libro(rows[index4][0],rows[index4][1],rows[index4][2],rows[index4][3],rows[index4][4],convert_author_to_list(rows[index4][5]))
                    # Llamada a funcion listar libros, mediante instancia
                    print(object1.list_books())

                    print("\nBúsqueda terminada\n") 

                
                elif search =="1":
                    isbn = []
                    for i in range(len(rows)):
                        isbn.append(rows[i][3])
                    print("Ingresaste la opción: Búsqueda por ISBN\n¿Cuál de los siguientes títulos buscas? ")
                    index2 =[]
                    for l, book2 in enumerate(isbn):
                        print(str(l+1)+".", book2)
                        index2.append(str(l+1))
                    
                    option_title2= input("Digite la opción del título del libro que busca: ")
                    while option_title2 not in index2:
                        print("Por favor, ingrese una opción válida.")
                        for l, book2 in enumerate(isbn):
                            print(str(l+1)+".", book2)

                        option_title2= input("\nDigite la opción del título del libro que busca: ")

                    index5 = int(option_title2)-1    
                    # Instancia de clase Libro
                    object2 = Libro(rows[index5][0],rows[index5][1],rows[index5][2],rows[index5][3],rows[index5][4],convert_author_to_list(rows[index5][5]))
                    # Llamada a funcion listar libros, mediante instancia
                    print(object2.list_books())

                    print("\nBúsqueda terminada\n")


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
                bookscsv.to_csv(f"Saved Files\{save_as_csv}.csv")
                print(f"El archivo de nombre {save_as_csv} se ha creado.")

            elif save_books=="2":
                bookstxt= pd.read_csv(file_name+".csv")
                save_as_txt=input("Ingrese el nombre que desea darle al archivo\n>>> ")
                bookstxt.to_csv(f"Saved Files\{save_as_txt}.txt")
                print(f"El archivo de nombre {save_as_txt} se ha creado.")

    elif option == '9':
        validation = False
        print("\nSe cerró correctamente.\n")

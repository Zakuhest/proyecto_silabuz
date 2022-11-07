import requests
import json
import numpy as np
import cv2
import urllib
import time

def get_image_url(img):                
    response_2=requests.get(img)
    data_2=response_2.json()
    resp=data_2['varieties'][0]['pokemon']

    response_3=requests.get("https://pokeapi.co/api/v2/pokemon/"+resp['name'])
    data_3=response_3.json()
    img_url=data_3['sprites']['front_default']
    return img_url    

class PokeApi:
    def __init__(self):
        self.__url=f"https://pokeapi.co/api/v2/"

    def get_generation(self,gen:str):
        #Obtener lista de pokemons por generación
        response = requests.get(self.__url+"generation/"+gen)
        data = response.json()
        region=data['main_region']['name']
        print(f"\nLa región que has ingresado es {region.upper()}\n")
        input("Presiona Enter para ver la lista de pokemons...\n")
        list_gen=[j['name'] for j in data['pokemon_species']]
        list_gen_url=[l['url'] for l in data['pokemon_species']]
        for i in range(len(list_gen)):
            print(f'''Pokemon:
                    {list_gen[i].capitalize()}\n''')
            print(f'''Url:
                    {get_image_url(list_gen_url[i])}\n\n\n''')
        return "\nTerminó el proceso\n"

    def get_forms(self, form:str):
        #Obtener pokemon por forma
        response = requests.get(self.__url+"pokemon-shape/"+form)
        data = response.json()
        print(f"\nEl nombre de la forma que has seleccionado es {data['name'].upper()}")
        input("\nPulsa enter para cargar los datos de los pokemons que tienen esta forma...")
        list_name=[j['name'] for j in data['pokemon_species']]
        list_url=[l['url'] for l in data['pokemon_species']]
        for i in range(len(list_name)):
            print(f'''Pokemon:
                    {list_name[i].capitalize()}\n''')
            print(f'''Url:
                    {list_url[i]}\n\n\n''')
            time.sleep(0.1)                   
        return "\nTerminó el proceso\n"   

    def get_abilities(self, ability: str):
        #Obtener lista de pokemons por habilidad
        response = requests.get(self.__url+"ability/"+ability)
        data = response.json()

        Id = data['id']
        name = data['name'].capitalize()
        name_pokemon = [data['pokemon'][c]['pokemon']['name'].capitalize() for c, i in enumerate(data['pokemon'])]
        url_pokemon = [data['pokemon'][c]['pokemon']['url'] for c, i in enumerate(data['pokemon'])]

        print(f"\nID: {Id}")
        print(f"\nAbility: {name}")
        input("\nPresiona enter para ver los pokemons...\n")
        print("\nPokemons: \n")
        
        for i in range(len(name_pokemon)):
            print(f'''Pokemon:
                    {name_pokemon[i]}\n''')
            print(f'''Url:
                    {url_pokemon[i]}\n\n\n''')
            time.sleep(0.2)                   
        return "\nTerminó el proceso."

    def get_habitat(self, habitat: str):
        #Obtener lista de pokemons por habitat
        response = requests.get(self.__url+"pokemon-habitat/"+habitat)
        data = response.json()

        Id = data['id']
        name = data['name'].capitalize()
        name_pokemon = [data['pokemon_species'][c]['name'].capitalize() for c, i in enumerate(data['pokemon_species'])]
        url_pokemon = [data['pokemon_species'][c]['url'] for c, i in enumerate(data['pokemon_species'])]

        print(f"\nID: {Id}")
        print(f"\nHabitat: {name}")
        input("\nPresiona enter para ver los pokemons...\n")
        print("\nPokemons: \n")
        
        for i in range(len(name_pokemon)):
            print(f'''Pokemon:
                    {name_pokemon[i]}\n''')
            print(f'''Url:
                    {url_pokemon[i]}\n\n\n''')
        return "\nTerminó el proceso."

    def get_types(self, types: str):
        #Obtener lista de pokemons por tipo
        response = requests.get(self.__url+"type/"+types)
        data = response.json()

        Id = data['id']
        name = data['name'].capitalize()
        name_pokemon = [data['pokemon'][c]['pokemon']['name'].capitalize() for c, i in enumerate(data['pokemon'])]
        url_pokemon = [data['pokemon'][c]['pokemon']['url'] for c, i in enumerate(data['pokemon'])]

        print(f"\nID: {Id}")
        print(f"\nType: {name}")
        input("\nPresiona enter para ver los pokemons...\n")
        print("\nPokemons: \n")

        for i in range(len(name_pokemon)):
            print(f'''Pokemon:
                    {name_pokemon[i]}\n''')
            print(f'''Url:
                    {url_pokemon[i]}\n\n\n''')
        return "\nTerminó el proceso."


#Instanciar clase
pokeapi=PokeApi()

validation = True
while validation:
    # Estructura de menu interactivo
    print(
    """
        Opción 1: Listar pokemons por generación.
        Opción 2: Listar pokemons por forma.
        Opción 3: Listar pokemons por habilidad.
        Opción 4: Listar pokemons por habitat.
        Opción 5: Listar pokemons por tipo.
        Opción 6: Salir.
    """)
    option=input("Ingresa una opción del 1 al 6\n>>>> ").strip()
    while option not in ("1","2","3","4","5","6"):
        print(
        """
        Opción 1: Listar pokemons por generación.
        Opción 2: Listar pokemons por forma.
        Opción 3: Listar pokemons por habilidad.
        Opción 4: Listar pokemons por habitat.
        Opción 5: Listar pokemons por tipo.
        Opción 6: Salir.
        """)
        option=input("Por favor, ingresa una opción válida. Ingresa una opción del 1 al 6\n>>>> ").strip()

    #Resultado de las opciones
    if option == "1":
        # Capturando excepcion en caso no se encuentre la generacion
        try:
            generacion=input("Ingresa generación del 1 al 8\n>>>> ")
            print(pokeapi.get_generation(generacion))
        except:
            print("\nNo se encontró la generación\n")    

    elif option=="2":
        # Capturando excepcion en caso no se encuentre la forma
        try:
            form=input("Ingresa número de forma (1-14)\n>>>> ")
            print(pokeapi.get_forms(form))
        except:
            print("\nNo se encontró la información")

    elif option=="3":
        # Capturando excepcion en caso no se encuentre la habilidad
        try:
            ability=input("Ingresa [id/nombre] de habilidad:\nPor ejemplo: '1'-> Stench, '2'-> Drizzle, '3'-> Speed-boost, ... \n>>>> ")
            print(pokeapi.get_abilities(ability))
        except Exception:
            print(f"\nNo se encontró la habilidad.")  
    
    elif option=="4":
        # Capturando excepcion en caso no se encuentre el habitat
        try:
            habitat = input("Ingresa [id/nombre] de habitat:\nPor ejemplo: '1'-> Cave, '2'-> Forest, '3'-> Grassland, ... \n>>>> ")
            print(pokeapi.get_habitat(habitat))
        except Exception:
            print(f"No se encontró el habitat.") 
    
    elif option=="5":
        # Capturando excepcion en caso no se encuentre el tipo
        try:
            types = input("Ingresa [id/nombre] de tipo:\nPor ejemplo: '1'-> Normal, '2'-> Fighting, '3'-> Flying, ... \n>>>> ")
            print(pokeapi.get_types(types))
        except Exception:
            print(f"No se encontró el tipo.")

    elif option=="6":
        validation = False
        print("\nSe cerró correctamente.\n")
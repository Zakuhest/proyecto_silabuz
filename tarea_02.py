import requests
import json
import numpy as np
import cv2
import urllib

class PokeApi:
    def __init__(self):
        self.__url=f"https://pokeapi.co/api/v2/"

    def get_generation(self,gen:str):
        #Obtener lista de pokemons por generación
        response = requests.get(self.__url+"generation/"+gen)
        data = response.json()
    
        region=data['main_region']['name']
        print(f"\nLa región que has ingresado es {region.upper()}\nY esta es la lista de pokemons:\n")
        lista=[j['name'] for j in data['pokemon_species']]
        lista="\n".join(lista)
        return lista

    def get_forms(self, form:str):
        #Obtener pokemon por forma
        response = requests.get(self.__url+"pokemon-form/"+form)
        data = response.json()
        forms=data['pokemon']['name']
        form2=data['form_name']
        print(f"El nombre del pokemon es: {forms.capitalize()}")

        form3 = data['form_order']
        print(f"Este es el numero de orden de forma del pokemon {form3}")

        if form2:
            print(f"La forma de este pokemon es {form2}")
        else:
            print("Este pokemon no tiene formas")

        image_url= data['sprites']['front_default']
        resp = urllib.request.urlopen(image_url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        return "\nTerminó el proceso."     

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
        print("\nPokemons: \n")
        
        for i in range(len(name_pokemon)):
            print(name_pokemon[i])
            print(url_pokemon[i])

        return "\nTerminó el proceso."


#Instanciar clase
pokeapi=PokeApi()

validation = True

#Opciones a elegir entre las 5 alternativas

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

    while option in ("") or option not in ("1","2","3","4","5", "6"):
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
        try:
            generacion=input("Ingresa generación del 1 al 8\n>>>> ")
            print(pokeapi.get_generation(generacion))
        except Exception as a:
            print(f"{a}\nNo se encontró la generación")    

    elif option=="2":
        try:
            form=input("Ingresa id de pokemon:\nPor ejemplo: '10041'-> Arceus, '10031'-> Deoxys-Attack, ...\n>>>> ")
            print(pokeapi.get_forms(form))
        except Exception as a:
            print(f"{a}\nNo se encontró la información")

    elif option=="3":
        try:
            ability=input("Ingresa [id/nombre] de habilidad:\nPor ejemplo: '1'-> Stench, '2'-> Drizzle, '3'-> Speed-boost, ... \n>>>> ")
            print(pokeapi.get_abilities(ability))
        except Exception:
            print(f"\nNo se encontró la habilidad.")  
    elif option=="4":
        pass     
    elif option=="5":
        pass
    elif option=="6":
        validation = False
        print("\nSe cerró correctamente.\n")
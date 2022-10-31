import requests
import json

class PokeApi:
    def __init__(self):
        self.__url=f"https://pokeapi.co/api/v2/"
        print(requests.get(self.__url))

    def get_generation(self,gen:str):
        response = requests.get(self.__url+"generation/"+gen)
        data = response.json()
    
        region=data['main_region']['name']
        print(f"\nLa región que has ingresado es {region.upper()}\nY esta es la lista de pokemons:\n")
        lista=[j['name'] for j in data['pokemon_species']]
        lista="\n".join(lista)
        return lista

    def get_forms(self, form:str):
        response = requests.get(self.__url+"pokemon-form/"+form)
        data = response.json()
        forms=data['pokemon']['name']
        form2=data['form_name']
        print(f"El nombre del pokemon es: {forms.capitalize()}")

        form3 = data['form_order']
        print(f"Este es el numero de orden de forma del pokemon {form3}")

        if form2:
            return f"La forma de este pokemon es {form2}"
        else:
            return"Este pokemon no tiene formas"

#Instanciar objeto
pokeapi=PokeApi()

option=input("Ingresa una opción del 1 al 5\n>>>>").strip()
while option in ("") or option not in ("1","2","3","4","5"):
    print("Por favor, ingresa una opción válida")
    option=input("Ingresa una opción del 1 al 5\n>>>>").strip()

if option == "1":
    try:
        generacion=input("Ingresa generación del 1 al 8\n>>>> ")
        print(pokeapi.get_generation(generacion))
    except Exception as a:
        print(f"{a}\nNo se encontró la generación")    

elif option=="2":
    try:
        form=input("Ingresa id de pokemon:\nPor ejemplo: '10041'->Arceus, '10031'->Deoxys-Attack\n>>>>")
        print(pokeapi.get_forms(form))
    except Exception as a:
        print(f"{a}\nNo se encontró la información")
        
elif option=="3":
    pass   
elif option=="4":
    pass     
elif option=="5":
    pass
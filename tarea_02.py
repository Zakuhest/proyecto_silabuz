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
    pass
elif option=="3":
    pass   
elif option=="4":
    pass     
elif option=="5":
    pass
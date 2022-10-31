import requests
import json

class PokeApi:
    def __init__(self):
        self.__url=f"https://pokeapi.co/api/v2/"
        print(requests.get(self.__url))


pokeapi=PokeApi
pokeapi()
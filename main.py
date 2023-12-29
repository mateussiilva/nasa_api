import requests
import wget

from pprint import pprint as print


def baixar_imagem(url_image:str,path_image:str):
    wget.download(url_image,path_image)
def criar_pasta():
    pass


KEY_API = "p26GqFEtUnVjtAy0yRx9EtyX9asPRFhgUjaKarzd"
url = f"https://api.nasa.gov/planetary/apod?api_key={KEY_API}"
response = requests.get(url)
response_json = response.json()
# chaves = tuple(map(lambda k: k,response_json))
# print(chaves)
titulo = response_json.get("title")
url_image = response_json.get("url")
path_image = titulo + ".jpg"

if response.status_code == 200:
    baixar_imagem(url_image,path_image)
    print("Imagem Baixada com sucesso!")
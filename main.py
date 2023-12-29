import requests
import urllib.request
from json import dump
from os.path import join
from pprint import pprint as print

def download_image(url_file,name_file):
	try:
		urllib.request.urlretrieve(url_file,name_file)
	except Exception as e:
		print(e)
	print("Download sucess")

# CONSTANTES
PATH = "/home/mateus/projetos_pessoais/nasa_api/assets/images"
KEY_API = "p26GqFEtUnVjtAy0yRx9EtyX9asPRFhgUjaKarzd"

url = f"https://api.nasa.gov/planetary/apod?api_key={KEY_API}"
response = requests.get(url)
dados = dict()

if response.status_code == 200:
	json_response = response.json()
	imagem = json_response.get("url")
	nome_image = json_response.get("title")+".jpg"

	download_image(imagem,join(PATH,nome_image))
 
	dados["image"] = join(PATH,nome_image)
	dados["titulo"] = json_response.get("title")
	dados["texto"] = json_response.get("explanation")
	dados["autor"] = json_response.get("copyright")
	with open("dados.json","w+") as file:
		dump(dados,file)

else:
	print("Erro, verifique a url")
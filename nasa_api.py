import requests
import json
import urllib.request
from os.path import join
from pprint import pprint as print

def download_image(url_file,name_file):
	try:
		urllib.request.urlretrieve(url_file,name_file)
	except Exception as e:
		print(e)
	print("Download sucess")


PATH = r"C:\Users\Usuario\Desktop"
KEY_API = "p26GqFEtUnVjtAy0yRx9EtyX9asPRFhgUjaKarzd"
url = f"https://api.nasa.gov/planetary/apod?api_key={KEY_API}"
response = requests.get(url)

if response.status_code == 200:
	json_response = response.json()

	dict_response = dict(json_response)
	imagem = dict_response.get("url")
	nome_image = dict_response.get("title")+".jpg"
	path_file = join(PATH,nome_image)
	print(path_file)
	download_image(imagem,path_file)

else:
	print("Erro, verifique a url")
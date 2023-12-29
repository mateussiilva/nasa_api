
from json import load,dump
from typing import Dict



class PyJson:

    
    def __init__(self,name_file:str) -> None:
        self.file = name_file
        
    def ler_json(self) -> Dict:
        with open(self.file,"r") as fp:
            dados = load(fp)
        return dados
    
    
if __name__ == "__main__":
    dados = PyJson("dados.json").ler_json()
    print(dados)
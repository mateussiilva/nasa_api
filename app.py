from flask import Flask,render_template,request
from PyJson import PyJson

app = Flask(__name__)




@app.route("/")
def home_page():
    return render_template(
        "home.html",title_page="Pagina Inicial",
        dados_imagem = PyJson('dados.json').ler_json()
        )



if __name__ == "__main__":
    app.run(debug=True)
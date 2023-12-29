from flask import Flask,render_template,request


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html",title_page="Pagina Inicial")



if __name__ == "__main__":
    app.run(debug=True)
#necesitamos un framework, podríamos hacerlo con nuestro propio codigo pero noe s lo recomendable.
#Django (más preparado) o Flask(Es más simple). Vamos a usar Flask.
from flask import Flask, render_template
#Inicializamos flask.

app = Flask(__name__) #variable para confirmar para confirmar que esta en el archivo principal

@app.route("/") # / es la página principal
def home():
    return render_template("home.html")

@app.route("/about")
def about(): 
    return render_template ("about.html")

if __name__ == "__main__":
    app.run(debug=True) 
   
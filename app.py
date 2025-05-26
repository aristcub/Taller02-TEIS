from flask import Flask, render_template
from app_poke.routes import pokenea_bp
import os

# Configurar ruta explícita para templates y static
app = Flask(
    __name__,
    template_folder="app_poke/templates",
    static_folder="app_poke/static"
)

app.register_blueprint(pokenea_bp, url_prefix="/pokenea")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

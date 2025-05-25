from flask import Flask, jsonify, render_template
from data import pokeneas
import random
import socket

app = Flask(__name__)

def get_container_id():
    return socket.gethostname()

@app.route("/api/pokenea")
def api_pokenea():
    pokenea = random.choice(pokeneas)
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": get_container_id()
    }
    return jsonify(response)

@app.route("/pokenea")
def show_pokenea():
    pokenea = random.choice(pokeneas)
    return render_template("pokenea.html", pokenea=pokenea, contenedor_id=get_container_id())

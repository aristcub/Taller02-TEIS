from flask import Blueprint, jsonify, render_template
from app_poke.data import pokeneas
import random
import socket

pokenea_bp = Blueprint('pokenea', __name__)

def get_container_id():
    return socket.gethostname()

@pokenea_bp.route("/json")
def api_pokenea():
    pokenea = random.choice(pokeneas)
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": get_container_id()
    })

@pokenea_bp.route("/frase")
def show_pokenea():
    pokenea = random.choice(pokeneas)
    return render_template("pokenea_view.html", pokenea=pokenea, contenedor_id=get_container_id())

@pokenea_bp.route("/ui")
def api_ui():
    return render_template("pokenea_api.html")


from flask import Flask, jsonify, render_template
import random
import os

app = Flask(__name__)

# Arreglo quemado de Pokeneas
pokeneas = [
    {
        "id": 1,
        "nombre": "Arepón",
        "altura": 0.5,
        "habilidad": "Doble Energía",
        "imagen": "🥟",
        "frase": "Con hambre no se piensa, mijo. Primero arepa, luego guerra."
    },
    {
        "id": 2,
        "nombre": "Silletrín",
        "altura": 1.2,
        "habilidad": "Floral Flash",
        "imagen": "💐",
        "frase": "La vida es como una silleta: pesada, pero llena de color."
    },
    {
        "id": 3,
        "nombre": "Guariluz",
        "altura": 1.5,
        "habilidad": "Brillo de Feria",
        "imagen": "🎇",
        "frase": "No hay oscuridad que una alborada no ilumine."
    }
]

# Ruta JSON
@app.route('/pokenea/json')
def pokenea_json():
    elegido = random.choice(pokeneas)
    contenedor_id = os.uname().nodename  # ID del contenedor o nombre del host
    data = {
        "id": elegido["id"],
        "nombre": elegido["nombre"],
        "altura": elegido["altura"],
        "habilidad": elegido["habilidad"],
        "contenedor_id": contenedor_id
    }
    return jsonify(data)

# Ruta con imagen y frase
@app.route('/pokenea/frase')
def pokenea_frase():
    elegido = random.choice(pokeneas)
    contenedor_id = os.uname().nodename
    return render_template("frase.html", pokenea=elegido, contenedor_id=contenedor_id)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# lista de retos
retos = [
    "Hoy no consumas carne: reduce tu huella de carbono digital y alimentaria.",
    "Apaga los vampiros de energía: desconecta cargadores y electrodomésticos que no uses.",
    "Ducha flash: intenta bañarte en menos de 5 minutos hoy.",
    "Cero plástico: no aceptes bolsas, pajitas ni botellas de plástico de un solo uso hoy.",
    "Movilidad limpia: camina, usa bicicleta o transporte público hoy."
]

# variables del juego
datos_usuario = {
    "reto": random.choice(retos),
    "pts": 0,
    "lvl": 1,
    "listo": False
}

@app.route('/')
def home():
    return render_template('index.html', juego=datos_usuario)

@app.route('/completar', methods=['POST'])
def check_reto():
    if datos_usuario["listo"] == False:
        datos_usuario["pts"] += 10
        datos_usuario["listo"] = True
        # sube de lvl cada 30 puntos
        datos_usuario["lvl"] = (datos_usuario["pts"] // 30) + 1
    return redirect(url_for('home'))

@app.route('/nuevo_reto', methods=['POST'])
def change_reto():
    datos_usuario["reto"] = random.choice(retos)
    datos_usuario["listo"] = False
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

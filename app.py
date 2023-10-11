from flask import Flask, request, render_template, jsonify

from logic.voluntario import Voluntario

app = Flask(__name__)

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []

@app.route("/tomar_datos", methods=["POST"])
def agregar_voluntario():
    # Obtén los datos del formulario enviado
    data = request.form

    # Accede a los datos por sus nombres de campo
    ID = data['ID']
    Nombre = data['Nombre']
    Apellido = data['Apellido']
    telefono = data['telefono']
    Intereses = data['Intereses']

    
    voluntario = Voluntario(ID, Nombre, Apellido, telefono, Intereses)
    voluntarios_db.append(voluntario)

  
    return jsonify({"mensaje": "Voluntario agregado con éxito"})

if __name__ == '__main__':
    app.run(debug=True)
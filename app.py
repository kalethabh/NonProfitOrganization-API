from flask import Flask, request, render_template, jsonify

from logic.voluntario import Voluntario

app = Flask(__name__)

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []


@app.route('/voluntario')
def voluntario():
    return render_template('voluntario.html')


@app.route('/agrevoluntario', methods=['POST'])
def add_voluntario():
    ID = request.form.get('ID')
    Nombre = request.form.get('name')
    Apellido = request.form.get('apellido')
    Telefono = request.form.get('telefono')
    Intereses = request.form.get('intereses')

    nuevo_voluntario = {
        'ID': ID,
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Telefono': Telefono,
        'Intereses': Intereses
    }

    voluntarios_db.append(nuevo_voluntario)
    return jsonify({"mensaje": "Voluntario agregado con éxito"})


if __name__ == '__main__':
    app.run(debug=True)

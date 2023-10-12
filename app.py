from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []


@app.route("/")
def index():
    print('Request for index page received')
    return render_template("Home.html")


@app.route('/register-voluntario')
def voluntario():
    return render_template('voluntario.html')


@app.route('/create-voluntario', methods=['POST'])
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
    return jsonify({"mensaje": "Voluntario agregado con éxito", "nuevo_voluntario": nuevo_voluntario})

# Ruta para eliminar voluntario por ID


@app.route('/delete-voluntario/<id>', methods=['GET'])
def delete_voluntario(id):
    for voluntario in voluntarios_db:
        if voluntario['ID'] == id:
            voluntarios_db.remove(voluntario)
            return jsonify({"mensaje": "Voluntario eliminado con éxito"})
    return jsonify({"mensaje": "Voluntario no encontrado"})


# Ruta para mostrar todos los voluntarios
@app.route('/voluntarios', methods=['GET'])
def mostrar_voluntarios():
    return jsonify({"voluntarios": voluntarios_db})


if __name__ == '__main__':
    app.run(debug=True)

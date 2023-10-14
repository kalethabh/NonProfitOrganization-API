from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='templates')

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []

# Lista para almacenar programas
programas_db = []

# Ruta para mostrar la página principal
@app.route("/")
def index():
    print('Request for index page received')
    return render_template("Home.html")

# Ruta para mostrar formulario de registro de voluntario
@app.route('/register-voluntario')
def voluntario():
    return render_template('FormularioVoluntario.html')

# Ruta para registrar un voluntario
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

# Ruta para mostrar formulario de registro de programa
@app.route('/register-programa')
def programa():
    return render_template('FormularioPrograma.html')

# Ruta para registrar un programa
@app.route('/create-programa', methods=['POST'])
def add_programa():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')

    nuevo_programa = {
        'nombre': nombre,
        'descripcion': descripcion,
        'participantes': []
    }

    programas_db.append(nuevo_programa)
    return jsonify({"mensaje": "Programa agregado con éxito", "nuevo_programa": nuevo_programa})

# Ruta para mostrar todos los programas
@app.route('/programas', methods=['GET'])
def mostrar_programas():
    return jsonify({"programas": programas_db})

# Ruta para mostrar formulario de registro en programa
@app.route('/asignar-programa')
def AsignarPrograma():
    return render_template('AsignarPrograma.html')

# Ruta para que los voluntarios se unan a un programa
@app.route('/unirse-programa/<int:programa_id>/<int:voluntario_id>', methods=['GET'])
def unirse_programa(programa_id, voluntario_id):
    programa_encontrado = None
    voluntario_encontrado = None

    print(programa_id)
    print(voluntario_id)

    # Buscar el programa por su ID
    for programa in programas_db:
        if programa['ID'] == programa_id:
            programa_encontrado = programa
            break

    # Buscar el voluntario por su ID
    for voluntario in voluntarios_db:
        if voluntario['ID'] == voluntario_id:
            voluntario_encontrado = voluntario
            break

    if programa_encontrado and voluntario_encontrado:
        programa_encontrado['participantes'].append(voluntario_encontrado)
        return jsonify({"mensaje": "Voluntario agregado al programa con éxito"})
    else:
        return jsonify({"mensaje": "Programa o voluntario no encontrado"})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

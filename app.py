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
    Nombre = request.form.get('Nombre')
    Apellido = request.form.get('Apellido')
    Telefono = request.form.get('Telefono')
    Intereses = request.form.get('Intereses')

    nuevo_voluntario = {
        'ID': ID,
        'name': Nombre,
        'Apellido': Apellido,
        'Telefono': Telefono,
        'Intereses': Intereses
    }
    
    voluntarios_db.append(nuevo_voluntario)
    return jsonify({"mensaje": "Voluntario agregado con éxito", "nuevo_voluntario": nuevo_voluntario})

# Ruta para eliminar voluntario por ID
@app.route('/eliminar-voluntario', methods=['GET'])
def form_delete_voluntario():
    return render_template('FormDeleteVoluntario.html')

# Ruta para eliminar voluntario por ID
@app.route('/eliminar-voluntario', methods=['POST'])
def delete_voluntario():
    ID = request.form.get('ID')
    for voluntario in voluntarios_db:
        if voluntario['ID'] == ID:
            voluntarios_db.remove(voluntario)
            return jsonify({"mensaje": "Voluntario eliminado con éxito"})
    return jsonify({"mensaje": "Voluntario no encontrado"})

# Ruta para mostrar todos los voluntarios
@app.route('/voluntarios')
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
@app.route('/unirse-programa', methods=['POST'])
def unirse_programa():
    programa_id = request.form.get('programa_id')
    voluntario_id = request.form.get('voluntario_id')

    # Buscar el programa por su nombre
    programa_encontrado = next(
        (programa for programa in programas_db if programa['nombre'] == programa_id), None)

    # Buscar el voluntario por su ID
    voluntario_encontrado = next(
        (voluntario for voluntario in voluntarios_db if voluntario['ID'] == voluntario_id), None)

    if programa_encontrado and voluntario_encontrado:
        programa_encontrado['participantes'].append(voluntario_encontrado)
        return jsonify({"mensaje": "Voluntario agregado al programa con éxito"})
    else:
        return jsonify({"mensaje": "Programa o voluntario no encontrado"})


if __name__ == '__main__':
    app.run(debug=True)

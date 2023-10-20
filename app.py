from fastapi import FastAPI, Form, JSONResponse

app = FastAPI()

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []

# Lista para almacenar programas
programas_db = []

# Ruta para registrar un voluntario
@app.post('/create-voluntario', response_class=JSONResponse)
async def add_voluntario(ID: int = Form(...), Nombre: str = Form(...), Apellido: str = Form(...), Telefono: int = Form(...), Intereses: str = Form(...)):
    nuevo_voluntario = {
        'ID': ID,
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Telefono': Telefono,
        'Intereses': Intereses
    }

    voluntarios_db.append(nuevo_voluntario)
    return {"mensaje": "Voluntario agregado con éxito", "nuevo_voluntario": nuevo_voluntario}

# Ruta para eliminar voluntario por ID
@app.post('/eliminar-voluntario', response_class=JSONResponse)
async def delete_voluntario(ID: str = Form(...)):
    for voluntario in voluntarios_db:
        if voluntario['ID'] == ID:
            voluntarios_db.remove(voluntario)
            return {"mensaje": "Voluntario eliminado con éxito"}
    return {"mensaje": "Voluntario no encontrado"}

# Ruta para registrar un programa
@app.post('/create-programa', response_class=JSONResponse)
async def add_programa(nombre: str = Form(...), descripcion: str = Form(...)):
    nuevo_programa = {
        'nombre': nombre,
        'descripcion': descripcion,
        'participantes': []
    }

    programas_db.append(nuevo_programa)
    return {"mensaje": "Programa agregado con éxito", "nuevo_programa": nuevo_programa}

# Ruta para que los voluntarios se unan a un programa
@app.post('/unirse-programa', response_class=JSONResponse)
async def unirse_programa(programa_id: str = Form(...), voluntario_id: str = Form(...)):
    programa_encontrado = next((programa for programa in programas_db if programa['nombre'] == programa_id), None)
    voluntario_encontrado = next((voluntario for voluntario in voluntarios_db if voluntario['ID'] == voluntario_id), None)

    if programa_encontrado and voluntario_encontrado:
        programa_encontrado['participantes'].append(voluntario_encontrado)
        return {"mensaje": "Voluntario agregado al programa con éxito"}
    else:
        return {"mensaje": "Programa o voluntario no encontrado"}

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []

# Lista para almacenar programas
programas_db = []

# Ruta para mostrar la página principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    print('Request for index page received')
    return templates.TemplateResponse('Home.html', {"request": request})

# Ruta para mostrar formulario de registro de voluntario
@app.get('/register-voluntario', response_class=HTMLResponse)
async def voluntario(request: Request):
    return templates.TemplateResponse('FormularioVoluntario.html', {"request": request})

# Ruta para registrar un voluntario
@app.post('/create-voluntario', response_class=JSONResponse)
async def add_voluntario(ID: str = Form(...), Nombre: str = Form(...), Apellido: str = Form(...), Telefono: str = Form(...), Intereses: str = Form(...)):
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
@app.get('/eliminar-voluntario', response_class=HTMLResponse)
async def form_delete_voluntario(request: Request):
    return templates.TemplateResponse('FormDeleteVoluntario.html', {"request": request})

# Ruta para eliminar voluntario por ID
@app.post('/eliminar-voluntario', response_class=JSONResponse)
async def delete_voluntario(ID: str = Form(...)):
    for voluntario in voluntarios_db:
        if voluntario['ID'] == ID:
            voluntarios_db.remove(voluntario)
            return {"mensaje": "Voluntario eliminado con éxito"}
    return {"mensaje": "Voluntario no encontrado"}

# Ruta para mostrar todos los voluntarios
@app.get('/voluntarios', response_class=JSONResponse)
async def mostrar_voluntarios():
    return {"voluntarios": voluntarios_db}

# Ruta para mostrar formulario de registro de programa
@app.get('/register-programa', response_class=HTMLResponse)
async def programa(request: Request):
    return templates.TemplateResponse('FormularioPrograma.html', {"request": request})

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

# Ruta para mostrar todos los programas
@app.get('/programas', response_class=JSONResponse)
async def mostrar_programas():
    return {"programas": programas_db}

# Ruta para mostrar formulario de registro en programa
@app.get('/asignar-programa', response_class=HTMLResponse)
async def AsignarPrograma(request: Request):
    return templates.TemplateResponse('AsignarPrograma.html', {"request": request})

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

if __name__ == '__main__':
    uvicorn.run('app:app')
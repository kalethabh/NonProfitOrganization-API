class Voluntario:
    """
    Clase que representa a un voluntario.
    """
    def __init__(self, ID, Nombre, Apellido, telefono, Intereses, voluntarios_db):
        self.ID = ID
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.telefono = telefono
        self.Intereses = Intereses
        self.actividades_asignadas = []  # Puedes usar una lista para rastrear las actividades asignadas
        self.voluntarios_db = []

    def agregar_voluntario(self):
        # Crear un diccionario con los datos del voluntario
        voluntario_data = {
            'ID': self.ID,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'telefono': self.telefono,
            'Intereses': self.Intereses
        }

        # Agregar el diccionario a la lista de voluntarios (o a tu base de datos real)
        self.voluntarios_db.append(voluntario_data)

    def eliminar_voluntario(self, voluntario_id):
        # Buscar el voluntario por su ID y eliminarlo
        for voluntario in self.voluntarios_db:
            if voluntario['ID'] == voluntario_id:
                self.voluntarios_db.remove(voluntario)

    def asignar_actividad(self, actividad):
        # Agregar la actividad a la lista de actividades asignadas al voluntario
        self.actividades_asignadas.append(actividad)

# Lista para almacenar voluntarios (simulación de una base de datos)
voluntarios_db = []

# Ejemplo de uso de la clase Voluntario


# Luego, puedes asignar actividades al voluntario1
actividad1 = "Ayuda en el comedor comunitario"
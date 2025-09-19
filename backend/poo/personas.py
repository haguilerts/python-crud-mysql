# Clase Persona
class Persona:
    def __init__(self, nombre, apellido=None, telefono=None, email=None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

# Clase Contacto hereda de Persona
class Contacto(Persona):
    def __init__(self, id, nombre, apellido, telefono, email):
        super().__init__(nombre, apellido, telefono, email)
        self.id = id

# Clase Cliente solo hereda nombre
class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

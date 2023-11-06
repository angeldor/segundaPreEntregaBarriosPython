class Client:
    def __init__(self, id, nombre, apellido, email, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def login(self):
        return f"Hola {self.nombre}, Inicio de sesion exitoso"
    
    def comprar(self):
        return "Compra realizada con éxito"




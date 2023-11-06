from paquete.modulocliente import Client

Angel = Client(nombre="Angel", apellido="Barrios",email="ab0180333@gmail.com", telefono=2215852370, id=1)
print (Angel)
print (Angel.login())
print (Angel.comprar())

Florencia = Client(nombre="Florencia", apellido="Galilea", email="florenciagalilea@gmail.com", telefono=2219998877, id=2)
print (Florencia)
print(Florencia.login())
print(Florencia.comprar())

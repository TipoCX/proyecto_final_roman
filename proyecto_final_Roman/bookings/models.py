from django.db import models

# Create your models here.
# class Reserva:

#     def __init__(self, nombre_de_usuario, destino) -> None:
#         self.nombre_de_usuario = nombre_de_usuario
#         self.destino = destino

#     def __str__(self) -> str:
#         return f"esta es una reserva del usuario: {self.nombre_de_usuario} con el destino: {self.destino}"

class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"esta es una reserva del usuario: {self.nombre_de_usuario} con el destino: {self.destino}"

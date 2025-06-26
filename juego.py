from personaje import Personaje
import random
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    if os.name == "nt":
        # Para Windows
        os.system("cls")

print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique nombre de su personaje:")
limpiar_pantalla()

personaje = Personaje(nombre)

print(personaje.estado)

nn = Personaje()
prob = personaje.probabilidad(nn)
opcion = Personaje.mostrar_mensaje(prob)

while opcion == 1:
    resultado = "G" if random.uniform(0,100) < prob else "P"
    if resultado == "G":
        print("""
              ¡Le has ganado al orco, felicidades!
 ¡Recibirás 50 puntos de experiencia!""")
        personaje.estado = 50
        nn.estado = -30

    else:
        print("""
               ¡Oh no! ¡El orco te ha ganado!
 ¡Has perdido 30 puntos de experiencia!
""")
        personaje.estado = -30
        nn.estado = 50
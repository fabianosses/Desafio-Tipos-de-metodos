from personaje import Personaje
import random
import os

def limpiar_terminal():
    """
    Limpia pantalla de terminmal
    """
    if os.system == "cls":  # For Windows
        _ = os.system('cls')
    else:  # For Linux and macOS
        _ = os.system('clear')

print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique nombre de su personaje:")
limpiar_terminal()

personaje = Personaje(nombre)

print(personaje.estado)

nn = Personaje()
prob = personaje.probabilidad(nn)
opcion = Personaje.mostrar_mensaje(prob)

while opcion == 1:
    limpiar_terminal()
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

    print(personaje.estado)
    print(nn.estado)

    prob = personaje.probabilidad(nn)
    opcion = Personaje.mostrar_mensaje(prob)

print("has huido!!")
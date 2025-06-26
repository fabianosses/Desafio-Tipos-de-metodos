class Personaje:
    def __init__(self, nombre = "orco"):
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre}       NIVEL: {self.nivel}      EXP: {self.exp}"
    
    @estado.setter
    def estado(self, exp):

        exp_temp = self.exp + exp
        # subir Nivel
        while exp_temp > 99:
            self.nivel += 1
            exp_temp -= 100

        # bajar Nivel
        while exp_temp < 0:
            if self.nivel == 1:
                self.exp = 0
                exp_temp = 0
            else:
                self.nivel -= 1
                exp_temp = 0

        self.exp = exp_temp

    def __lt__ (self, enemigo):
    # sobrecarga para método de "menor que" implementado para mis instancias
        return self.nivel < enemigo.nivel
    
    def __gt__ (self, enemigo):
    # sobrecarga para método de "mayor que" implementado para mis instancias
        return self.nivel > enemigo.nivel
    
    def __eq__ (self,enemigo):
    # sobrecargapara método de "igual que" implementado para mis instancias
        return self.nivel == enemigo.nivel
                
    def probabilidad (self, enemigo):
        """
        ○ Si el jugador es menor al orco, tiene un 33% de probabilidades de ganar.
        ○ Siel jugador es mayor al orco, tiene un 66% de probabilidades de ganar.
        ○ Siel jugador es igual al orco, tiene un 50% de probabilidades de ganar.
        """
        if self < enemigo:
            return 33
        elif self > enemigo:
            return 66
        else:
            self == enemigo
            return 50

    @staticmethod
    def mostrar_mensaje (probab):
        return int(input(f"""
        ¡Oh no!, ¡Ha aparecido un Orco!
                         
 Con tu nivel actual, tienes {probab} de probabilidades de ganarle al Orco.
 Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
 Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
 ¿Qué deseas hacer?
 1. Atacar
 2. Huir            """))



class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.exp = 0
        pass

    @property
    def estado(self):
        return f"El nombre es: {self.nombre}, su nivel: {self.nivel}, su experiencia: {self.exp}"
    
    @estado.setter
    def estado(self, exp):

        exp_temp = self.exp + exp
        # subir Nivel
        while exp_temp > 99:
            self.nivel += 1
            exp_temp -= 100

        # bajar Nivel
        while exp_temp < 0:
            self.nivel -= 1
            exp_temp = 0
            if self.nivel == 1:
                self.exp = 0
                exp_temp = 0

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
            return 0.33
        elif self > enemigo:
            return 0.66
        else:
            self == enemigo
            return 0.5




        


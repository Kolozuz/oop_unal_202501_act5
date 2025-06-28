class Programador:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class EquipoMaraton:
    def __init__(self, nombre, universidad):
        self.nombre = nombre
        self.universidad = universidad
        self.programadores = []
        self.tamaño_maximo = 3
        self.valid = False
    
    def agregar_programador(self, programador):
        if self.esta_lleno:
            print("No puede añadirse otro integrante, el equipo ya está completo.")
            return
        
        self.programadores.append(programador)
    
    def mostrar_programadores(self):
        for programador in self.programadores:
            print(f"{programador.nombre} {programador.apellido}")

    def esta_lleno(self):
        return len(self.programadores) == self.tamaño_maximo
        
    def validar_campo(self, valor_campo: str) -> bool:
        if len(valor_campo) >= 20:
            return False
        
        for char in valor_campo:
            if char.isdigit():
                return False
            
        return True

class App:
    pass

if __name__ == "__main__":
    
    mi_app = App()
    mi_app.run()


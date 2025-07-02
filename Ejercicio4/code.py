import math
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
    def __init__(self):
        self.root = Tk()
        self.root.title("Formulario de Inscripción - Maratón de Programación")
        
        self.setup_ui()

    def setup_ui(self):
        # Seccion para la información del equipo
        team_info_label_frame = ttk.LabelFrame(self.root, text="Información del Equipo")
        team_info_label_frame.pack(padx=15, pady=15, fill=X)

        ttk.Label(team_info_label_frame, text="Nombre del Equipo:").pack(padx=10, pady=5, anchor=W)
        self.team_name_entry = ttk.Entry(team_info_label_frame)
        self.team_name_entry.pack(padx="10 80", pady=5, fill=X)

        universities = ["Universidad Nacional de Colombia (UNAL)", "Universidad de Antioquia (UDEA)", "Universidad abierta y a Distancia (UNAD)" "Universidad de los Andes (UNIANDES))"]
        ttk.Label(team_info_label_frame, text="Universidad:").pack(padx=10, pady=5, anchor=W)
        self.university_entry = ttk.Combobox(team_info_label_frame, values=universities)
        self.university_entry.set("Escoja una universidad")
        self.university_entry.pack(padx="10 80", pady=5, fill=X)

        # Sección para la información de los programadores
        self.programmers_info_label_frame = ttk.LabelFrame(self.root, text="Información de los integrantes")
        self.programmers_info_label_frame.pack(side=LEFT, padx=15, pady=15, fill=X)

        self.programador_fields = [[ttk.Label(self.programmers_info_label_frame, text=f"Nombre programador {_ + 1}:"), ttk.Entry(self.programmers_info_label_frame, width=50)] for _ in range(3)]
        
        for label, entry in self.programador_fields:
            label.pack(padx=10, pady=5, anchor=W)
            entry.pack(padx="10 80", pady=5, fill=X)

        # Botones para agregar y quitar programadores
        actions_label_frame = ttk.LabelFrame(self.root, text="Acciones")
        actions_label_frame.pack(side=TOP, padx=15, pady=15, fill=Y)
        ttk.Button(actions_label_frame, text="+", command=self.agregar_programador).pack(pady=10, padx=5, anchor=W)
        ttk.Button(actions_label_frame, text="-", command=self.quitar_programador).pack(pady=10, padx=5, anchor=W)

        ttk.Button(self.root, text="Enviar", command=self.submit_form).pack(side=TOP, pady=10)

    def agregar_programador(self):
        if len(self.programador_fields) < 3:
            # Crear un nuevo campo para el programador
            new_label = ttk.Label(self.programmers_info_label_frame, text=f"Nombre programador {len(self.programador_fields) + 1}:")
            new_entry = ttk.Entry(self.programmers_info_label_frame)
            new_label.pack(padx=10, pady=5, anchor=W)
            new_entry.pack(padx="10 80", pady=5, fill=X)

            self.programador_fields.append((new_label, new_entry))
            
        else:
            messagebox.showerror("Error", "No se pueden agregar más programadores")
    
    def quitar_programador(self):
        if len(self.programador_fields) > 2:
            # Eliminar el último campo de programador
            label, entry = self.programador_fields.pop()
            label.destroy()
            entry.destroy()
        else:
            messagebox.showerror("Error", "El equipo debe tener al menos 2 integrantes")

    def submit_form(self):
        self.equipo = EquipoMaraton("", "")
        pass
#
        ## Botón para calcular las notas
        #self.calculate_button = ttk.Button(self.root, text="Calcular", command=self.calcular_notas)
        #self.calculate_button.grid(row=5, column=0)
#
        ## Botón para limpiar las entradas
        #self.clear_button = ttk.Button(self.root, text="Limpiar", command=self.limpiar_entradas)
        #self.clear_button.grid(row=5, column=1)
#
        ## Crear el contenedor de resultados una sola vez
        #self.resultado_label_frame = ttk.LabelFrame(self.root, text="Resultados")
        #self.resultado_label_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        #self.result_label = ttk.Label(self.resultado_label_frame, text="", justify=LEFT)
        #self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky=W)

    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    
    mi_app = App()
    mi_app.run()


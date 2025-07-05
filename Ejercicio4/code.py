import math
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip


class Programador:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class EquipoMaraton:
    def __init__(self, nombre="", universidad=""):
        self.nombre = nombre
        self.universidad = universidad
        self.programadores = [None] * 3
        self.tamaño_maximo = len(self.programadores)

    def agregar_programador(self, programador):
        self.programadores.append(programador)

    def mostrar_programadores(self):
        for programador in self.programadores:
            print(f"{programador.nombre} {programador.apellido}")

    def esta_lleno(self):
        return len(self.programadores) == self.tamaño_maximo

    def validar_campo(self, valor_campo: str) -> bool:
        if not valor_campo:
            return False

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
        self.equipo = EquipoMaraton()

        self.setup_ui()

    def setup_ui(self):
        # Seccion para la información del equipo
        team_info_label_frame = ttk.LabelFrame(self.root, text="Información del Equipo")
        team_info_label_frame.pack(padx=15, pady=15, fill=X)

        ttk.Label(team_info_label_frame, text="Nombre del Equipo").pack(
            padx=10, pady=0, anchor=W
        )
        self.team_name_entry = ttk.Entry(team_info_label_frame)
        self.team_name_entry.pack(padx=10, pady=10, fill=X)

        universities = [
            "Universidad Nacional de Colombia (UNAL)",
            "Universidad de Antioquia (UDEA)",
            "Universidad abierta y a Distancia (UNAD)"
            "Universidad de los Andes (UNIANDES)",
        ]
        ttk.Label(team_info_label_frame, text="Universidad").pack(
            padx=10, pady=0, anchor=W
        )
        self.university_entry = ttk.Combobox(team_info_label_frame, values=universities, state="readonly")
        self.university_entry.current(0)  # Selecciona el primer elemento por defecto
        self.university_entry.pack(padx=10, pady=10, fill=X)

        # Sección para la información de los programadores
        self.programmers_info_label_frame = ttk.LabelFrame(self.root, text="Información de los integrantes")
        self.programmers_info_label_frame.pack(side=LEFT, padx=15, pady=15, fill=BOTH)

        # Crear campos para los programadores
        self.programador_fields = [
            ttk.LabelFrame(
                self.programmers_info_label_frame, text=f"Programador {_ + 1}"
            )
            for _ in range(self.equipo.tamaño_maximo)
        ]

        for container in self.programador_fields:

            ttk.Label(container, text=f"Nombre").grid(sticky=W, row=0, column=0, padx=10, pady=0)
            ttk.Entry(container).grid(row=1, column=0, padx=10, pady=10)

            ttk.Label(container, text=f"Apellido").grid(sticky=W, row=0, column=1, padx=10, pady=0)
            ttk.Entry(container).grid(row=1, column=1, padx=10, pady=10)

            container.pack(padx=10, pady=5, fill=X)

        # Botones para agregar y quitar programadores
        actions_label_frame = ttk.LabelFrame(self.root, text="Acciones")
        add_member_button = ttk.Button(actions_label_frame, text="+", command=self.agregar_programador)
        add_member_button.pack(pady=10, padx=5, anchor=W)
        Hovertip(add_member_button, "Agregar un programador al equipo", hover_delay=100)

        remove_member_button = ttk.Button(actions_label_frame, text="-", command=self.quitar_programador)
        remove_member_button.pack(pady=10, padx=5, anchor=W)
        Hovertip(remove_member_button, "Quitar un programador al equipo", hover_delay=100)

        actions_label_frame.pack(side=TOP, padx=15, pady=15, fill=BOTH)

        # Botón para enviar el formulario
        ttk.Button(self.root, text="Enviar", command=self.submit_form).pack(pady=10)

    def agregar_programador(self):
        if self.equipo.esta_lleno():
            messagebox.showerror("Error", "No se pueden agregar más programadores")
        else:
            # Crear un nuevo contenedor
            new_container = ttk.LabelFrame(self.programmers_info_label_frame, text=f"Programador {len(self.programador_fields) + 1}")
            
            # Crear un nuevo campo para el nombre
            new_name_label = ttk.Label(new_container, text=f"Nombre")
            new_name_entry = ttk.Entry(new_container)
            new_name_label.grid(sticky=W, row=1, column=1, padx=10, pady=0)
            new_name_entry.grid(row=2, column=1, padx=10, pady=10)

            # Crear un nuevo campo para el apellido
            new_lastname_label = ttk.Label(new_container, text=f"Apellido")
            new_lastname_entry = ttk.Entry(new_container)
            new_lastname_label.grid(sticky=W, row=1, column=2, padx=10, pady=0)
            new_lastname_entry.grid(row=2, column=2, padx=10, pady=10)

            new_container.pack(padx=10, pady=5, fill=X)

            self.programador_fields.append(new_container)
            self.equipo.programadores.append(None)

    def quitar_programador(self):
        if len(self.programador_fields) > 2:
            # Eliminar el último campo de programador
            programmer_info_container = self.programador_fields.pop()
            programmer_info_container.destroy()
            self.equipo.programadores.pop()
        else:
            messagebox.showerror("Error", "El equipo debe tener al menos 2 integrantes")

    def submit_form(self):
        # Validar campos del equipo
        team_name = self.team_name_entry.get().strip()
        university_name = self.university_entry.get().strip()

        if not team_name or not university_name:
            messagebox.showerror(
                "Error",
                "Por favor, complete la información del equipo.",
            )
            return
        else:
            self.equipo.nombre = team_name
            self.equipo.universidad = university_name

        # Validar campos de los programadores
        for programador in self.programador_fields:
            _, name_entry, _, lastname_entry = programador.winfo_children()

            nombre = name_entry.get().strip()
            apellido = lastname_entry.get().strip()

            if self.equipo.validar_campo(nombre):
                if self.equipo.validar_campo(apellido):
                    programador = Programador(nombre, apellido)
                    self.equipo.programadores.pop()
                    self.equipo.agregar_programador(programador)
                else:
                    messagebox.showerror(
                        "Error",
                        f"El apellido '{apellido}' no es válido. No puede ser vacío, debe contener menos de 20 caracteres y no debe tener números.",
                    )
                    return
            else:
                messagebox.showerror(
                    "Error",
                    f"El nombre '{nombre}' no es válido. No puede ser vacío, debe contener menos de 20 caracteres y no debe tener números.",
                )
                return
            
        # Mostrar mensaje de éxito
        messagebox.showinfo(
            "Éxito",
            f"Equipo '{self.equipo.nombre}' de la {self.equipo.universidad} inscrito correctamente con {len(self.equipo.programadores)} programadores.",
        )

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    mi_app = App()
    mi_app.run()

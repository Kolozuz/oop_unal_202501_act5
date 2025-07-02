from tkinter import *

from tkinter import messagebox


class Ventana(Tk):

    def __init__(self):

        super().__init__()

        self.title("Interfaz de Vendedor")

        self.config(bg="lightblue")

        self.nombre_var = StringVar()

        self.apellido_var = StringVar()

        self.edad_var = StringVar()

        self.nombre = Label(self, text="Nombre")

        self.nombre.grid(row=0, column=0, padx=20, pady=20)

        self.nombre.config(bg="lightblue")

        self.apellido = Label(self, text="Apellido")

        self.apellido.grid(row=1, column=0, padx=20, pady=20)

        self.apellido.config(bg="lightblue")

        self.edad = Label(self, text="Edad")

        self.edad.grid(row=2, column=0, padx=20, pady=20)

        self.edad.config(bg="lightblue")

        self.entrada_nombre = Entry(self)

        self.entrada_nombre.grid(row=0, column=1, padx=20, pady=20)

        self.entrada_apellido = Entry(self)

        self.entrada_apellido.grid(row=1, column=1, padx=20, pady=20)

        self.entrada_edad = Entry(self)

        self.entrada_edad.grid(row=2, column=1, padx=20, pady=20)

        self.mostrar = Button(self)

        self.mostrar.config(text="Mostrar", command=self.mostrar_mensaje)

        self.mostrar.grid(row=3, column=0, padx=20, pady=20)

        self.borrar = Button(self)

        self.borrar.config(text="Borrar", command=self.limpiar)

        self.borrar.grid(row=3, column=1, padx=20, pady=20)

        self.muestra_1 = Entry(self)

        self.muestra_1.grid(row=0, column=2, columnspan=2, padx=20, pady=20)

        self.muestra_1.config(state="disabled")

        self.muestra_1.config(textvariable=self.nombre_var)

        self.muestra_2 = Entry(self)

        self.muestra_2.grid(row=1, column=2, columnspan=2, padx=20, pady=20)

        self.muestra_2.config(state="disabled")

        self.muestra_2.config(textvariable=self.apellido_var)

        self.muestra_3 = Entry(self)

        self.muestra_3.grid(row=2, column=2, columnspan=2, padx=20, pady=20)

        self.muestra_3.config(state="disabled")

        self.muestra_3.config(textvariable=self.edad_var)

        self.mensaje = Label(self, text="La edad no puede ser negativa ni mayor a 120")

        self.mensaje.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        self.mensaje.config(bg="lightblue")

    def mostrar_mensaje(self):

        nombre = self.entrada_nombre.get()

        apellido = self.entrada_apellido.get()

        if not nombre or not apellido:

            messagebox.showerror("Error", "Uno o más campos nulos")

        else:

            self.nombre_var.set(nombre)

            self.apellido_var.set(apellido)

        try:

            edad = int(self.entrada_edad.get())

            if edad >= 0 and edad < 18:

                messagebox.showerror("Error", "El vendedor debe ser mayor de 18 años")

                self.mensaje.config(text="El vendedor debe ser mayor de 18 años")

            elif edad >= 0 and edad <= 120:

                self.edad_var.set(edad)

            else:

                messagebox.showerror(
                    "Error", "La edad no puede ser negativa ni mayor a 120"
                )

                self.mensaje.config(text="La edad no puede ser negativa ni mayor a 120")

        except ValueError:

            messagebox.showerror(
                "Error", "Campo de edad nulo o formato de edad no válido."
            )

        except Exception:

            messagebox.showerror("Error", "Ocurrió un error inesperado.")

    def limpiar(self):

        self.entrada_nombre.delete(0, END)

        self.entrada_apellido.delete(0, END)

        self.entrada_edad.delete(0, END)

        self.nombre_var.set("")

        self.apellido_var.set("")

        self.edad_var.set("")


class Principal:

    def main(self):

        ventana = Ventana()

        ventana.mainloop()


if __name__ == "__main__":

    interfaz = Principal()

    interfaz.main()

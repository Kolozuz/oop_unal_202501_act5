from tkinter import *

from tkinter import messagebox

import math


class Ventana(Tk):

    def __init__(self):

        super().__init__()

        self.title("Cálculos Numéricos")

        self.config(bg="lightblue")

        self.valor_var = StringVar()

        self.raiz_var = StringVar()

        self.log_var = StringVar()

        self.valor = Label(self, text="Valor")

        self.valor.grid(row=0, column=0, padx=20, pady=20)

        self.valor.config(bg="lightblue")

        self.log = Label(self, text="Logaritmo")

        self.log.grid(row=1, column=0, padx=20, pady=20)

        self.log.config(bg="lightblue")

        self.raiz = Label(self, text="Raíz")

        self.raiz.grid(row=2, column=0, padx=20, pady=20)

        self.raiz.config(bg="lightblue")

        self.entrada_valor = Entry(self)

        self.entrada_valor.grid(row=0, column=1, padx=20, pady=20)

        self.muestra_raiz = Entry(self)

        self.muestra_raiz.grid(row=2, column=1, padx=20, pady=20)

        self.muestra_raiz.config(state="disabled", textvariable=self.raiz_var)

        self.muestra_log = Entry(self)

        self.muestra_log.grid(row=1, column=1, padx=20, pady=20)

        self.muestra_log.config(state="disabled", textvariable=self.log_var)

        self.mensaje_1 = Label(self, text="")

        self.mensaje_1.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        self.mensaje_1.config(bg="lightblue")

        self.mensaje_2 = Label(self, text="")

        self.mensaje_2.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

        self.mensaje_2.config(bg="lightblue")

        self.calcular_logaritmo = Button(self)

        self.calcular_logaritmo.config(
            text="Calcular Logaritmo", command=self.calcular_log
        )

        self.calcular_logaritmo.grid(row=3, column=0, padx=20, pady=20)

        self.calcular_raiz = Button(self)

        self.calcular_raiz.config(
            text="Calcular Raíz", command=self.calcular_raiz_cuadrada
        )

        self.calcular_raiz.grid(row=3, column=1, padx=20, pady=20)

        self.borrar = Button(self)

        self.borrar.config(text="Borrar", command=self.limpiar)

        self.borrar.grid(row=3, column=2, padx=20, pady=20)

    def calcular_log(self):

        valor = self.entrada_valor.get()

        if not valor:

            messagebox.showerror("Error", "Campo nulo")

            return

        try:

            valor = float(self.entrada_valor.get())

            if valor < 0:

                raise ArithmeticError("El valor debe ser un número positivo")

            elif valor == 0:

                self.mensaje_1.config(
                    text="Error: El valor debe ser distinto de 0 para calcular el logaritmo"
                )

            else:

                resultado_1 = round(math.log(valor), 2)

                self.log_var.set(resultado_1)

        except ArithmeticError:

            self.mensaje_1.config(
                text="Error: el valor debe ser un número positivo para calcular el logaritmo"
            )

        except ValueError:

            self.mensaje_1.config(
                text="Error: el valor debe ser numérico para calcular el logaritmo"
            )

    def calcular_raiz_cuadrada(self):

        valor = self.entrada_valor.get()

        if not valor:

            messagebox.showerror("Error", "Campo nulo")

            return

        try:

            valor = float(self.entrada_valor.get())

            if valor < 0:

                raise ArithmeticError("El valor debe ser un número positivo")

            else:

                resultado_2 = round(math.sqrt(valor), 2)

                self.raiz_var.set(resultado_2)

        except ArithmeticError:

            self.mensaje_2.config(
                text="Error: el valor debe ser un número positivo para calcular la raíz cuadrada"
            )

        except ValueError:

            self.mensaje_2.config(
                text="Error: el valor debe ser numérico para calcular la raíz cuadrada"
            )

    def limpiar(self):

        self.entrada_valor.delete(0, END)

        self.log_var.set("")

        self.raiz_var.set("")


class Principal:

    def main(self):

        ventana = Ventana()

        ventana.mainloop()


if __name__ == "__main__":

    interfaz = Principal()

    interfaz.main()

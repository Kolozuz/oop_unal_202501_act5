from tkinter import *

from tkinter import messagebox

class Ventana(Tk):

    def __init__(self):

        super().__init__()

        self.title("Calculadora")

        self.config(bg="lightblue")

        self.resultado_var = StringVar()

        self.numerador = Label(self, text="Numerador")

        self.numerador.grid(row=0, column=0, padx=20, pady=20)

        self.numerador.config(bg="lightblue")

        self.denominador = Label(self, text="Denominador")

        self.denominador.grid(row=1, column=0, padx=20, pady=20)

        self.denominador.config(bg="lightblue")

        self.resultado = Label(self, text="Resultado")

        self.resultado.grid(row=2, column=0, padx=20, pady=20)

        self.resultado.config(bg="lightblue")

        self.entrada_numerador = Entry(self)

        self.entrada_numerador.grid(row=0, column=1, padx=20, pady=20)

        self.entrada_denominador = Entry(self)

        self.entrada_denominador.grid(row=1, column=1, padx=20, pady=20)

        self.salida_resultado = Entry(self)

        self.salida_resultado.grid(row=2, column=1, padx=20, pady=20)

        self.salida_resultado.config(state="disabled")

        self.salida_resultado.config(textvariable=self.resultado_var)

        self.calcular = Button(self)

        self.calcular.config(text="Calcular", command=self.calcular_division)

        self.calcular.grid(row=3, column=0, padx=20, pady=20)

        self.borrar = Button(self)

        self.borrar.config(text="Borrar", command=self.limpiar)

        self.borrar.grid(row=3, column=1, padx=20, pady=20)

    def calcular_division(self):

        try:

            numerador = float(self.entrada_numerador.get())

            denominador = float(self.entrada_denominador.get())

            resultado = numerador / denominador

            self.resultado_var.set(round(resultado, 2))

        except ZeroDivisionError:

            messagebox.showerror("Error", "No es posible realizar una división por 0.")

        except ValueError:

            messagebox.showerror("Error", "Campo nulo o formato de entrada no válido.")

        except Exception:

            messagebox.showerror("Error", "Ocurrió un error inesperado.")

    def limpiar(self):

        self.entrada_numerador.delete(0, END)

        self.entrada_denominador.delete(0, END)

        self.resultado_var.set("")


class Principal:

    def main(self):

        ventana = Ventana()

        ventana.mainloop()


if __name__ == "__main__":

    interfaz = Principal()

    interfaz.main()

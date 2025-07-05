## Ejercicio 6.6. `Catchs` múltiples (p. 410)

### Objetivos de aprendizaje
Al finalizar este ejercicio, el lector tendrá la capacidad para:

- Definir múltiples catch para el tratamiento de excepciones.
- Definir gestores para el tratamiento de excepciones aritméticas.

### Enunciado: clase CálculosNuméricos
Se requiere definir una clase denominada CálculosNúmericos que realice las siguientes operaciones:

- Calcular el logaritmo neperiano recibiendo un valor double como parámetro. Este método debe ser estático. Si el valor no es positivo
se genera una excepción aritmética.
- Calcular la raíz cuadrada recibiendo un valor double como parámetro. Este método debe ser estático. Si el valor no es positivo se genera una excepción aritmética.
Se debe crear un método main que utilice dichos métodos ingresando
un valor por teclado.

### Diagrama de Casos de uso

![alt text](media/ejer3act5.svg)

### Diagrama de Clases

![alt text](media/image-5.png)

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio3/code.py)

#### Ejecución del programa

**Sin ingresar un valor**

![alt text](media/image.png)

**Ingresando un valor negativo**

![alt text](media/image-1.png)

**Ingresando 0 como valor**

![alt text](media/image-2.png)

**Ingresando un valor no válido**

![alt text](media/image-3.png)

**Ingresando un valor válido**

![alt text](media/image-4.png)
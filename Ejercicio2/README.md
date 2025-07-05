## Ejercicio 6.5. Lanzamiento de excepciones (p. 404)

### Objetivos de aprendizaje
Al finalizar este ejercicio, el lector tendrá la capacidad para:

- Lanzar excepciones específicas en métodos de una clase.
- Conocer y aplicar la sentencia throw para el lanzamiento de excepciones.

### Enunciado: clase Vendedor
Se requiere implementar una clase vendedor que posee los siguientes atributos: nombre (tipo String), apellidos (tipo String) y edad (tipo int).
La clase contiene un constructor que inicialice los atributos de la clase. Además, la clase posee los siguientes métodos:

- Imprimir: muestra por pantalla los valores de sus atributos.
- Verificar edad: este método recibe como parámetro un valor entero que representa la edad del vendedor. Para que un vendedor
pueda desempeñar sus labores se requiere que sea mayor de edad
(mayor de 18 años). Si esta condición no se cumple, se lanza una
excepción de tipo IllegalArgumentException con el mensaje "El vendedor debe ser mayor de 18 años". Además, se evalúa si la edad se encuentra en el rango de 0 a 120, si no se cumple, se genera
una excepción de tipo IllegalArgumentException con el mensaje "La
edad no puede ser negativa ni mayor a 120". Si la edad cumple
estos requerimientos se pueden instanciar el objeto vendedor.

Además, se requiere que los datos del vendedor se ingresen por teclado.

### Diagrama de Casos de uso

![alt text](media/ejer2act5.svg)

### Diagrama de Clases

![alt text](media/image-11.png)

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio2/code.py)

#### Ejecución del programa

**Sin ingresar ningún valor**

![alt text](media/image.png)

![alt text](media/image-1.png)

**Ingresando solamente un valor**

![alt text](media/image-2.png)

![alt text](media/image-3.png)

**Ingresando un número negativo**
![alt text](media/image-4.png)

**Ingresando un número menor a 18 y mayor o igual a 0**

![alt text](media/image-5.png)

![alt text](media/image-9.png)

**Ingresando un número mayor a 120**

![alt text](media/image-6.png)

![alt text](media/image-7.png)

**Ingresando un valor no válido**

![alt text](media/image-8.png)

**Ingresando un valor válido**

![alt text](media/image-10.png)
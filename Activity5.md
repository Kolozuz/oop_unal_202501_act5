## Ejercicio 1

### Enunciado



### Diagrama de Casos de uso



### Diagrama de Clases

![alt text](Ejercicio1/image.png)

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio1/code.py)

#### Ejecución del programa

**Sin ingresar un valor**
![alt text](Ejercicio1/media/image.png)

**Ingresando solamente un valor no válido**
![alt text](Ejercicio1/media/image-1.png)

**Ingresando solamente un valor válido/numérico**
![alt text](Ejercicio1/media/image-2.png)

**Ingresando 0 como denominador**
![alt text](Ejercicio1/media/image-3.png)

**Ingresando valores válidos**
![alt text](Ejercicio1/media/image-4.png)

## Ejercicio 2

### Enunciado



### Diagrama de Casos de uso



### Diagrama de Clases

![alt text](Ejercicio2/image.png)

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio2/code.py)

#### Ejecución del programa

**Sin ingresar ningún valor**

![alt text](Ejercicio2/media/image.png)

![alt text](Ejercicio2/media/image-1.png)

**Ingresando solamente un valor**

![alt text](Ejercicio2/media/image-2.png)

![alt text](Ejercicio2/media/image-3.png)

**Ingresando un número negativo**
![alt text](Ejercicio2/media/image-4.png)

**Ingresando un número menor a 18 y mayor o igual a 0**

![alt text](Ejercicio2/media/image-5.png)

![alt text](Ejercicio2/media/image-9.png)

**Ingresando un número mayor a 120**

![alt text](Ejercicio2/media/image-6.png)

![alt text](Ejercicio2/media/image-7.png)

**Ingresando un valor no válido**

![alt text](Ejercicio2/media/image-8.png)

**Ingresando un valor válido**

![alt text](Ejercicio2/media/image-10.png)

## Ejercicio 3

### Enunciado



### Diagrama de Casos de uso



### Diagrama de Clases

![alt text](Ejercicio3/image.png)

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio3/code.py)

#### Ejecución del programa

**Sin ingresar un valor**

![alt text](Ejercicio3/media/image.png)

**Ingresando un valor negativo**

![alt text](Ejercicio3/media/image-1.png)

**Ingresando 0 como valor**

![alt text](Ejercicio3/media/image-2.png)

**Ingresando un valor no válido**

![alt text](Ejercicio3/media/image-3.png)

**Ingresando un valor válido**

![alt text](Ejercicio3/media/image-4.png)

## Ejercicio 6.7. Validación de campos (p. 417)

Las excepciones se pueden utilizar para validar el formato de campos de entrada. Por ejemplo:
- Restringir que un campo de entrada de datos sea numérico, alfabético, alfanumérico, etc.
- Restringir la cantidad de caracteres que debe tener un campo de entrada de datos.
- Impedir que se ingresen fechas anteriores a la fecha actual.
- Definir campos obligatorios en un formulario de tal manera que no reciba valores vacíos.
- Definir restricciones especiales de los campos de entrada. Por ejemplo, si es un correo electrónico, que tenga el carácter @.

Para estos casos, si se presentan situaciones que no cumplen dichas condiciones se debe generar la excepción correspondiente.

### Objetivo de aprendizaje

Al finalizar este ejercicio, el lector tendrá la capacidad para definir métodos que realicen validación de campos y generen las excepciones apropiadas en caso de que no se cumplan las condiciones estipuladas en los requisitos de un programa.

### Enunciado: clase EquipoMaratónProgramación

Un equipo de programadores desea participar en una maratón de programación. El equipo tiene los siguientes atributos:
- Nombre del equipo (tipo String).
- Universidad que está representando el equipo (tipo String).
- Lenguaje de programación que va a utilizar el equipo en la competencia (tipo String).
- Tamaño del equipo (tipo int).

Se requiere un constructor que inicialice los atributos del equipo. El equipo está conformado por varios programadores, mínimo dos y máximo tres. Cada programador posee nombre y apellidos (de tipo String). Se requieren además los siguientes métodos:
- Un método para determinar si el equipo está completo.
- Un método para añadir programadores al equipo. Si el equipo está lleno se debe imprimir la excepción correspondiente.
- Un método para validar los atributos nombre y apellidos de un programador para que reciban datos que sean solo texto. Si se reciben datos numéricos se debe generar la excepción correspondiente. Además, no se permiten que los campos String tengan una longitud igual o superior a 20 caracteres.
- En un método main se debe crear un equipo solicitando sus datos por teclado y se validan los nombres y apellidos de los programadores.

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio4/code.py)

#### Ejecución del programa



## Ejercicio 3

### Enunciado



### Diagrama de Casos de uso

![alt text](Ejercicio5/image.png)

### Diagrama de Clases



### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio5/code.py)

#### Ejecución del programa

**Interfaz gráfica**

![alt text](Ejercicio5/media/image.png)

**Cuando el archivo de prueba está en la misma ubicación del trabajo con el código**

![alt text](Ejercicio5/media/image-1.png)

**Cuando el archivo de prueba NO está en la misma ubicación del trabajo con el código**

![alt text](Ejercicio5/media/image-2.png)
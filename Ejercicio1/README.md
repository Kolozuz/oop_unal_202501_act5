## Ejercicio 6.4 Excepciones (p. 399)

Las excepciones son un mecanismo especial para gestionar errores y permiten separar el tratamiento de errores del código normal de un programa (Kölling y Barnes, 2013).
El formato para escribir un bloque en el que se gestionan excepciones es:

```java
try {
    instrucciones
} catch {
    instrucciones
} finally {
    instrucciones
}
```

Dentro del bloque try se coloca el código que podría generar una excepción. Los bloques catch capturan y tratan una excepción cuando esta ocurre. Pueden existir varios bloques catch. Estos se definen directamente después del bloque try. Ningún código puede estar entre el final del bloque try y el comienzo del primer bloque catch. Los catch se evalúan por orden, si un catch atrapa la excepción que ha ocurrido, se ejecuta y los demás no.
Por último, el bloque finallly es opcional e incluye código que se ejecuta siempre, independientemente si se ha producido una excepción o no (Altadill-Izurra y Pérez-Martínez, 2017).

### Objetivos de aprendizaje
Al finalizar este ejercicio, el lector tendrá la capacidad para:

- Identificar bloques de código donde se pueden generar excepciones.
- Identificar los bloques catch que capturan una excepción específica.
- Reconocer y diferenciar los propósitos de los bloques try, catch y finally para la gestión de excepciones.

### Diagrama de Casos de uso

![alt text](media/ejer1act5.svg)

### Diagrama de Clases

![alt text](media/image-5.png)

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio1/code.py)

#### Ejecución del programa

**Sin ingresar un valor**
![alt text](media/image.png)

**Ingresando solamente un valor no válido**
![alt text](media/image-1.png)

**Ingresando solamente un valor válido/numérico**
![alt text](media/image-2.png)

**Ingresando 0 como denominador**
![alt text](media/image-3.png)

**Ingresando valores válidos**
![alt text](media/image-4.png)

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

### Diagrama de Casos de uso

![alt text](media/image.svg)

### Diagrama de Clases

```mermaid
classDiagram
    class Programador {
        +nombre: str
        +apellido: str
        «constructor»Programador(nombre: str, apellido: str)
    }
    class EquipoMaraton {
        +nombre: str
        +universidad: str
        +programadores: list[Programador]
        +tamaño_maximo: int
        «constructor»EquipoMaraton(nombre: str, universidad: str)
        +agregar_programador(programador: Programador)
        +esta_lleno() bool
        +validar_campo(valor_campo: str) bool
    }
    class App {
        +root: Tk
        +team_name_entry
        +university_entry
        +programmers_info_label_frame
        +programador_fields
        +equipo: EquipoMaraton
        «constructor»App()
        +setup_ui()
        +agregar_programador()
        +quitar_programador()
        +submit_form()
        +run()
    }

    EquipoMaraton o-- Programador : contiene
    App o-- EquipoMaraton : crea/usa
```

### Solución

[Click para ver código fuente](https://github.com/Kolozuz/oop_unal_202501_act5/blob/main/Ejercicio4/code.py)

#### Ejecución del programa

**Cuando no se llena la información del equipo**

![alt text](media/image.png)

**Cuando se deja vacío alguno de los campos de los integrantes**

![alt text](media/image-1.png)

**Cuando alguno de los campos de los integrantes contiene dígitos**

![alt text](media/image-2.png)

**Cuando alguno de los campos de los integrantes tiene mas de 19 caracteres**

![alt text](media/image-3.png)

**Cuando la ejecucion es correcta**

![alt text](media/image-4.png)
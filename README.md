# Python_curso

## Curso Santander
- Luis Enrique Namigtle Jimenez

## 1. Introducción a Python
Python se diseño con el objetivo de ser un lenguaje fácil de leer y escribir con una sintaxis clara y concisa.

### Características
- Legibilidad : Utiliza una sintaxis clara y sencilla para facilitar la lectura y compresión del código.
- Multiplataforma : Se puede ejecturar en diferentes sistemas operativos como Windows, macOs y Linux.
- Tipado dinámico : No es necesita declarar explícitamente el tipo de datos de las variables.
- Aplicaciones : Desarrollo web, Ciencia de datos, Inteligencia Artificial, Automatización de tareas, desarrollo de juegos etc.

### Indentación
La indentación (espacios o tabulaciones al inicio de una línea) se utiliza para delimitar bloques de código es decir, Python utiliza la indentación para determinar el alcance de las declaraciones. El siguiente ejemplo se muestra utilizando un if.

```python
if condicion:
    instruccion_1
    instruccion_2
else :
    instruccion_3
    instruccion_4
```
### Comentarios
Los comentarios son líneas de texto en el código que son ignorados por el intérprete de Python. Es utilizado para explicar o documentar el código. Para hacer comentarios en Python basta con colocar el simbolo #, mientras que para comentarios de varias líneas se encierran entre triles comillas """. Veamos el ejemplo

```Python
#Este es un comentarios de python usando una línea

"""
Este es un comentarios de python
usando dos líneas
"""

```

## 2.1 Variables
Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas.

### Declaración de variables
Para declarar una variable y asignar un valor, utilizamos el operados de asignacion "=" por ejemplo:

```python
nombre = "Luis"
edad= 25
Sexo = "Masculino"
a=b=c= True
```
Python automáticamente infiere en el tipo de datos de cada variable en función del valor asignado.

### Normas para nombrar variables
Algunas reglas que se recomiendan al momento de usar las variables son las siguientes :
- No pueden comenzar con un número las variables.
- No se pueden utilizar palabras clave reservadas de Python como nombres de variables (por ejemplo, if,else,for,while,etc)
- Python distingue entre mayúsculas y minúsculas, por lo que "Edad", "edad", "EDAD" son variables diferentes.

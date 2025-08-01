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

### Sensibilidad a mayúsculas y minúsculas

Python es sensible para distinguir entre mayúsculas y minúsculas. 

### Punto y coma
Python no requiere el uso de punto y coma (;) al final de cada instrucción, pero si se necesita escribir varias instrucciones en una sola línea, puedes separarlas con punto y coma. Por ejemplos

```Python
instruccion_1; instruccion_2; instruccion_3
```
## 2. Fundamentos de Python 

### Enteros (int)
Los números enteros son aquellos que no tienen parte decimal.  Ejemplo

```Python
a = 25
b = 25
```

### Flotante (float)

Los números flotantes, también conocidos como números de punto flotante, son aquellos que tienen una parte decimal. Ejemplo

```Python
a = 25.55
b = 25.99
```

### Cadenas de texto (string)

Las cadenas de texto son secuencias de caracteres encerradas entre comillas simplres ('') o dobles (" "). Ejemplo

```Python
nombre = "Luis"
apellido = "Namigtle"
```

### Booleanos (True/False)
Se utilizan comúnmente en expresiones condicionales y operaciones lógicas. Ejemplo

```Python
uno_es_mayor_de_dos = True
dos_es_menor_que_uno = False
```
Las expresiones booleanas en Python, siempre comienza con una letra mayúscula.

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

### 2.2 Operadores 

## Aritmeticos
Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas. Los principales operadores aritméticos son:

- **Suma(+) :** suma de dos valores.
- **Resta (-) :** resta el segundo valor del primero.
- **Multiplicación (*) :** multiplica dos valores.
- **División (/) :** divide el primer valor por el segundo y devuelve el resultado de tipo flotante.
- **División (//) :** divide el primer valor por el segundo y devuelve el un resultado de tipo entero (se descarta la parte decimal).
- **Modulo (%) :** devuelve el resto de la división entre el primer valor y el segundo.
- **Exponenciación (**) :** elevar el primer valro a la potencia del segundo.

Ejemplo :

```Python
a = 100
b = 100

suma = a + b
resta = a - b
mutiplicacion = a * b
division_flotante = a / b
division_entera = a // b
modulo = a % b
exponente = a ** b
```
```verilog

module cand(
    input a,
    input b,
    output c

)

endmodule

```
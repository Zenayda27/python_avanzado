## recursividad en python 

# definicion
La recursividad en Python es una técnica de programación en la que una función se llama a sí misma para resolver un problema poco a poco, hasta llegar a una condición que detiene las llamadas.
2. Características
Función recursiva: es una función que se llama a sí misma.
Caso base: es la condición que detiene la recursividad.
Caso recursivo: es la parte donde la función vuelve a llamarse.

# ejemplos en codigo

1. Ejemplos en código
Este código puedes copiarlo y pegarlo en Python:
Resultado:

```python
def contar(n):
    if n == 0:  # Caso base
        print(0)
    else:
        print(n)
        contar(n - 1)  # Llamada recursiva

contar(5)
```

## conociendo mas sobre funciones parametros y argumentos 
sobre los parametros / argumentos nominales es ampliamente usado para distintos configuraciones y que se puede pasar solo los argumentos que se usaran y dejar los parametros por defecto si no se van a modificar.
```python
# tenemos una programa que me permite accede a internet que tiene parametros por defecto, sin embargo si se actualiza uno de los accesos se podra modificar el valor.
## primer caso accesos por defecto
def config (user="admin",pass="1234",port="8080",BSSID=wifi"):
    return "conectado a la red"
config()
## segundo caso 1 BSSID cambi por el de "laboratorio1"
def config (user="admin",pass="1234",port="8080",BSSID=wifi"):
    return "conectado a la red"

config (BSSID="laboratorio")

## reyner desea conectar al wifi de ana luz, pregunta como se llama tu wifi y cual es la contraseña. respuesta le dice el wifi es A56 y su contraseña es 12345678
def config (user="admin",pass="1234",port="8080",BSSID=wifi"):
    return "conectado a la red"
    config (BSSID="A56",pass="12345678")
```
### conociendo *args y **kargs (empaquetado y desempaquetado de argumentos posicionales )

esta tecnica nos permite empaquetar nuestros argumentos cuando no sabemos la cantidad de datos que vamos a pasar. imaginemos que nos piden una funcion para sumar cantidad de nuemeros la solucion seria empaquetar los argumentos y luego desempaquetar para ello en la definicion de la funcion dentro de los parametros debemos usar el operardor `*` delante del nombre del parametro posicional esto hara que todos los argumentos se almacenan en una tupla`()` (lista`[]`) esto nos permite recorer dentro de sus elementos para poder desempaquetarlo y realizar las operaciones secesarias.
```python
# deseamos crear una funcion que nos permita sumar n cantidad de  numeros 
# n es un numero variable puede ser 3, 7, 8.....n
def suma(*args):
    #*args = (2,5,7,8,9)
    acumulado =0
    for i in args:
        acumulado +=i
    return acumulado 
print(suma(2,5,7,8,9))
```
###  desempaquetando argumentos nominales
### desempaquetando argumentos nominales

En este caso, como en el anterior, utilizaremos el operador **,
la casuística es la misma, sin embargo, para desempaquetar
 argumentos nominales usaremos ** delante del nombre del parámetro
nominal, a diferencia del anterior esto se empaquetará en un
 diccionario {"clave": "valor"}.

# encontrar la persona con mayor calificación.
```python
def mejor_alumno(**kwargs):
    # **kwargs={"noemi":18,"eduardo":18,"david":19}
    nota_maxima = -1

    for alumno, nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno

    return mejor_alumno

mejor_alumno(noemi=20, eduardo=18, david=19)
 Resultado:
 ```

 ## Funciones Anonimas 
 las funciones anonimas en python son llamdas `lambda`, estas funciones tiene las siguientes propiedades:
 1. se escribe en una unica sentencia `(lineal)`
 2. no tiene nombre `(anonima)`
 3. su cuerpo conlleva un `(return)` implicito
 4. puede recibir cualquier numero de parametros 
La escructura para definir una funcion `lambda` es la siguiente:
1. escribir la plabra reservada `lambda` 
2. especificar la cantidad de parametros.
3. indicar los datos de retorno 
```python
lambda a,b: a+b
```
> [!TIP] Puesto que esta funcion es anonima para ejecutar debempos almacenar la funcion en una variable.
 ```python
suma=lambda a,b: a+b
suma(3,6)
```

## documentacion 
python nos permite documentar una funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para esto usamos una cadena de texto despues de la definicion de una funcion, a esta cadena de texto se le conoce como `docstring` y esta delimitado por triples `""" aqui el texto"""`.
```python
def suma (a,b):
    """
    funcion para realizar la suma de dos numeros
    """
## los docstring tambien nos permite explicar los parametros que r4ecibe y los datos de salida
def resta (a,b):
    """
    a= un numero entero.
    b= un numero entero.
    en ambos casos a,b no deben recibir vaalores menores 0.
    retornara un dato entero <int> positivo
    """
    return a-b
```
> [!WARNING] en el proceso de documentacion tener en cuenta de incluir a lo menos lo siguiente:
 1. breve explicacion sobre que hace la funcion
 2. especificaciones y caracteristicas de los parametros incluyendo sus tipos 
3. restricciones de la funcion
4. el valor que retorna y sus caracteristicas



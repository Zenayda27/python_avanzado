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
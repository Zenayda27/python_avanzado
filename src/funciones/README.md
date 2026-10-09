# Funciones en python 
las funciones nos perimten ordeanr mejor el codigo y reutilizarlo cuando sea ncesario 
```python
# ejemplo deseamos crear un programa en python que nos permite sumar dos numeros 
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```

como hacemos reutilizable el ejercicio anterior y mas lejible.
para eso utilizaremos funciones
la caracteristica de un afuncion en python es la siguiente:
1. debe comenzar con la p'alabra reservada `def`.
2. debe tener un nombre que de a entender que realizara la funcion.
3. debera tener parametros y estos estaran encerrados en parametros aun asi debera tener los `()`
4. las funciones deberan retomar datos a travez de la palabra reservada `return`

```python
#crear un programa que me permita sumar dos numeros 
def sumar(a:int,b:int):
    return a+b
print(sumar(78,56))
print(sumar(78,56))
```
## funciones avanzadas
existen dos grandes coneceptos para poder entender el uso avanzado de las funciones:
1. arguemntos, parametros posicionales y nominales, *args y +kargas.
2. anotaciones en la salida de una funcion.
3. recursividad.
```python
# anotacion en una funcion 
def suma(a:int,b:float)->int:
    return a+b
# crear una funcion que revisa cuatro numeros enteros como salida que me muestre los 4 numeros enteros en una lista
def numeros_enteros(a:int,b:int,c:int,d:int)->list[int]:
    return [a,b,c,d]
```
**Argumentos Parametros**
```python

















```
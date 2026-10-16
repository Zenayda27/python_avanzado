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
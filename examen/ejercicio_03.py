### Type-hints (Anotaciones de tipo)

Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) y retorne un número flotante (float) que represente el promedio de los valores. Incluye las anotaciones de tipo estrictas vistas en el apunte.

```PYTHON
def obtener_promedio(numeros: list[int]) -> float:
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio

notas = [15, 18, 16, 14, 17]

resultado = obtener_promedio(notas)

print("El promedio es:", resultado)
```
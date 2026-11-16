### Documentación (docstring)

Crea una función llamada calcular_potencia(base: float, exponente: float) -> float que eleve un número a su potencia. Añade un docstring completo que cumpla estrictamente con la advertencia del apunte: 
```Python
def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número.

    Args:
        base (float): Número que se va a elevar.
        exponente (float): Potencia a la que se eleva la base.

    Returns:
        float: Resultado de la potencia.
    """
    resultado = base ** exponente
    return resultado


# Llamamos a la función
resultado = calcular_potencia(2.0, 3.0)

print("El resultado de la potencia es:", resultado)

```
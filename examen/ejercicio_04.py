### Empaquetado Posicional (*args) 

Crea una función llamada unir_frases(*args) que reciba una cantidad variable de cadenas de texto (str) y las una en una sola oración separadas por un espacio, retornando el resultado final. 

```Python
def unir_frases(*args):
    resultado = " ".join(args)
    return resultado

frase = unir_frases("Hola", "mi", "nombre", "es", "Abel")

print("Frase completa:", frase)


```
### Closure (Clausura)
Escribe una función externa llamada crear_validador_limite(limite_maximo: int) que retorne una función interior. Esta función interior debe recibir un número y retornar True si es menor o igual al limite_maximo, o False si lo supera. Pon a prueba tu closure creando un validador con límite 100. 

```Python
def crear_validador_limite(limite_maximo: int):
    def validar(numero: int) -> bool:
        return numero <= limite_maximo

    return validar


# Creamos un validador con límite de 100
validador = crear_validador_limite(100)

# Probamos la función
print("El número 80 es válido:", validador(80))
print("El número 100 es válido:", validador(100))
print("El número 150 es válido:", validador(150))

```
### Empaquetado Nominal (**kwargs)


Diseña una función llamada generar_perfil_usuario(**kwargs) que reciba datos arbitrarios en formato clave-valor (como nombre, edad, país, profesión) y devuelva una cadena de texto descriptiva que recorra el diccionario armado e imprima cada característica del usuario. 

```Python
def generar_perfil_usuario(**kwargs):
    perfil = "Perfil del usuario:\n"

    for clave, valor in kwargs.items():
        perfil += f"{clave}: {valor}\n"

    return perfil

resultado = generar_perfil_usuario(
    nombre="Abel",
    edad=20,
    pais="Peru",
    profesion="Estudiante"
)

print(resultado)

```
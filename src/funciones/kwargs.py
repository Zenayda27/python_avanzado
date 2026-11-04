# crear una funcion que me permita saber de una lista de ingredientes cual es el mayor precio
#ejemplo:
# entrada: ajo=2 , papa=3, aceite=8
# salida: el ingrediente de mayor precio es aceite 
# Crear una funcion que permita saber
# cual ingrediente tiene el mayor precio

def mayor_precio(**kwargs):
    precio_maximo = -1

    for ingrediente, precio in kwargs.items():
        if precio > precio_maximo:
            precio_maximo = precio
            ingrediente_maximo = ingrediente

    return ingrediente_maximo


# Llamar a la funcion
print(mayor_precio(ajo=2, papa=3, aceite=8)) 
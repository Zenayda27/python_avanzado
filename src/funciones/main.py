# crear un programa que me permita mostrar mensajes personalizados, crear una funcion similar a la funcion print de python

def mensaje(texto:str):
    print("Mensaje personalizado:", texto)
    texto=f"""
    -----------------------------------------
    {mensaje}
    --------------------------------------
    """
    print (texto)

mensaje("hola como estas es un nuevo mensaje")
mensaje("es otro texto")

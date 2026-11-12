## crear una funcion tipo closure que me permita ingresar nombre y apellido y me retorne un mensaje con ambos datos.

def creador (nombre:str):
    def apellido (ap:str):
        return f"tu nombre es : {nombre} y tu apellido es {ap}"
    return apellido

alumno1=creador("david") # def apellido (ap): return
alumno2=creador("noemi")
print (alumno1("goliat"))
print (alumno2("maikel"))


# usando closure crear una funcion multiplicador que resiva por parametro el factor que devuelva una funcion que permita multiplicar cualquier numero por el factor
 
def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar


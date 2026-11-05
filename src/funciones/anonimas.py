# haciendo uso de lambda crear la funcion que me muestre un mensaje personalizado

lambda nombre: f"Hola {nombre}, bienvenido al curso de Python."

nombre = input("Ingrese su nombre: ")

print(mensaje(nombre))

# crear una funcion calcular el area de un rectangula, siendo la formula la siguiente  area=base*altura

area_rectangulo:int=lambda b,h: b*h
print (area_rectangulo(h=8,b=4))
print (area_rectangulo(10,7))

# crear una funcion que verifique si un numerto es par o impar
Es par=lambda n: n% 2 ==0
if es_par(4):
    print("es par")
else:
    print ("es impar")

si_es_par=lambda n: "es par" if n%2==0 else "es impar"
print (si_es_par(100))









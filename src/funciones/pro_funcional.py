# ejercicio para map()
## recuerde map sirve para transformar todos los elementos 
## Ejercicio 1: Tienes una lista de numeros y quieres obtener una nueva lista con el cubo (elevado a 3)de cada numero.
numeros:list[int]=[1,2,3,4]
nueva_lista=list (map(lambda e:e**3,numeros))
print(nueva_lista)
def cubo(e):
    return e**3
map(cubo,numeros)

#ejercicio para filter()
## ejercicio 2: Tienes una lista de temperaturas (algunas bajo cero). filtra la lista para quedarse solo con las temperaturas positivas (mayores a 0).
temp:list[int|float]=[-2,10,0,-20,-1,-10,18,23.0]
nueva_tem=list(filter(lambda t:t>0,temp))
print(f"las temperaturas mayores a cero son: {nueva_temp}")

# ejercicio combinando map() y filter()
## tienes una lista de numeros. Primero filtrar para quedarte solo con los numeros pares. Luego usa, map para multiplicarlo por 10 los numeros pares.
# 1. forma
num:list[int]=[2,3,4,5,6,12,13,14]
numeros_pares:list[int]=list(filter(lambda n:n%2==0,num))
print(numeros_pares)
por_diez:list[int]=list(map(lambda n:n*10,numeros_pares))
print(por_diez)
#2. forma
num2:list[int]=[2,3,4,6,7,9,11,12,15,17,18]
pares_por_diez:list[int]=list(map(lambda n:n*10,filter(lambda n:n%2==0,num)))
print(pares_por_diez)
#3. forma usando compresion de listas
print([ n*10 for n in num if n%2==0])
#refactorizacion: es una tecnica para mejor o hacer mas optimo el codigo






#refactorizacion: es una tecnica para mejor o hacer mas optimo el codigo 
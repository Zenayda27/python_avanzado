# crear un programa que asigne un puntaje a cada letra del adecedarios y que funcion me permita saber la letra que tenga menor puntaje mayor  puntaje y la media 

def calcular_puntajes(puntajes):
    menor = min(puntajes, key=puntajes.get)
    mayor = max(puntajes, key=puntajes.get)
    media = sum(puntajes.values()) / len(puntajes)

    print("\n--- RESULTADOS ---")
    print("Letra con menor puntaje:", menor, puntajes[menor])
    print("Letra con mayor puntaje:", mayor, puntajes[mayor])
    print("La media de los puntajes es:", media)

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

puntajes = {}

for letra in abecedario:
    puntos = int(input("Ingrese el puntaje de la letra " + letra + ": "))
    puntajes[letra] = puntos

calcular_puntajes(puntajes)
## crear una funcion que revisa 5 numeros enteros y que retorne solo una lista de numeros pares, tener en cuenta las anotaciones 

def numeros_pares(a: int, b: int, c: int, d: int, e: int) -> list[int]:
    numeros: list[int] = [a, b, c, d, e]
    return [n for n in numeros if n % 2 == 0]

print(numeros_pares(4, 7, 10, 3, 8))
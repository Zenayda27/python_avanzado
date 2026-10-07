# crear un programa que me permita desarrollar las 4 operaciones basica (sema, resta, division , multiplicacion)


def suma(a:int, b:int):
    return a + b

def resta(a:int,b:int):
    return a - b

def multiplicacion(a:int,b:int):
    return a * b

def division(a:int,b:int):
    return a / b

print("Suma:", suma(78,36))
print("Resta:", resta(70,54))
print("Multiplicación:", multiplicacion(60,76))
print("division:", division(20,47))

def opraciones (n:list,o:str):
    if o=="+":
        return sum(n)
print(operaciones([4,8,20,78],"+"))

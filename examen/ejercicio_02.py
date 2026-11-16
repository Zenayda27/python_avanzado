### Parametros nominales y por defecto 

Crea una función llamada calcular_precio_final que calcule el precio de un producto aplicando un impuesto y un descuento opcional.
● Parámetros por defecto: impuesto = 0.18 (18%) y descuento = 0.0. 
● Utiliza argumentos nominales en su llamada para aplicar solo un descuento del 0.05 (5%) manteniendo el impuesto por defecto. 

```python
def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    precio_con_impuesto = precio + (precio * impuesto)
    precio_final = precio_con_impuesto - (precio_con_impuesto * descuento)
    return precio_final

resultado = calcular_precio_final(100, descuento=0.05)

print("El precio final es:", resultado)
```
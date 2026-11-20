# Modularidad 
la `modularidad` consiste en dividir un programa grande en archivos pequeños y reutilizables llamados `modulos` cada modulo es simplemente un archivo `.py` 
**Ventajas:**
- `reutilizacion` escribes el codigo una vez y lo usas en muchpos prgramas 
- `organizacion` cada archivo tiene una responsabilidad clara.
- `Mantenimiento` es mas facil encontar y corregir errores.
- `Trabajo en equipo` cada persona puede desarrollar su propio modulo 
## 1. crear un modulo
basta con crear un archivo con la extencion `.py` por ejemplo`matematicas.py` 
## 2. importar un modulo completo
la maner de como reutilizamos los modulos es haciendo de la palabra reservada`import` esto sr debe declarar en el archivo donde reutilizaremos ciertas funciones o variiables de un modulo 
para importar 

`import nombre_archivos`
`matematicas.py`
```python
def suma(a,b):
    return a+b
def resta (a,b)
    return a-b
```
`main.py`
```python
import matematicas
## para hacer uso de una de las funciones tengo que accerder al archivo luego un punto y el nombre de dto, funcion que deseamos utilizar
matematicas.resta(5,8)


```


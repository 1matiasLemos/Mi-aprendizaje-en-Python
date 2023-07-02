### Modulos ###

#los modulos son librerias o ficheros con codigo o funciones que podemos importar 
#los ficheros deben ser escritos con minuscula y sin numeros al principio del nombre del fichero

import module #importamos el fichero o modulo

module.printValue("hola matias") #tenemos acceso a la funcion que definimos en module

### SI QUEREMOS ACCEDER SOLO A ALGUNA FUNCION, VARIABLE O DATO ESPECIFICO ###

from module import sum_numbers, printValue #accedemos a la funcion sum_numbers del fichero module
printValue('hola Lemos')
sum_numbers(132,43,22)
from module import elemento_fichero #accedemos al diccionario definido dentro del fichero module
print(elemento_fichero.keys()) #['nombre', 'apellido', 'edad'] 
print(elemento_fichero.values())
print(elemento_fichero)

import math #libreria math, contiene todo tipo de operaciones matematicas

print(math.pow(2,8)) #potencias
print(math.sqrt(64)) #raiz cuadrada
print(math.cbrt(64)) #raiz cubica

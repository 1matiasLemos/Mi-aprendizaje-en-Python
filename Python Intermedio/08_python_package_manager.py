# pip install pip     #instala la version de pip 
# pip --version     #consulta la version de pip 

# pip install numpy
# pip show numpy (imprime la informacion del paquete)

import numpy

numpy_array = numpy.array([1,2,4,57,2,312])
print(numpy_array) #Salida: [  1   2   4  57   2 312]


# pip install pandas

import pandas
#pip unistall pandas (desinstala pandas)

panda_array = pandas.array([1,32,4,5,5,'23'],str) #toma una lista y un tipo para convertir los elementos
print(panda_array) 
'''Salida: <PandasArray> 
            ['1', '32', '4', '5', '5', '23'] strings
             Length: 6, dtype: str352''' #cuanta los elementos y el tipo de dato

panda_array = pandas.array([1,32,4,5,5,'23'],int)
print(panda_array) 
'''Salida: <PandasArray> 
            [1, 32, 4, 5, 5, 23]   Int
             Length: 6, dtype: int32''' #cuanta los elementos y el tipo de dato

panda_array = pandas.array([1,32,4,5,5,'23'],float)
print(panda_array) 
'''Salida: <PandasArray> 
           [1.0, 32.0, 4.0, 5.0, 5.0, 23.0] Float
           Length: 6, dtype: float64'''

panda_array = pandas.array([0,32,4,5,5,'23'],bool)
print(panda_array) 
'''Salida: <PandasArray> 
           [False, True, True, True, True, True] los numeros mayores que cero son True
           Length: 6, dtype: bool'''

import requests

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
# print(respuesta.content)


## Package arithmetics 

from my_package import arithmetics

print(arithmetics.sum_numbers(1,4))
## Higher orden functions_ funciones de orden superior ##

def sum_one(value):
    return value + 1
def sum_five(value):
    return value + 5
def multy_for_six(value):
    return value * 6

def sum_two_values_and_add_value(value1,value2,f_sum):
    return f_sum(value1 + value2)

'''al pasar como parametro una funcion, esta se usará dentro de la funcion sum_two_values_and_add_value 
la funcion hará lo que la funcion parametro tenga dentro de si'''
print(sum_two_values_and_add_value(43,5, sum_one)) #parametro funcion sum_one, retornará el value + 1
print(sum_two_values_and_add_value(43,5, sum_five)) #parametro funcion sum_five, retornará el value + 5
print(sum_two_values_and_add_value(43,5, multy_for_six)) #parametro funcion multy_for_six, retornará el value x 6

## Closures ##

def sum_ten(value1):
    def add(value):
        return value + value1
    return add


f_add = sum_ten(124)  #esta forma...
print(f_add(23)) #esta forma...
print(sum_ten(124)(134)) #es igual que esta otra forma

'''el primer parametro es de la funcion sum_ten; mientras que el segundo argumento es de la funcion add'''
#print(             sum_ten(124)                                        add(134))

##Built-in Higher Order Functions##

numbers = [3,4,1,4,2]
my_other_numbers = [10,30,40,633]

#Map

def multiply_two(number):
    return number *2

'''un map lo que hace es usar una funcion ya establecida en la que irá usando como argumento o parametro uno por uno
los elemento de una lista o iterable; devuelve una lista, pero que no es una lista como tal, en la que guarda
lo que retorna la funcion usada'''
print(list(map(multiply_two, numbers))) 
'''en este caso, se usa una funcion que retorna el valor parametro multiplicado por 2; el map guarda lo que se retorna 
y va creando un lista con el resultado de la multiplicacion; lo que se veria algo así -> (3*2),(4*2),(1*2)
El resultado es [6, 8, 2, 8, 4]'''
print(list(map(lambda number: number * 2, numbers)))

## Filter ##

def filter_greater_than_ten(numbers):
    if numbers > 10:
        return True
    elif numbers >20:
        return True
    return False
    
'''un filter crea un listado en donde una condicion se cumple, usa, en este caso, los bool dentro de una funcion con los
que determina cuales seran los elementos filtrados que guardará en la lista filter'''
print(list(filter(filter_greater_than_ten,my_other_numbers)))
'''en esta funcion determina cuando un numero es mayor que 10; el filter, guarda cuando se cumple la condicion, cuando hay algo
mayor que diez; devuelve los numeros que cumplieron con la condicion, y por ende los que son mayores que diez [30, 40, 633]'''

print(list(filter(lambda number: number<30,my_other_numbers)))
'''en este filter se usa una funcion que compara si un numero es menor que 30. El listado filtrado dirá que [10]
es el unico numero menor que 30 de todo el argumento lista o iterable'''

## Reduce ##

from functools import reduce

def sum_two_values(firts_value, second_value):
    return firts_value + second_value

'''lo que hace reduce es tomar los primeros dos elementos de la lista y operarlos entre si; luego, usa el resultado de esa
operacion para operarlo con el siguiente elemento, algo como esto -> ((((1+2)+3)+4)+5)''' 
print(reduce(sum_two_values,numbers),numbers)
#a diferencia de un map o un filter, un reduce no es en un listado sino un solo dato
print(reduce(lambda first_value,second_value: first_value + second_value, numbers),numbers) 
## Error types ##

## Syntax Error 
'''Los SyntaxError son errores de sintaxis en nuestro codigo, que no se escribió correctamente una parte del codigo'''
#print 'Hola comunidad' #SyntaxError
print('Hola comunidad') #correcto

## NameError
'''los NameError suceden cuando se intenta llamar a una variable no está definida'''
# print(variable) NameError
dat = 'dato'
print(dat)

## IndexError
'''Los IndexError suceden cuando se accede a un elemento en una lista que está fuera del rango o no existe tal elemento'''
my_list = ['python','suift','kotlin','java']
#print(my_list[5]) IndexError
print(my_list[3])
print(my_list[-1])

## ModuleNotFoundError
'''Este error sucede cuando importamos un modulo o libreria que no existe'''
#import maths
import math

## AttributeError
'''este error sucede cuando se intenta acceder a un atributo, de un modulo o libreria, que no existe como tal '''
#print(math.Pi) AttributeError
print(math.pi)

##  KeyError
'''los KeyError suceden cuando se accede a una llave de un diccionario que no existe'''
my_dict = {'nombre':'matias','apellido':'Lemos'}
#print(my_dict['edad']) KeyError
print(my_dict['apellido'])

## TypeError 
'''el TypeError sucede cuando se opera de manera inadecuada a un tipo de dato especifico, ej: se opera un list como dict'''
#print(my_list['java']) TypeError
print(my_list[2])

## ImportError 
'''el ImportError sucede cuando intentamos importar algun atributo de un modulo o libreria, y que éste no exista'''
#from math import Pi ImportError 
from math import pi 

## ValueError
'''el ValueError sucede cuando intentamos convertir a un tipo de dato diferente, pero que es imposible'''
my_int = int('19') 
#my_int = int('10 años') ValueError
print(type(my_int))

## ZeroDivisionError
'''el error es obvio, no se puede dividir entre 0 (cero)'''
#print(4/0) ZeroDivisionError
print(4/1)


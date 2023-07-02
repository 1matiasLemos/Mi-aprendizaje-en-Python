## Lambdas ##

#la funciones lambdas son pequeñas funciones anonimas, sin nombre, que hacen algo en concreto
#la funcion lambda se almacena dentro de una variable que se comporta como una funcion con argumentos, que retorna any
sum_lambda = lambda first_num, second_num: first_num + second_num

print(sum_lambda(1,3))

multy_lambda = lambda first_num, second_num: first_num * second_num - 13
print(multy_lambda(10,4))

#cuando hay una lambda en una funcion, podemos mandarle los parametros de la lambda junto con los parametros de la funcion
def fuction_with_lambda(value):

    return lambda first_num, second_num: first_num * second_num - value
#                    parametro_funcion  f_lambda
print(fuction_with_lambda   (42)          (4,6)) 


#asi como las lambdas se pueden guardar en variables, las funciones tambien
def sum_one(value):
    return value + 46

function_sum_one = sum_one #aqui creamos una variable
print(function_sum_one(10)) #se comportará como la funcion que se use para inicializarla
function_sum_one = fuction_with_lambda
print(function_sum_one(42) (3,5))
#diferencias 
print(type(function_sum_one)) #esta es una variable de tipo function
print(type(sum_one)) #mientras, que la funcion es solo una function
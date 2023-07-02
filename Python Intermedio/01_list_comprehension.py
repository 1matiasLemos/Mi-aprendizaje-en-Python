my_original_list = [1,2,3,4,5,6,7] 

my_range = range(-12,10) #le damos un rango de inicio y final, pero el valor final no se imprime, sino el anterior a ese
print(list(my_range), end = ' ') #cuando usamos un end en un print, le quitamos el \n por defecto que esta funcion tiene
print(my_range)

#el objeto i es donde se almacena lo retornado del for, para crear la lista
my_list = [i for i in my_original_list]
#my_list = [e for i in my_original_list] NameError, la variable del for es la misma que se usa para guardar
#my_list = [variable for variable in my_original_list] 
print(my_list)
    
my_string = '1,2,3,4,5,6,7,8' 
#cuando hacemos una lista en base a un str, cada caracter, sin excepción, será convertido en un elemento de la lista
my_list = [i for i in my_string] 
print(my_list) #['1', ',', '2', ',', '3', ',', '4', ',', '5', ',', '6', ',', '7', ',', '8'] nueva lista
my_list = list(my_string)
print(my_list)
 
# operaciones dentro del for #
my_list = [i * 10 for i in my_original_list]
print(my_list)
my_list = [i - i for i in my_original_list]
print(my_list)
my_list = [i * i for i in my_original_list]
print(my_list)

def sum_five(num):
    return num + 5
#se puede hacer lo que sea con el objeto
my_list = [sum_five(i) for i in my_original_list]
print(my_list) 
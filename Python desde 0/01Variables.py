#ejemplos de imprimir diferentes variables

my_string = "hola"
my_bool = True
my_int = 32

 #concatenacion de cadenas de variables

print(my_string, my_bool, my_int)

#convertir tipo de dato a string
'''
este metodo es solo para parsear entre dos variables existentes
'''

my_string_2 = str(my_int)
print(my_string_2)
print(type(my_string_2))

#convertir string a int

my_string_2 = int(my_int)
print(my_string_2)
print(type(my_string_2))

#funciones del sistema

print(len(my_string)) #funcion len que sirve para contar caracteres de un texto

'''crear variables en una linea

nombre, apellido, edad, año = "Matias", "Lemos", 18, 2023

print("My name is ", nombre)
print(type(nombre))
print("my surname is ", apellido)
print(type(apellido))
print("my age is ", edad)
print(type(edad))
print("the year is ", año)
print(type(año))

peso = input("cuanto pesas?")
print(peso)
'''
#las variables se pueden cambiar manualmente sin parsear, mientras se escriban desde consola

peso = "nombres"
print(peso)

#listas

nombre_completo = "Matias Lemos"
to_list = list(nombre_completo)
print(to_list) #esta funcion descompone una cadena de texto y las separa caracter por caracter
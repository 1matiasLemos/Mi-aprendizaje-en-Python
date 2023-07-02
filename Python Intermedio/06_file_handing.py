import os #importamos os para poder operar con ficheros

## .txt file

my_text_file = open("Python Intermedio/my_file2.txt", 'r+') #Leer y escribir
 
#my_text_file.write('mi nombre es matias\napellido es Lemos\ntengo 18 aÃ±os\nmi lenguaje actual es Python')

## --Read--
'''la funcion read lee todo el contenido del fichero .txt, pero solo una vez; si se lo llama una segunda vez no mostrará nada,
ya que se considerará como que estas queriendo seguir leyendo hacia abajo pero ya no hay nada que leer'''
#print(my_text_file.read())
#print(my_text_file.read(18)) #si se le agrega numeros es como ir leyendo caracteres de una cadena de texto hasta cierto caracter
# print(my_text_file.read()) no muestra nada, ya que ya se usó esta funcion una vez


## --Readline--
'''El readline lee linea a linea dependiendo de cuantas veces lo llamemos, y de cuantas lineas tenga el fichero'''
#print(my_text_file.readline(), end='') primera linea del fichero
#print(my_text_file.readline(), end='') segunda linea del fichero
#print(my_text_file.readline(), end='') tercera linea del fichero
#print(my_text_file.readline()) cuarta, y última, linea del fichero

## --Readlines--
'''la funcion readlines retorna una lista con todas las lineas del fichero'''
#print(my_text_file.readlines()) #retorna una lista con todas las lineas en ella
'''si le agregamos un entero mayor que 0, se comportará como un readline'''
#print(my_text_file.readlines(2)) #primera linea del fichero
#print(my_text_file.readlines(6)) #segunda linea del fichero
#print(my_text_file.readlines(10))# tercera linea del fichero
#print(my_text_file.readlines(6)) #cuarta, y última, linea del fichero
'''for line in my_text_file.readlines(): #se comportará como una lista en un bucle
    print(line) #imprimirá desde la primer linea hasta la ultima'''


## --Write--
'''al usar el write escribimos en el fichero que luego se guardará'''
#my_text_file.write('\npero tambien me gusta Java') 
my_text_file.close() #metodo close es el opuesto al open que usamos para abrir nuestro fichero

## ---Manera de crear ficheros---
'''para crear un nuevo fichero primero usamos la ruta en la que deseamos que esté, le asignamos un nombre y una terminacion,
en este caso es un .txt'''
#my_new_file = open("Python Intermedio/my_new_file.txt",'w+') 
'''esribimos lo que queremos que contenga el fichero, ya seann numeros o letras'''
#my_new_file.write('este es el fichero numero 2\nme llamo gonzalo\ntengo 21\nme gusta el lenguaje C++')

'''una vez creado este fichero, ahora podemos leerlo, tambien sobrescribir si queremos'''
my_new_file = open("Python Intermedio/my_new_file.txt",'r+')

my_new_file.close() #si cerramos el fichero no podremos operar con el 
#print(my_new_file.readlines()) #ValueError

## --Borar ficheros--

#os.remove("Python Intermedio/my_file2.txt") #esto nos permite borrar cualquier fichero desde aqui
#os.remove("Python Intermedio/my_new_file.txt") 
#os.remove("Python Intermedio/my_python_file.py")


## ---crear fichero .py

#my_python_file = open("Python Intermedio/my_python_file.py",'w+')
#my_python_file.write('hola = "hola mundo"\nprint(hola)')

## .json file

import json

'''creacion del archivo .json'''
my_json_file = open("Python Intermedio/my_file.json", 'w+')
json_text = {"Nombre":"Matias",
    "Apellido":"Lemos",
    "Edad":18,
    "Lenguaje": ['Python','Java','C++'],
    'webside': 'www.youtube.com'
    }

'''el dump sirve para escribir dentro del archivo json; el indent, indica la cantidad de espacios que tendrá dicha
indentacion donde el int es la cantidad de espacios (4 = tab) y se organizará como una estructura de codigo'''
json.dump(json_text,my_json_file, indent=4)
'''el primer parametro: es el objeto a escribir dentro del json; el segundo parametro: es el archivo json en el cual 
se va a enviar el objeto'''
my_json_file.close()

'''con el with open abrimos el archivo de manera temporal, y escribimos lo que queremos hacer 
usando una indentacion, como si de un bloque de codigo hablaramos. Al finalizar ese bloque de codigo,
se cerrará el archivo (.close()) por lo que si queremos usarlo de nuevo, debemos hacer un open'''
with open("Python Intermedio/my_file.json") as my_temporal_json_file:
    for index in my_temporal_json_file:
        print(index)

'''podemos usar el archivo json y guardar lo que contiene en una variable de tipo dict'''
json_dict = json.load(open("Python Intermedio/my_file.json"))
print(json_dict)
print(type(json_dict))

# .CSV 
import csv
'''los ficheros .csv son formatos de tipo hoja de calculo'''
my_csv_file = open("Python Intermedio/my_file.csv", 'w+')

'''creamos un writer o escritor, como parametro ponemos el nombre del archivo csv que creamos, esto indica
que este writer solo escribirá dentro del fichero que se le asignó como parametro'''
csv_writer = csv.writer(my_csv_file)

'''writerows crea filas y columnas usando cada caracter del argumento como una columna; la coma indica el fin 
de la fila y empieza una nueva usando los caracteres del siguiente argumento para crear una nueva fila con nuevas
columnas'''
csv_writer.writerows(['F234','F234'])

'''por otro lado, el writerow solo crea columnas en una fila; la coma indica el fin de la columna y pasa a tomar
el segundo argumento como la siguiente columna'''
csv_writer.writerow(['fila2_columna1','columna2'])
csv_writer.writerow(['fila3_columna1','columna3'])


# csv_writer.writerow(['Nombre','Apellido','Edad','Lenguaje','webside'])
# csv_writer.writerow(['Matias','Lemos',18,'Python','www.youtube.com'])

print(my_csv_file.readline())

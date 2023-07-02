#String maneras de crear

my_String = "Mi String"
my_other_String = 'Mi String' #ambas maneras son correctas 

#caracteres especiales

#lo que siga despues del caracter estara en la linea debajo
Other_string = "Texto con\n salto de linea"
print(Other_string)
tab_string = "\ttexto con tabulacion"
print(tab_string)
scape_string = "\\tTexto \\n escapado" #al colocar la doble barra se cancelan los caracteres especiales

#Formateo

name, apellido, edad = "Matias", "Lemos", 18

'''al usar format sirve para ubicar los tipos de datos en una impresion
primero ubicar el lugar y el tipo de dato con los porcentajes mas la letra del tipo de dato
el 
'''
#el orden de impresion de los datos será el que le demos
print("Hola mi nombre es {} {} y mi edad es {}".format(apellido,name,edad))#se colocan dos llaves para ubicar
print("Hola mi nombre es %s %s y mi edad es %d" %(apellido,name,edad))#se utilizan los porcentajes
print(f"Hola mi nombre es {name} {apellido} y mi edad es {edad}") #inferencia

#desempaquetado de caracteres

palabra = "Colectivo"
a,b,c,d,e,f,g,h,i = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i + "\n")

#Division

Palabra_cortada = palabra[0:5] #selecciona desde un carater hasta otro
print(Palabra_cortada)
Palabra_cortada = palabra[-6:-1]
print(Palabra_cortada)
Palabra_cortada = palabra[0:] #sin final, escribe todos los caracteres
print(Palabra_cortada)
Palabra_cortada = palabra[-4] #escribe el caracter especifico
print(Palabra_cortada)
Palabra_cortada = palabra[4]
print(Palabra_cortada)

#Reverse

palabra_reversa = palabra[::-1] #imprime la palabra en reversa 
print(palabra_reversa)

#Funciones

print(palabra.capitalize()) #imrpime el primer caracter en mayuscula

print(palabra.upper()) #escribe la palabra todo en mayuscula

print(palabra.upper().isupper()) # comprueba que estan en mayuscula

print(palabra.casefold()) #escribe la palabra en minusculas

print(palabra.count("t")) #cuenta cuantos caracteres especificos hay en la palabra

print(palabra.isnumeric()) #es un numero?

print("3432".isnumeric()) #true

print(palabra.isprintable()) #es imprimible?

print(palabra.encode())

print(palabra.find("v")) #encuentra donde comienza el caracter especifico 
print(palabra.find("C")) #(0) 0C1 O2 l3 e4

print(palabra.index("t"))

print(palabra.startswith("Col")) #tal cosa empieza con..?

print(sorted(palabra)) #devuelve una lista con letras de la cadena de texto, en orden alfabetico, como elementos

print(palabra.lower()) #devuelve la cadena pero en minusculas

print('texto con espacios'.split()) #devuelve una lista pero sin los espacios-> ['texto', 'con', 'espacios']
print(palabra.split(sep= 'o')) #el metodo split(sep=) retorna una lista donde cada elemento es lo que hay entre el argumento
#para ser mas preciso, en la palabra 'colectivo' si el sep = 'o' entonces lo que hay entre medio de 'o' en la palabra será un elemento
#ej: 'Colectivo'-> ['c','lectiv',''] se quitó la letra 'o' que seria el arg
print(palabra.split(sep= 'o',maxsplit=1)) #el maxsplit sirve para indicar cual es el numero de elementos que tendrá la lista
#ej: si la letra 'o' está dos veces, por defecto, te retorna 3 elementos ['C','lectiv','']
#pero si pones que el maxsplit = 1 (esto indica el elemento 1 en la lista, [0,1] lo cual, en realidad, son 2 elementos)
#entonces te retornará hasta el elemento 1 de la lista 
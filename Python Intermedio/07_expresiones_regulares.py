## Regular expresions ##

import re

my_string = 'esta es la lección numero 7: Lección Expresiones regulares'
my_other_string = 'esta no es la lección numero 6: Lección manejo de ficheros'

## match ##
'''el match busca desde el primer caracter de una cadena de texto un patron'''
#Cuando se utiliza re.I en una expresión regular, se ignora la distinción entre letras mayúsculas y minúsculas al buscar coincidencias. 
match = re.match('ESTA ES LA LECCIÓN',my_string,re.I) 
start, end = match.span() #el span es una tupla que contiene un valor de inicio y final span(0,18)
print(match)
print(my_string[start:end])

match = re.match('esta no es la lección',my_other_string)
if match is not None:
    start, end = match.span()
    print(match)
    print(my_other_string[start:end])

## search ##
'''el search, a diferencia del match, puede buscar un patron que esté ubicado en cualquier lugar dentro de la cadena de texto'''
objeto_search = re.search('lección',my_other_string)

print(objeto_search)


## findall

'''el findall retorna una lista de con el patron encontrado tantas veces'''
findall = re.findall('e',my_other_string,re.I)
print(findall)

## split 

print(re.split('e',my_string))

## sub
'''el sub sirve para cambiar el patron encontrado por un texto diferente'''

#patron = 'leccion',intercambio = 'LECCION', en la variable my_string
print(re.sub('lección|Expresiones|regulares','LECCION',my_string)) #al agregar el pipe o barra vertical, podemos ingresar mas patrones
print(re.sub('lección','LECCIÓN',my_string))

#en caso de tener dos o mas patrones que solo varian en un caracter
print(re.sub('[l|L]ección','LECCIÓN',my_string))

my_patern = 'hola, Hola, HolA,hOLA'

print(re.sub('[H|h]ol[a|A]','cambio',my_patern))

## Pattern

my_pattern = r'[lL]ección'
print(re.findall(my_pattern,my_string))

my_pattern = r'[lL]ección|Expresiones'
print(re.findall(my_pattern,my_string))

my_pattern = r'[0-9]' #numero entre el 0 al 9 
print(re.findall(my_pattern,my_string))
print(re.search(my_pattern,my_string))

my_pattern = r'\d' #patron para encontrar patrones numericos
print(re.findall(my_pattern,my_string))

my_pattern = r'\D' #patron para encontrar patrones no numericos
print(re.findall(my_pattern,my_string))

my_pattern = r'[l].' #el punto indica que debe haber algun caracter despues de la letra l, un punto equivale a un caracter 
print(re.findall(my_pattern,my_string)) #salida: ['la', 'le', 'la']
# my_pattern = r'[l]...'  (...) =  3 caracteres despues de la "l" 
# print(re.findall(my_pattern,my_string))

my_pattern = r'[l].*' #El "*" indica "todos los caracteres luego de" 
print(re.findall(my_pattern,my_string)) #salida: todos los caracteres despues de la "l"
#['la lección numero 7: Lección Expresiones regulares']

                            #del principio  empieza con +54    luego numeros, minimo que el patron llegue a 12 caracteres o mas
my_pattern = r'^[+54]\d{12,}' # '^          [+54]               \d{12,}'  
print(re.findall(my_pattern,'+543855433145'))

my_pattern = r'^[a-zA-Z0-9\._-]+@[a-zA-Z]+\.[a-zA-Z]+$'
print(re.match(my_pattern,'digitalizacion_98@gmail.com'))


# aprendiendo
# para practicar y aprender expresiones regulares https://regex101.com

'''de_a_hasta_z = '[a-z]' #puede ser en mayusculas o minusculas

##Caracteres especiales 
all_punto = '\.' #todos los puntos que encuentres
print(re.sub(all_punto,'punto','primer ., segundo .')) #primer punto, segundo punto

#el simbolo ^ sirve para indicar un patron que comienza si o si desde el inicio de la cadena
desde_el_inicio_de_la_cadena = '^a' #la primer a al incio de la cadena
print(re.sub(desde_el_inicio_de_la_cadena,'(primera a)', 'a traves de muchas aves')) #(primera a) traves de muchas aves

#conjunto de caracteres [] se puede mandar un conjunto de caracteres dentro de corchetes
vocales = '[aeiou]'
#buscará cuantas veces un elemento del conjunto aparece dentro de la frase 
print(re.findall(vocales,'cuando te parezca a ti')) #['u', 'a', 'o', 'e', 'a', 'e', 'a', 'a', 'i']
#reemplazará todos los elementos del conjunto por 'v' (vocal)
print(re.sub(vocales,'v','cuando te parezca a ti')) #cvvndv tv pvrvzcv v tv


print(re.match(de_a_hasta_z,'litas'))
'''

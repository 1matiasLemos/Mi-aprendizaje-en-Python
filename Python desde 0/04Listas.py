#listas

my_list = list() #ambas maneras son correctas, son listas
my_otherlist = []

my_list = [13,23,4,6,7557,23] #se guardan muchos datos en una lista
print(my_list)
print(type(my_list))
my_list2 = [18,1.75,"Matias",'Lemos']
print(my_list2)

print(my_list[1]) #se selecciona la posicion, cada elemento separado funciona como caracter
print(my_list[-3]) #funciona igual que un string, como una linea de tiempo 
print(my_list.count(23)) #cuenta elementos iguales al parametro especifico hay
#print(my_list[4]) esto generará un error porque no hay elemento 4, pero si -4

age, heigth, name, surname = my_list2 #los datos dentro de la lista se pueden pasar a muchas individuales

print(age)
print(heigth)
print(name)
print(surname)

print(my_list + my_list2) #los elementos de las listas se pueden concatenar en una sola

# Creación, inserción, actualización y eliminación

my_list2.append("Suncho") #se agrega un nuevo elemento a la lista
print(my_list2)

my_list2.insert(1,"azul") #1.75 pasa a ser el segundo
#se agrega un nuevo elemento, pero insertado en una posicion especifica
print(my_list2)

my_list2[1] = "amarillo" # "azul"
 #se actualiza o cambia un elemento de la lista, indicando su posicion 
print(my_list2[1])
print(my_list2)
 
my_list2.remove("amarillo") #se remueve un elemento especifico de la lista
print(my_list2)

#a diferencia del remove, el pop quita un elemento y lo retorna, lo guarda. por defecto guarda el ultimo elen
my_pop_element = my_list2.pop(3)  #Lemos
print("Mi elemento pop: " + my_pop_element) #Lemos
print(my_list2)

#se borra completamente el elemento
del my_list2[2] # "Matias"
print(my_list2)

my_new_list = my_list2
print(my_new_list)

#invierte los elementos de la lista
my_new_list.reverse()
print(my_new_list)

#ordena los elemenos tomando en cuenta el orden alfanumerico
#my_new_list.sort() TypeError: '<' not supported between instances of 'str' and 'float'
print(my_new_list)

#elimina todos los elementos de la lista
my_list2.clear() 
print(my_list2)

#Listas bidimensionales 

my_bidimensional_list = [[1],[2],[3],[4]]
my_bidimensional_list[0][0] = 'primer elemento de la fila 0'
my_bidimensional_list[1][0] = 'primer elemento de la fila 1'
my_bidimensional_list[2][0] = 'primer elemento de la fila 2'
my_bidimensional_list[3][0] = 'primer elemento de la fila 3'
print(f'{my_bidimensional_list[0][0]}\n{my_bidimensional_list[1][0]}')
print(f'{my_bidimensional_list[2][0]}\n{my_bidimensional_list[3][0]}')

#Pasar list a str

lista_a_convertir = ['hola', 'soy', 'una', 'lista']
str_resultante = ' '.join(str(elemento) for elemento in lista_a_convertir)
print(str_resultante)
#partes: 
# primero hacemos un bucle con lista_a_convertir y cada elemento es convertido a str
# despues usamos la funcion join que sirve para ir uniendo cada elemento
# ' ' -> sirve para agregar entre cada elemento (despues del elemento 'hola' agrega un ' ' y continua el bucle)

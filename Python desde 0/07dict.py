my_dict = dict()
my_other_dict = {}

print(type(my_dict))

#los nombres son las llaves, se agrupan por llaves y valores o datos
my_other_dict = {
    "Nombre":"Matias", #siempre colocar las comas
    "Apellido":"Lemos",
    "Edad":18,
    "Lenguaje": {"Python","Java","javaScript"}, #se pueden agregar varios valores a una sola llave
    1:1.75 #altura
    } 
#ejemp: llave 'Nombre', valor 'Matias'

print(len(my_other_dict)) #solo se cuentan las llaves

print(my_other_dict["Nombre"])
my_other_dict["Nombre"] = "MatiasJose" #actualizamos en valor o dato dentro de la llave "Nombre"
#my_other_dict["Nombre"] = {"MatiasL", "Lemos"} #si queremos agregar mas valores a una llave
print(my_other_dict)

del my_other_dict["Nombre"] #borrará la llave y los datos que hayamos seleccionado
print(my_other_dict)

#con esta funcion solo se busca por llaves, no por valores
print("Apellido" in my_other_dict) #true
print("Lemos" in  my_other_dict) #false

print(my_other_dict.keys()) #imprime solo las llaves
print(my_other_dict.values()) #imprime solo los valores


lista = ["hola",2,1244,"msafd"] 
my_new_dict = dict.fromkeys(lista) #crea un nuevo diccionario usando los elementos de la lista
print(my_new_dict)

my_new_dict = dict.fromkeys(("hola",2,1244,"msafd")) #manera manual para crear un diccionario
my_new_dict["hola"] = "hi"
print(my_new_dict.get("hola")) #restorna el valor de la clave

my_new_dict = dict.fromkeys(my_other_dict,"afasf") #toma las claves para crear el dict y le agrega el texto a todas
print(my_new_dict)

my_values = my_new_dict.values() #toma los valores del dict
print(type(my_values)) #dict_values esto es un diccionario de valores
 
print(list(my_new_dict)) #trasformado en list
print(tuple(my_new_dict)) #transformado en tupla
print(set(my_new_dict)) #tranformado en un set


#Crear diccionario con bucle 
          #key:  value      
dict_for = {key:    0     for key in range(1,10)} # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

dict_for = {'key'+str(i): 'value'+str(i) for i in range(1,5)}
print(dict_for)#{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# invertir dicts 
           #value como key  #key como value
dict_for = {value:          key             for key,value in dict_for.items()}
print(dict_for)#{'value1': 'key1', 'value2': 'key2', 'value3': 'key3', 'value4': 'key4'}

#dict dentro de otro dict

inside_other_dict = {
    'Perro':{'edad':5},
    'Gato':{'edad':6},
    'Tortuga':{'edad':10},
    'Caballo':{'caracteristicas':{'edad':7,'raza':'purasangre'}}
    }
print(inside_other_dict["Perro"]['edad']) # 5
print(inside_other_dict["Gato"]['edad']) # 6
print(inside_other_dict["Tortuga"]['edad']) # 10
print(inside_other_dict["Caballo"]['caracteristicas']['raza']) #purasangre 
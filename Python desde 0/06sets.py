my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicia como un diccionario

my_other_set = {"Matias",18,1.75,"Lemos"}
print(type(my_other_set))

print(len(my_other_set)) #3 elementos 

my_other_set.add("MatiasLs")
print(my_other_set) #los sets no son una estructura ordenada como una lista o tuplas
#print(my_othr_set[2]) #no permite acceder a un elemento

my_other_set.add("MatiasLs") #un sets no admite repetidos, no puede haber dos elementos iguales
print(my_other_set)

print("Matias" in my_other_set) #dara un bool si el elemento existe en el set
print('Lemos2' in my_other_set) #Lemos2 está en my_other_set False

my_other_set.remove("Lemos") #removerá el elemento Lemos
print(my_other_set)

my_other_set.clear() #limpia todo el set
print(my_other_set) #set()

my_set = {100,230,232,432}
my_set = list(my_set) #transforma el set en una list
print(my_set[0]) #el orden de la lista tampoco estará ordenada, ya que era un set
my_set = set(my_set)


my_other_set = {'Name','lemos',33} 
my_new_set = my_set.union(my_other_set)
#a diferencia de las listas solo se puede unir dos o mas sets con esta funcion
print(my_new_set)
print(my_new_set.union(my_other_set).union(my_set).union({"Hola", 'Javascript'})) #no admite repetidos

print(my_new_set.difference(my_set)) #imprime lo que diferencia un set de otro set
print(my_new_set.intersection(my_set)) #imprime solo la interseccion de un set en especifico
#esto quiere decir, solo lo que contiene tal set escrito como argumento en la funcion 
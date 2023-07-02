#la principal caracteristica de las tuplas es que no se pueden modificar los elementos primarios

my_tuple = tuple() #las tuplas se definen con parentesis en vez de corchetes
my_other_tuple = ()

my_tuple = (18,"Matias",1.75,'Lemos')
print(type(my_tuple))
my_other_tuple = (20,24,350,23)
print(my_tuple[2])
print(my_tuple[-1])
#print(my_tuple[4]) #error
#print(my_tuple[-5]) #error

print(my_tuple.count("Matias")) #1 
print(my_tuple.index("Lemos")) #3, indica el indice donde encontró el elemento
print(my_tuple + my_other_tuple)

gretter_tuple = my_tuple + my_other_tuple
print(gretter_tuple[1:3])

my_tuple = list(my_tuple) #transforma la tupla a lista
print(type(my_tuple))
my_tuple.insert(1,"Suncho")
my_tuple = tuple(my_tuple) #pasa la lista a una tupla de nuevo
print(my_tuple)
print(type(my_tuple))

del my_tuple

#del my_tuple{2} #no se puede borrar un elemento de una tupla
#print(my_tuple)  error
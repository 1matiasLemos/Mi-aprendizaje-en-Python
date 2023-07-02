class Person:
        
    def __init__(self, name, surname): #esto es un constructor que asigna elementos a la clase en donde está
        self.name1 = name #los elementos a los que se puede acceder solo son los que son creados dentro del constructor
        self.surname1 = surname #se guardan los valores de los parametros dentro de los elementos del constructor

    def walk(self):#si se quiere acceder a los elementos dentro de otra funcion en una misma clase, se usa el parametro self
        
        print(f'{self.name1} {self.surname1} está caminando')

#enviamos datos por parametros y creamos un nuevo objeto de tipo clase Person
my_person = Person('Matias', "Lemos") 
print(my_person.name1) #solo se accede a los elementos dentro del constructor, no de los parametros
my_person.walk()

print(type(my_person))

class Person2:
    def __init__(self, name, surname):
        #ejemplos de concatenaciones
        self.full_name = name, surname #devuelve como una tupla ('Matias', 'Lemos')
        self.full_name2 = name + surname # MatiasLemos #variable Publica
        self.full_name3 = f'{name} {surname}' # Matias Lemos 
        self.__name = name + " privado" #al colocar dos guion bajo creamos una variable Privada de esta funcion

    def get_name(self): #metodo getter para acceder a variables de tipo privado
        return self.__name
    
    def set_name(self, nombre): #metodo setter, ponemos un parametro para recibir el nuevo valor
        self.__name = nombre #asignamos el valor del parametro a la variable privada, la modificamos
        return self.__name #el return es opcional


my_other_person = Person2('Matias', 'Lemos') #cramos un nuevo objeto tipo class
my_other_person.full_name2 = "Matias Jose Lemos" #se puede cambiar el valor de un elemento
#print(my_other_person._name) no se puede acceder a esta variable privada
my_other_person.full_name = 134 #el tipado nos permite modificar los elementos publicos dentro de la funcion
print(my_other_person.full_name2)

#Metodos getter y setter
print(my_other_person.get_name()) #llamamos al metodo getter que nos retorna el valor de la variable de tipo privado
print(my_other_person.set_name('Jorge')) #enviamos un parametro
print(my_other_person.get_name()) #tiene un nuevo valor 'Jorge'
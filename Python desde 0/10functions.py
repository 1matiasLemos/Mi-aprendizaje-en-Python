
## Funciones ##

def my_function():
    print("Esto es una función")

my_function()


#las variables dentro no estan establecidas con un tipo de dato especifico, significa que pueden ser 
#cualquier tipo de dato que sean enviados a traves de los parametros
def suma_two_values(f_number,sec_number): #solo admite la misma cantidad de parametros, en este caso son dos
    print(f_number + sec_number)
    print(type(f_number + sec_number))

#definimos como cadenas de texto
number1 = "100" 
number2 = "300"

'''la funcion pasará los valores de los parametros a sus propias variables
esto quiere decir que puedes hacer cualquier operacion con cualquier tipo de dato, mientras ambos sean los mismos'''
suma_two_values(number1,number2) #se sumará las cadenas de texto, porque son str, '100300'
suma_two_values(int(number1), int(number2)) #los parametros ahora son int, por consecuancia se sumarán, 400
#suma_two_values(int(number1), number2) #esto da error, no puedes poner un int y str juntos


'''#podemos darle los argumentos sin guardarlos en una variable, desde la consola
suma_two_values(input(), input()) #si no especificamos el tipo de dato que es el argumento, por defecto, será de tipo str
suma_two_values(int(input()),int(input())) 
suma_two_values(float(input()),float(input()))'''

def suma_two_values_with_return(f_number,sec_number = 23): #esta funcion con retorno, solo devuelve el resultado

    my_sum = f_number + sec_number
    return my_sum

my_result = suma_two_values_with_return(10,22) #cuando nos retorna, debemos guardar ese valor retornado en una variable
print(my_result) #32 = 10 + 22
'''O tambien''' 
print(suma_two_values_with_return(10,22)) #podemos no guardar el valor retornado e imprimirlo directamente

def print_names (name, surname):
    print(f"{name} {surname}")
#aunque le pasamos los parametros en un orden diferente, se reordenarán dentro de la funcion
print_names(surname = "Lemos", name = "Matias") 

#funciones con por defecto
def print_names_with_defect (name, surname, alias = "sin alias"): #la variable alias tiene un por defecto
    print(f"{name} {surname} {alias}")
#con esta funcion se puede pasar dos argumentos y que la funcion cumpla de igual forma
print_names_with_defect("Matias","Lemos") #alias por defecto
print_names_with_defect("Matias","Lemos","Matwell") #sin el por defecto

def print_texts_upper(*texts): #al poner el asterisco se crea un parametros infinito, puedes pasar infinitos parametros
    print(texts) #imprime todos los parametros como si fuera una lista
    for text in texts: #toma los parametros y lo imprime uno a la vez
        print(text.upper())

print_texts_upper("hola", "python", "aula")
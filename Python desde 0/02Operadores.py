#tipos de operadores

print("Sumar ", 3 + 3)
print("Restar ", 34 - 3)
print("Multiplicar ", 2 * 2)
print("Dividir ", 34 / 2) #la division siempre da un float
print("Division sin el resto ", 15 // 2) #el resto no se muestra
print("Resto de la division ", 13 % 2) # solo se muestra el resto de la division 
print("Exponeciar o potencia ", 2 ** 3)

#operadores de texto 

print("Hola" + " " + "Python") #este operador imprime la cadena de texto como esten escritas
print("Hola", "Python") #de esta manera la cadena de texto tendrá un espacio en medio de cada cadena

#este operador solo puede imprimir cadenas o variables str
print("Hola" + str(3)) #si se quiere imprimir algun dato tipo numerico, de debe forzar como str

#se permite imprimir un dato int sin cambiar su tipo de dato, permanente
numero = 15
print("Numero" + str(numero)) #esto no cambia su tipo de dato original 
print(type(numero)) #int

#se puede repetir la cadena de texto con un operador de multiplicacion
print("Hola" * 3)


#Operadores Comparativos 

#Estos operadores imprimen un bool
print( 4 > 8)
print( 4 < 8)
print( 4 >= 8)
print( 4 <= 8)
print( 4 == 8)
print( 4 != 8)

#Con cadenas de texto 
print("")
print("Hola" > "Python") #este operador compara en orden alfabetico
print("Hola" < "Python")
print("Hola" >= "Python") #la letra H es menor que la letra P
print("Hola" <= "Python")
print(len("Hola") <= len("Python")) #cuenta de caracteres
print("Hola" == "Python")
print("Hola" != "Python")

#Operadores Logicos
print("")
print( 3 < 4 and "Hola" < "Python")
print( 3 > 4 or "Hola" < "Python")
print( not(3 < 4)) #el not niega la la condicion 

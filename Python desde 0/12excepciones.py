### Excepciones ###

# try except
try:
    print('2' + 5)
    print('No se ha producido un error\n')
except: #except sirve para mandar un bloque de codigo en caso de haber errores en el bloque de codigo try
    print("Los valores no se pueden sumar porque son distintos\n")

#try except else
try:
    print(2 + 5)
    print('No se ha producido un error')
except: 
    print("Los valores no se pueden sumar porque son distintos")
else: #el else se ejecuta solo si no se ha producido un error 
    print('La ejecucion continua correctamente\n')

# try except else y finally
try:
    print('2' + 5)
    print('No se ha producido un error')
except:
    print("Los valores no se pueden sumar porque son distintos")
else: #el else es opcional al igual de que el finally 
    print('La ejecucion continua correctamente')
finally: #el finally se ejecuta siempre, sin importar que haya errores o no
    print('Se finalizó la ejecucion')


# Exceptions por tipo
try:
    print('2' + 5)
    print('No se ha producido un error')
except TypeError: #al poner un tipo de error especifico, el except solo se ejecuta cuando ocurre ese tipo de error especifico
    print("Los valores no se pueden sumar porque son distintos")

### tipos de errores: principales ###
#TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado. ej (str * 32)
#ZeroDivisionError : Ocurre cuando se itenta dividir por cero. ej (12/0)
#OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
#IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
#KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
#FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
#ImportError : Ocurre cuando falla la importación de un módulo.
#Exception : Este tipo de excepcion sirve para capturar cualquier tipo de error e imprimirlo para saber de que tipo es

## Captura de informacion de exceptions ##
try:
    print('2' + 5)
    print('No se ha producido un error')
except TypeError as e: #al poner un tipo de error especifico, el except solo se ejecuta cuando ocurre ese tipo de error especifico
    print(e)
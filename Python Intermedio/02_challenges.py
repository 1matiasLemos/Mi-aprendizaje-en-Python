### El famoso 'Fizz Buzz': ###
def function_fizzbuzz():

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

### Es un anagrama ###

def anagram(str1, str2) -> bool:
    if str1.lower() ==  str2.lower():
        return False
    return sorted(str1.lower()) == sorted(str2.lower())

### Fibonacci ### 
def fibonacci():

    prev = 0
    next = 1
    fib = 0
    while fib <= 80:
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        
### Factorial recursivo ### 
def factorial(factorial): #retorna el factorial del argumento que se envie
    lista = [i for i in range(factorial,0,-1)] #se crea una lista inversa hasta 1s
    Numfact = lista[0] #toma el primer elemento de la lista
    for i in range(0,lista.__len__()-1): 
        Numfact = Numfact * lista[i+1] #multiplica por el siguiente elemento
    return f'{lista}\nEl factorial de {factorial} es = {Numfact}'
print(factorial(2))


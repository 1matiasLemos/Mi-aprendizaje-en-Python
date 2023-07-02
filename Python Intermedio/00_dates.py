 ### Dates ###

from datetime import datetime

now = datetime.now() #esta funcion accede a nuestro calendario y la hora

#toda funcion será sobre lo que este pasando ahora (now)
print(now.ctime()) #retorna la fecha actual, day, month, time y year
print(now.now()) #funciona de la misma manera que el ctime, pero solo la fecha y hora en numeros son retornados
print(now.time()) #retorna la hora actual
print(now.minute) #los minutos de la hora en el reloj
print(now.second) #segundos actuales
print(now.year) #año ''''
print(now.day) #dia ''''
print(now.month) #mes ''''
print(now.hour) #hora ''''

timestamp = now.timestamp()
print(timestamp)

                     #año/mes/dia/hora/minuto/segundo
year_2023 = datetime(2023, 4  ,3  ,9,   42,    10) #el datetime se usa para definir fechas, como minimo se deben crear el año,mes y dia
print(year_2023) #out= 2023-04-03 09:42:10

from datetime import time
                    
hour = minute = second = 13
current_time = time(hour,minute,second) #podemos definir una hora especifica, constante
#current_time = time(24,60,60) ValueError, no existe la hora 24, ni el minuto 60, ni el segundo 60 en el reloj
print(current_time)

from datetime import date

current_date = date(2023,3,24) #el date es solo para definir fechas

print(current_date)

## operaciones con fechas ##

try:
    current_date.year += 1
except Exception as e:
    print((e)) #TypeError: no se pueden sumar dos tipos de datos diferentes

#podemos hacer operaciones con enteros, pero solo cuando estamos inicializando un objeto
current_date = date(current_date.year + 1,current_date.month,current_date.day) 
print(current_date)

diff = year_2023.date() - current_date #podemos restar dias o fechas entre otras 
#diff = year_2023 + now TypeError
print(diff)

from datetime import timedelta

star_timedelta = timedelta(233,100,100,weeks = 10)
end_timedelta = timedelta(255,200,100,weeks = 15)

print(star_timedelta.days)
print(star_timedelta+end_timedelta)
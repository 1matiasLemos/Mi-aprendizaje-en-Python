my_condition = 0

while my_condition < 20:

    my_condition += 1
    print(my_condition)

    if my_condition == 17:
        break #palabra reservada para detener bucles

my_list = [12,13,434,24,24,213] #6 elementos, 

for elements in my_list: #si se usa una lista como range, imprime los elementos hasta el ultimo
    print(elements)

my_dict = {'nombre':'Matias','apellido':'Lemos','edad':'18','altura':1.75}

for elements in my_dict.values(): #imprime los valores
    print(elements) #los valores son guardados dentro del elements
    if elements == "apellido":
        continue #palabra reservada para que el ciclo se siga ejecutando



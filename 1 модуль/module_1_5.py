immutable_var = (1, "string", True, 3.14)
print("Кортеж: ", immutable_var)

try:
    immutable_var[0] = 5
except TypeError as e:
    print("Ошибка:", e)
    print("Нельзя менять значения элементов в кортеже")
    #Кортеж неизменяемый объект в python

mutable_list = [1, "string", True, 3.14]
print("Исходный список: ",mutable_list)
mutable_list[0] = 10
mutable_list.append('Строка')
print("Измененный список:", mutable_list)
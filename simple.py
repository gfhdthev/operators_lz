#сразу открываем все вайлы и записываем вводные данные в переменную
input_data = open('input.txt', 'r')
data = input_data.read()
output = open('output.txt', 'w')

data = data.split() #разделяем элементы
a = int(data[0]) #берем первый и единственный элемент

for i in range(2, a+1):
    if a%i == 0 and a != i: #ищем числа, на которое делится вводное число, и которое не равно ему
        output.write(str('N'))
        break #если мы находим хотя бы одно такое, то мы сразу останавливаем цикл
    elif a%i == 0 and i == a: #а если цикл доходит до найшего вводного числа, то, значит, оно простое
        output.write(str('Y'))

if a == 1: #ели вводно число равно едините, то выводим 'N', т.к. 1 - не простое число
    output.write(str('N'))

input_data.close()
output.close()
input_data = open('input.txt', 'r')
data = input_data.read()

data = data.split() #разделение элементов

#3 вводных значение
l = float(data[0])
s = float(data[1])
e = int(data[2])

sum = round(s-l, e) #находим сумму без начальной суммы(для удобства)

n = 1#число для 1/(n**2)
k = 0#кол-во итераций
t = 0#прибавляемое значение к l

if s-l <= 1.65:#проверяем, чтобы s и l отличались не более чем на 1.65

    while True:
        t += (1/(n**2))#обновляем значение, которое мы прибавляем

        if t <= sum:

            k += 1#прибавляем одну итерацию
            n += 1#прибавляем одно n для суммы

        elif t > sum:
            break#выходим из цикла

    output = open('output.txt', 'w')
    output.write(str(k))#выводим кол-во итераций

else: 
    output = open('output.txt', 'w')
    output.write(str('ERROR!'))

input_data.close()
output.close()
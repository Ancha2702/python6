#Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.


number = int(input('Введите число n: \n'))
list_new = [pow(-3,i) for i in range(0, number)]
print(list_new)
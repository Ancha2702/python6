# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import randrange

n = 11
list_to_mult = [randrange(1, 10) for i in range(n)]
mult_to_list = (list_to_mult[::-1])
print(list_to_mult, mult_to_list)
res = [[a*b for a, b in zip(list_to_mult, mult_to_list)]]
print(res)

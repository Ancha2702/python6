#Из списка выше оставьте только те пары, где сумма кортежа кратна 5

from random import randrange

n = 200
num_list = [randrange(1, 100) for i in range(n)]
   
list_k = list(filter(lambda x: (x[0]+x[1])%5 == 0,enumerate(num_list)))
print(list_k)
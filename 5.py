#5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
#[1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

from random import randrange

n = 200
num_list = [randrange(1, 100) for i in range(n)]
index_list = [i for i in range(0, len(num_list))]


def delete_el(index_list,num_list)->list:
    """_summary_

    Args:
        index_list (_list_): список индексов_
        num_list (_list_): _сгенерированный список чисел_

    Returns:
        list: _отфильтрованный список(без дубликатов - индекс/элемент)_
    """
        
    list_k = (list(zip(index_list,num_list)))

    
    for x in list_k:
        if x[0] == x[1]:
            list_k.remove(x)
    return(list_k)


print(delete_el(index_list,num_list))
#numbers = [random.randint(1, 100) for _ in range(200)]
#print(f'список без совпадений -> {list(filter(lambda x: x[0] != x[1], enumerate(numbers)))}')
#print(f'список удаленных -> {list(filter(lambda x: x[0] == x[1], enumerate(numbers)))}')
#if __name__ == '__main__':

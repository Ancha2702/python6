#1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.


word = input('Введите элемент, который нужно найти \n')
string = input('Введите строку, где нужно найти индекс второго вхождения: \n')
words = string.split()
find = -1 if words.count(word) <2 else list(filter(lambda x:x[1]==word, enumerate(words)))[1][0]
print (find)

# def find_index(word,string):
#     words = string.split()
#     count=0
#     for i, el in enumerate (words): 
#         if word in el:
#             count+=1
#             if count==2:
#                 print(i)
#                 break
#     else: print('Такого элемента нет')
  
  
# find_index(word,string)
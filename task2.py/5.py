#5. Реализуйте алгоритм перемешивания списка.

import random

def get_list (n, lft, rght):
    return [random.randint(lft, rght) for i in range (n)]

def shuffle_list (lst):
    return random.shuffle (lst)

n = 20
lft =  -10
rght = 10

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)
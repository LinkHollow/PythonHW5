import os
os.system('cls')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
count_a = 0
count_b = 0
count_c = 0
def num_summ(x, y, z, g, l):
    if x<=y:    
        if x > z:
            return(num_summ(x, y, z+1, g+1, l))
        elif (x == z) and (y > g):
            return(num_summ(x, y, z, g+1, l))
        elif l != z:
            return(num_summ(x, y, z,g+1, l+1))
        return(g)
    return(num_summ(y, x, z, g, l))
print(num_summ(a, b, count_a, count_b, count_c))
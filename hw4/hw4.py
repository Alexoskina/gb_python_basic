from sys import argv
from functools import reduce

# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

name, time, rate, benefit = argv

calculation = (int(time) * int(rate)) + int(benefit)
print(f"Your pay is equal {calculation}")

# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

lst = [1, 3, 6, 9, 12, 13, 17, 20]
new_lst = [el for el in lst if el > lst[lst.index(el) - 1]]
print(new_lst)

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

numbers = range(20, 241)
new_list = [el for el in numbers if el % 20 == 0 or el % 21 == 0]
print(new_list)

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))

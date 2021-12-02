# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def nums(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return "Не делите на ноль!"
    except ValueError:
        return "Это не число:)"


print(nums(int(input("Введите a = ")), int(input("Введите b = "))))


# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def info(name, surname, year, city, email, telephone):
    print(name, surname, year, city, email, telephone)


info(name="Иван", surname="Иванов", year="1999", city="Караганда", email="ivaninanich@test.ru", telephone="89999999999")


# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
# PS Нагуглила вариант решения через цикл, но поленилась с этим разбираться :D


def my_func(x, y):
    return x ** abs(y)
    # return x ** y


print(my_func(2, -3))

# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


result = 0
while True:
    lst = input("Введите число или символ Q, чтобы выйти: ").split(" ")
    for i in lst:
        try:
            num = int(i)
            result += num
        except:
            if i == 'q' or "Q":
                print(f"Ваш результат - {result}. Программа прервана")
                exit(0)
            else:
                print(f"Ваш результат - {result}.")
                exit(1)


# Реализовать функцию int_func(_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def my_func():
    words = str(input("Введите слово из маленьких латинских букв: "))
    print(words.title())


my_func()
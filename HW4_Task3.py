# 3) Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#numbers = list(map(int,input("Введите числа через пробел:\n").split()))
numbers = [1, 2, 3, 22, 9,  5, 1, 5, 3, 10, 16, 78]
def new_numbers(numbers):
    return [i for i in set(numbers)]

initial_numbers = numbers
print(f"Исходный список:{initial_numbers}")
print(f"Список из неповторяющихся элементов: {new_numbers(numbers)}")
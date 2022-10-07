# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
n = int(input("Введите натуральное число n: "))
i = 2 # первое простое число
enumeration = []
initial_number = n
while i <= n:
    if n % i == 0:
        enumeration.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {initial_number} приведены в списке: {enumeration}")
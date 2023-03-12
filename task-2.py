"""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) | """

num = int(input("Введите число: "))  
num_str = str(num)
sum = 0
for digit in num_str:
    sum += int(digit)
print("Сумма цифр = ", sum)



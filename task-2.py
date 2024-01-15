"""
Завдання 2
Є список цілих, заповнений випадковими числами.
На підставі даних цього масиву потрібно:
■ Створити список цілих, що містить лише парні числа з першого списку;
■ Створити список цілих, що містить лише непарні числа з першого списку;
■ Створити список цілих, що містить лише негативні числа з першого списку;
■ Створити список цілих, що містить лише позитивні числа з першого списку.
"""

from random import randint

my_list = [randint(-10, 10) for _ in range(10)]
print(f'my list: {my_list}')
new_list_1 = []
new_list_2 = []
new_list_3 = []
new_list_4 = []

for i in my_list:
    if i % 2 == 0:
        new_list_1.append(i)
    else:
        new_list_2.append(i)

print(f"new list with even: {new_list_1}")
print(f"new list with odd: {new_list_2}")

for i in my_list:
    if i < 0:
        new_list_3.append(i)
    else:
        new_list_4.append(i)

print(f"new list with negative numbers: {new_list_3}")
print(f"new list with positive numbers: {new_list_4}")

"""
Завдання 1
У списку цілих, заповненому випадковими числами обчислити:
■ Суму негативних чисел;
■ Суму парних чисел;
■ Суму непарних чисел;
■ Добуток елементів з кратними індексами 3;
■ Добуток елементів між мінімальним та максимальним елементом;
■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
"""

from random import randint

num_list = [randint(-10, 10) for _ in range(10)]
print(num_list)
sum_negative = 0
sum_even = 0
sun_odd = 0

for i in num_list:
    if i < 0:
        sum_negative += i
print(f'sum of negative numbers: {sum_negative}')

for i in num_list:
    if i % 2 == 0:
        sum_even += i
    else:
        sun_odd += i
print(f'sum of even numbers: {sum_even}\nsum of odd numbers: {sun_odd}')

myltiply_3 = 1
for i in range(0, len(num_list)):
    if i % 3 == 0:
        myltiply_3 *= num_list[i]
print(f'myltiply of numbers with index 3: {myltiply_3}')

max_num, min_num = max(num_list), min(num_list)
multiply_max_min = max_num * min_num
print(f"multiply of max and min numbers: {multiply_max_min}")

first_positive_index = 0
last_positive_index = 0

for i in range(len(num_list)):
    if num_list[i] > 0:
        first_positive_index = i
        break

for i in range(len(num_list) - 1, -1, -1):
    if num_list[i] > 0:
        last_positive_index = i
        break

sum_between_positives_and_negatives = sum(num_list[first_positive_index+1:last_positive_index])
print(f'sum between positive and negative numbers: {sum_between_positives_and_negatives}')

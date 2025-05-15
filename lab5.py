
# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
# сравнительного вычисления данной функции рекурсивно и итерационно. Определить (смоделировать) 
# границы применимости рекурсивного и итерационного подхода. 
# Вариант 9
# F(0)=5; F(1)=1; F(n)= (-1)^n*(2F(n-1)-F(n-2)) при n четном, F(n)=F(n-2)/(2n)!-F(n-1) при n нечетном

import math
import time
import matplotlib.pyplot as plt

while True:
    n = int(input("Введите натуральное число n>=0: "))
    if n >= 0:
        break
    else:
        print("Введено неверное число!")

def factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        return k * factorial(k-1)

def F_iter(n):  # Итерационное решение
    if n == 0:
        return 5
    elif n == 1:
        return 1

    F = [0] * (n + 1)
    F[0] = 5
    F[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 0:  # четное n
            F[i] = (-1)**i * (2 * F[i-1] - F[i-2])
        else:  # нечетное n
            F[i] = F[i-2] / factorial(2*i) - F[i-1]
    return F[n]

def F_rec(n):  # Рекурсивное решение
    if n == 0:
        return 5
    elif n == 1:
        return 1
    elif n % 2 == 0:  # четное n
        return (-1)**n * (2 * F_rec(n-1) - F_rec(n-2))
    else:  # нечетное n
        return F_rec(n-2) / factorial(2*n) - F_rec(n-1)

# Создание списков для построения таблицы значений
rec_times = []
rec_values = []
iter_times = []
iter_values = []
n_values = list(range(0, n + 1))

for n_val in n_values:  # заполнение списков
    # Итерационный метод
    t0 = time.time()
    iter_val = F_iter(n_val)
    t1 = time.time()
    iter_values.append(iter_val)
    iter_times.append(t1 - t0)

    # Рекурсивный метод (только для n <= 20 из-за ограничений рекурсии)
    if n_val <= 20:
        t0_rec = time.time()
        rec_val = F_rec(n_val)
        t1_rec = time.time()
        rec_values.append(rec_val)
        rec_times.append(t1_rec - t0_rec)
    else:
        rec_values.append(None)
        rec_times.append(None)

# Вывод таблицы
print('{:<4}|{:<25}|{:<25}|{:<25}|{:<25}'.format(
    'n', 'Время рекурсии', 'Время итерации', 'Значение рекурсии', 'Значение итерации'))
print('-' * 105)
for i, n_val in enumerate(n_values):
    if n_val <= 20:
        print('{:<4}|{:<25.6f}|{:<25.6f}|{:<25.6f}|{:<25.6f}'.format(
            n_val, rec_times[i], iter_times[i], rec_values[i], iter_values[i]))
    else:
        print('{:<4}|{:<25}|{:<25.6f}|{:<25}|{:<25.6f}'.format(
            n_val, "> limit", iter_times[i], "> limit", iter_values[i]))

# Построение графиков (только для n <= 20)
plot_n = min(n, 20)
plt.figure(figsize=(10, 6))
plt.plot(n_values[:plot_n+1], iter_times[:plot_n+1], label='Итерация')
plt.plot(n_values[:plot_n+1], rec_times[:plot_n+1], label='Рекурсия')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.title('Сравнение времени рекурсивного и итерационного подхода')
plt.legend()
plt.grid(True)
plt.show()

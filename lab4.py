# lab4.py
# Лабораторная работа №4

import numpy as np
import matplotlib.pyplot as plt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(abs(x)**0.5) + 1):
        if x % i == 0:
            return False
    return True

K_test = 3
N_test = 10
A_test = np.array([
    [9, 5, 1, 6, -3, -8, -7, 1, 1, 10],
    [1, 6, -5, -1, -4, -1, 10, 5, -10, -6],
    [-8, -2, -3, 7, 9, 1, 8, 0, 9, 5],
    [-7, 6, 0, -8, 4, 2, 1, -8, -5, -1],
    [-3, -9, -4, -1, -5, -3, -6, 9, 7, -6],
    [-7, 1, 7, 8, -3, 5, 7, -1, -7, -6],
    [-1, 6, -5, 2, 2, 2, 3, 10, -8, 4],
    [-4, -2, 1, -2, -2, -4, -7, -10, 15, 5],
    [2, -3, 0, -7, -1, 0, 9, -8, 9, 4],
    [-8, -10, 3, 0, -5, 10, -8, -10, -1, 8]
])

print('1 — тестовые данные\n2 — случайные\nq — выход')
while True:
    choice = input('Ваш выбор: ')
    if choice in ['1', '2', 'q']:
        break

if choice == 'q':
    exit()

if choice == '1':
    K, N, A = K_test, N_test, A_test
else:
    K = int(input('Введите K: '))
    while True:
        N = int(input('Введите N (>=6): '))
        if N >= 6:
            break
    A = np.random.randint(-10, 11, size=(N, N))

n = N // 2
A = np.array(A)
print('\nМатрица A:\n', A)

E = A[:n, :n]
B = A[:n, n:]
C = A[n:, n:]
D = A[n:, :n]

print('\nПодматрица E:\n', E)
print('\nПодматрица B:\n', B)
print('\nПодматрица C:\n', C)
print('\nПодматрица D:\n', D)

prime_count = sum(is_prime(B[i, j]) for j in range(1, B.shape[1], 2) for i in range(B.shape[0]))
even_rows_sum = sum(B[i].sum() for i in range(0, B.shape[0], 2))

print(f'\nПростых чисел в нечётных столбцах B: {prime_count}')
print(f'Сумма чисел в чётных строках B: {even_rows_sum}')

F = A.copy()

if prime_count > even_rows_sum:
    print("\n> Выполняем симметричную замену B и E")
    F[:n, :n] = np.fliplr(B.copy())
    F[:n, n:] = np.fliplr(E.copy())
else:
    print("\n> Выполняем несимметричную замену C и E")
    F[n:, n:], F[:n, :n] = E.copy(), C.copy()

print('\nМатрица F:\n', F)

det_A = round(np.linalg.det(A), 5)
trace_F = np.trace(F)

print(f'\nОпределитель матрицы A: {det_A}')
print(f'След матрицы F: {trace_F}')

if det_A > trace_F:
    print('\n> Вычисляем выражение A⁻¹·Aᵗ – K·F⁻¹')
    expr = np.dot(np.linalg.inv(A), A.T) - K * np.linalg.inv(F)
else:
    print('\n> Вычисляем выражение (Aᵗ + G – Fᵗ)·K')
    expr = (A.T + np.tril(A) - F.T) * K

print('\nРезультат выражения:\n', expr)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Тепловая карта F")
plt.imshow(F, cmap="viridis")
plt.colorbar()

plt.subplot(1, 3, 2)
plt.title("Максимальные значения по столбцам F")
plt.bar(range(F.shape[1]), np.max(F, axis=0))

plt.subplot(1, 3, 3)
plt.title("1-я строка F (доли по модулю)")
plt.pie(np.abs(F[0]), labels=range(len(F[0])), autopct='%1.1f%%')

plt.tight_layout()
plt.show()
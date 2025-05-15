# lab3.py
# Лабораторная работа №3
# Требуются функции: input_or_random, generate_matrix, build_matrix_A, print_matrix и т.д.
# Для запуска необходимо реализовать недостающие функции или импортировать их из модуля

choice = input_or_random()

if choice == 'q':
    exit()

if choice == '1':
    K = 3
    N = 10
    n = N // 2
    B = [
        [-8, -7, 1, 1, 10],
        [-1, 10, 5, -10, -6],
        [1, 8, 0, 9, 5],
        [2, 1, -8, -5, -1],
        [-3, -6, 9, 7, -6]
    ]
    C = [
        [5, 7, -1, -7, -6],
        [2, 3, 10, -8, 4],
        [-4, -7, -10, 15, 5],
        [0, 9, -8, 9, 4],
        [10, -8, -10, -1, 8]
    ]
    D = [
        [-7, 1, 7, 8, -3],
        [-1, 6, -5, 2, 2],
        [-4, -2, 1, -2, -2],
        [2, -3, 0, -7, -1],
        [-8, -10, 3, 0, -5]
    ]
    E = [
        [9, 5, 1, 6, -3],
        [1, 6, -5, -1, -4],
        [-8, -2, -3, 7, 9],
        [-7, 6, 0, -8, 4],
        [-3, -9, -4, -1, -5]
    ]
else:
    K = int(input("Введите K: "))
    while True:
        N = int(input("Введите N (>=6): "))
        if N >= 6 and N % 2 == 0:
            break
        print("Число N должно быть чётным и не меньше 6.")
    n = N // 2
    B = generate_matrix(n)
    C = generate_matrix(n)
    D = generate_matrix(n)
    E = generate_matrix(n)

# Формирование A
A = build_matrix_A(E, B, D, C)

print_matrix("Матрица E:", E)
print_matrix("Матрица B:", B)
print_matrix("Матрица C:", C)
print_matrix("Матрица D:", D)
print_matrix("Матрица A:", A)

# Условие
prime_count = count_primes_area2(B)
product_area3 = product_perimeter_area3(B)

print(f"Простых чисел в области 2 (B): {prime_count}")
print(f"Произведение по периметру области 3 (B): {product_area3}")

if prime_count > product_area3:
    B_mod = symmetric_swap_area1_3([row[:] for row in B])
    F = build_matrix_A(E, B_mod, D, C)
else:
    F = build_matrix_A(E, C, D, B)  # C и B меняются несимметрично

print_matrix("Матрица F:", F)

# Вычисление выражения
A_T = transpose(A)
F_T = transpose(F)
F_plus_A = matrix_add(F, A)
K_AT = matrix_scalar_mult(A_T, K)
K_F_T = matrix_scalar_mult(F_T, K)
KAT_mul_FplusA = matrix_mult(K_AT, F_plus_A)
result = matrix_sub(KAT_mul_FplusA, K_F_T)

print_matrix("Транспонированная матрица A:", A_T)
print_matrix("Транспонированная матрица F:", F_T)
print_matrix("Сумма F + A:", F_plus_A)
print_matrix("K * Aᵗ:", K_AT)
print_matrix("K * Fᵗ:", K_F_T)
print_matrix("Результат выражения ((K*Aᵗ)*(F+A)) - K*Fᵗ:", result)
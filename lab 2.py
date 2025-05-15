"""
Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
1. Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
2. Распознавание и обработку делать через регулярные выражения;
3. В вариантах, где есть параметр (например К), допускается его заменить на любое число;
4. Все остальные требования соответствуют варианту задания лабораторной работы №1.

Нечетные четырехричные числа, не превышающие 1024_10, у которых вторая справа цифра равна 3.
Выводит на экран цифры числа, исключая тройки.
Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""

import re

digit_to_word = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три'
}

min_num = None
max_num = None
num_filtered = []

try:
    with open("txt.txt", "r", encoding="utf-8") as file:
        content = file.read()
        # Ищем числа в четверичной системе, где вторая справа цифра 3 и последняя цифра 1 или 3
        numbers = re.findall(r'(?<!\d)[0-3]*3[13](?!\d)', content)
        
        if not numbers:
            print("\nВ файле txt.txt нет чисел, удовлетворяющих условиям")
        else:
            for num_str in numbers:
                # Проверяем длину числа (чтобы не превышало 1024 в десятичной)
                if len(num_str) > 5:  # 100000 в четверичной = 1024 в десятичной
                    continue
                
                num = int(num_str, 4)  # Преобразуем из четверичной в десятичную
                num_filtered.append(num)
                
                # Обновляем min и max
                if min_num is None or num < min_num:
                    min_num = num
                if max_num is None or num > max_num:
                    max_num = num

    if num_filtered:
        print("Список чисел, удовлетворяющих условию (в десятичной системе):")
        print(num_filtered)
        
        print("\nЦифры чисел в четверичной системе, исключая тройки:")
        for num in num_filtered:
            # Преобразуем обратно в четверичную систему
            quat_num = ''
            n = num
            while n > 0:
                quat_num = str(n % 4) + quat_num
                n = n // 4
            if num == 0:
                quat_num = '0'
            
            # Удаляем тройки и выводим
            filtered_digits = re.sub(r'3', '', quat_num)
            print(f"{num} (четверичное: {quat_num}) -> {filtered_digits}")
        
        # Вычисляем среднее между min и max
        avg_num = (min_num + max_num) // 2
        
        # Преобразуем среднее число в четверичную систему для вывода прописью
        avg_quat = ''
        n = avg_num
        while n > 0:
            avg_quat = str(n % 4) + avg_quat
            n = n // 4
        if avg_num == 0:
            avg_quat = '0'
        
        avg_words = ' '.join([digit_to_word[d] for d in avg_quat])
        
        print(f"\nМинимальное число: {min_num}")
        print(f"Максимальное число: {max_num}")
        print(f"Среднее число между min и max: {avg_num} (четверичное: {avg_quat})")
        print(f"Среднее число прописью: {avg_words}")
    else:
        print("Нет чисел, удовлетворяющих условиям.")

except FileNotFoundError:
    print("Файл txt.txt не найден в директории проекта")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
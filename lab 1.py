"""
Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
распознает, преобразует и выводит на экран лексемы по определенному правилу.
Лексемы разделены пробелами. Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Регулярные выражения использовать нельзя.

Нечетные четырехричные числа, не превышающие 1024_10, у которых вторая справа цифра равна 3.
Выводит на экран цифры числа, исключая тройки.
Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""

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
    with open("text.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                print("\nФайл text.txt в директории проекта закончился")
                break
            
            # Разбиваем строку на лексемы
            tokens = line.split()
            
            for token in tokens:
                # Проверяем, что токен состоит только из цифр 0-3 (четверичная система)
                if all(c in '0123' for c in token):
                    # Проверяем длину числа (чтобы не превышало 1024 в десятичной)
                    if len(token) > 5:  # 100000 в четверичной = 1024 в десятичной
                        continue
                    
                    # Проверяем, что число нечетное (последняя цифра 1 или 3)
                    if token[-1] not in ('1', '3'):
                        continue
                    
                    # Проверяем, что вторая справа цифра равна 3
                    if len(token) >= 2 and token[-2] == '3':
                        num = int(token, 4)  # Преобразуем из четверичной в десятичную
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
            
            # Удаляем тройки и выводим
            filtered_digits = ''.join([d for d in quat_num if d != '3'])
            print(f"{num} (четверичное: {quat_num}) -> {filtered_digits}")
        
        # Вычисляем среднее между min и max
        avg_num = (min_num + max_num) // 2
        
        # Преобразуем среднее число в четверичную систему для вывода прописью
        avg_quat = ''
        n = avg_num
        while n > 0:
            avg_quat = str(n % 4) + avg_quat
            n = n // 4
        
        avg_words = ' '.join([digit_to_word[d] for d in avg_quat])
        
        print(f"\nМинимальное число: {min_num} (четверичное: {bin(min_num)[2:]})")
        print(f"Максимальное число: {max_num} (четверичное: {bin(max_num)[2:]})")
        print(f"Среднее число между min и max: {avg_num} (четверичное: {avg_quat})")
        print(f"Среднее число прописью: {avg_words}")
    else:
        print("Нет чисел, удовлетворяющих условиям.")

except FileNotFoundError:
    print("Файл text.txt не найден в директории проекта")
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
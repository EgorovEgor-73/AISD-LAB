# Вариант 9 (усложненный)
# Ограничения: 
# 1. В совещании должно быть не менее 1 человека из отдела продаж
# 2. Не более 2 человек из отдела рекламы
# Целевая функция: выбрать вариант с максимальным суммарным рейтингом сотрудников

# Списки сотрудников с их рейтингами
sales_dept = {
    "Иванов": 8.5,
    "Петров": 7.2,
    "Сидоров": 9.1,
    "Кузнецов": 6.8,
    "Смирнов": 7.9
}

marketing_dept = {
    "Васильев": 8.1,
    "Николаев": 7.5,
    "Федоров": 8.9,
    "Михайлов": 6.5,
    "Алексеев": 7.7
}

# Ввод данных
k1 = len(sales_dept)
k2 = len(marketing_dept)
print(f"В отделе продаж: {k1} человек")
print(f"В отделе рекламы: {k2} человек")

n = int(input("\nВведите количество человек для совещания (N): "))
while n < 2 or n > 5:  # Ограничение по условиям задачи
    n = int(input(f"Введите число от 2 до 5: "))

# Формирование всех возможных комбинаций с ограничениями
from itertools import combinations

all_employees = list(sales_dept.keys()) + list(marketing_dept.keys())
valid_meetings = []

for meeting in combinations(all_employees, n):
    sales_count = sum(1 for emp in meeting if emp in sales_dept)
    marketing_count = sum(1 for emp in meeting if emp in marketing_dept)
    
    # Проверка ограничений
    if sales_count >= 1 and marketing_count <= 2:
        # Расчет суммарного рейтинга
        total_rating = sum(sales_dept.get(emp, 0) + marketing_dept.get(emp, 0) for emp in meeting)
        valid_meetings.append((meeting, total_rating))

# Сортировка по рейтингу
valid_meetings.sort(key=lambda x: x[1], reverse=True)

# Вывод результатов
print(f"\nВсего допустимых вариантов совещания: {len(valid_meetings)}")
print("Топ-10 вариантов с наивысшим рейтингом:")
for i, (meeting, rating) in enumerate(valid_meetings[:10], 1):
    print(f"{i}. {', '.join(meeting)} (Рейтинг: {rating:.1f})")

# Лучший вариант
if valid_meetings:
    best_meeting, best_rating = valid_meetings[0]
    print(f"\nОптимальный состав совещания: {', '.join(best_meeting)}")
    print(f"Суммарный рейтинг: {best_rating:.1f}")
else:
    print("\nНет вариантов, удовлетворяющих ограничениям")
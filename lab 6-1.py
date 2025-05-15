# Вариант 9. В торговой компании работает К человек (к1 - в отделе продаж, к2 - в отделе рекламы). 
# На совещание по продвижению нового товара требуется N человек из этих двух отделов. 
# Вывести все возможные варианты состава совещания.

# Списки сотрудников
sales_dept = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов"]
marketing_dept = ["Васильев", "Николаев", "Федоров", "Михайлов", "Алексеев"]

# Ввод данных
k1 = len(sales_dept)
k2 = len(marketing_dept)
print(f"В отделе продаж: {k1} человек")
print(f"В отделе рекламы: {k2} человек")

n = int(input("Введите количество человек для совещания (N): "))
while n < 1 or n > (k1 + k2):
    n = int(input(f"Введите число от 1 до {k1 + k2}: "))

# Формирование всех возможных комбинаций
from itertools import combinations

all_employees = sales_dept + marketing_dept
meetings = list(combinations(all_employees, n))

# Вывод результатов
print(f"\nВсего возможных вариантов совещания: {len(meetings)}")
for i, meeting in enumerate(meetings, 1):
    print(f"{i}. {', '.join(meeting)}")
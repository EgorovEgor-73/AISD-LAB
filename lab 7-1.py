import tkinter as tk
from tkinter import ttk, scrolledtext
from itertools import combinations

class MeetingPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Планировщик совещаний")
        self.root.geometry("800x600")
        
        # Данные сотрудников
        self.sales_dept = {
            "Иванов": 8.5,
            "Петров": 7.2,
            "Сидоров": 9.1,
            "Кузнецов": 6.8,
            "Смирнов": 7.9
        }
        
        self.marketing_dept = {
            "Васильев": 8.1,
            "Николаев": 7.5,
            "Федоров": 8.9,
            "Михайлов": 6.5,
            "Алексеев": 7.7
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Фрейм для ввода данных
        input_frame = ttk.LabelFrame(self.root, text="Параметры совещания", padding=10)
        input_frame.pack(pady=10, padx=10, fill="x")
        
        # Выбор количества участников
        ttk.Label(input_frame, text="Количество участников (N):").grid(row=0, column=0, sticky="w")
        self.n_var = tk.IntVar(value=3)
        self.n_spinbox = ttk.Spinbox(input_frame, from_=2, to=5, textvariable=self.n_var)
        self.n_spinbox.grid(row=0, column=1, sticky="ew", padx=5)
        
        # Ограничения
        ttk.Label(input_frame, text="Ограничения:").grid(row=1, column=0, sticky="w")
        self.min_sales_var = tk.IntVar(value=1)
        self.max_marketing_var = tk.IntVar(value=2)
        
        ttk.Checkbutton(input_frame, text="Минимум из отдела продаж", variable=self.min_sales_var).grid(row=2, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(input_frame, text="Максимум из отдела рекламы", variable=self.max_marketing_var).grid(row=3, column=0, columnspan=2, sticky="w")
        
        # Кнопка расчета
        ttk.Button(input_frame, text="Сформировать варианты", command=self.generate_meetings).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Фрейм для вывода результатов
        output_frame = ttk.LabelFrame(self.root, text="Результаты", padding=10)
        output_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Поле вывода с прокруткой
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=80, height=20)
        self.output_text.pack(fill="both", expand=True)
        
        # Статус бар
        self.status_var = tk.StringVar(value="Готов к работе")
        ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN).pack(side=tk.BOTTOM, fill=tk.X)
    
    def generate_meetings(self):
        n = self.n_var.get()
        min_sales = self.min_sales_var.get()
        max_marketing = self.max_marketing_var.get()
        
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("Идет расчет...")
        self.root.update()
        
        try:
            all_employees = list(self.sales_dept.keys()) + list(self.marketing_dept.keys())
            valid_meetings = []
            
            for meeting in combinations(all_employees, n):
                sales_count = sum(1 for emp in meeting if emp in self.sales_dept)
                marketing_count = sum(1 for emp in meeting if emp in self.marketing_dept)
                
                # Проверка ограничений
                if (not min_sales or sales_count >= 1) and (not max_marketing or marketing_count <= 2):
                    # Расчет суммарного рейтинга
                    total_rating = sum(self.sales_dept.get(emp, 0) + self.marketing_dept.get(emp, 0) for emp in meeting)
                    valid_meetings.append((meeting, total_rating))
            
            # Сортировка по рейтингу
            valid_meetings.sort(key=lambda x: x[1], reverse=True)
            
            # Вывод результатов
            self.output_text.insert(tk.END, f"Всего допустимых вариантов: {len(valid_meetings)}\n\n")
            self.output_text.insert(tk.END, "Топ-20 вариантов с наивысшим рейтингом:\n")
            
            for i, (meeting, rating) in enumerate(valid_meetings[:20], 1):
                sales = [emp for emp in meeting if emp in self.sales_dept]
                marketing = [emp for emp in meeting if emp in self.marketing_dept]
                self.output_text.insert(tk.END, f"{i}. {' + '.join(meeting)}\n")
                self.output_text.insert(tk.END, f"   Продажи: {', '.join(sales)} | Реклама: {', '.join(marketing)}\n")
                self.output_text.insert(tk.END, f"   Общий рейтинг: {rating:.1f}\n\n")
            
            if valid_meetings:
                best_meeting, best_rating = valid_meetings[0]
                self.output_text.insert(tk.END, f"\nОптимальный состав:\n{' + '.join(best_meeting)}\n")
                self.output_text.insert(tk.END, f"Максимальный рейтинг: {best_rating:.1f}\n")
            
            self.status_var.set(f"Готово. Найдено {len(valid_meetings)} вариантов")
        
        except Exception as e:
            self.output_text.insert(tk.END, f"Ошибка: {str(e)}")
            self.status_var.set("Ошибка при расчете")

def main():
    root = tk.Tk()
    app = MeetingPlannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
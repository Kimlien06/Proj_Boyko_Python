import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime, timedelta
from tkcalendar import DateEntry


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Умный To-Do List")
        self.root.geometry("1000x950")
        self.root.resizable(False, False)

        # Уникальный дизайн
        self.root.configure(bg='white')
        self.style = ttk.Style()
        self.style.theme_use('default')

        # Настраиваем стили
        self.style.configure('TFrame', background='white')
        self.style.configure('TLabel', font=('Arial', 12, 'bold'), background='white')
        self.style.configure('TButton', font=('Arial', 10, 'bold'), padding=5, background='light grey', borderwidth=1)
        self.style.configure('TEntry', font=('Arial', 12), padding=5)
        self.style.configure('Treeview.Heading', font=('Arial', 11, 'bold'))
        self.style.map('TButton', background=[('active', '#3a6a7c')])

        # Заголовок
        self.header_frame = ttk.Frame(root)
        self.header_frame.pack(pady=10)

        self.title_label = ttk.Label(self.header_frame, text="Мой To-Do List", font=('Arial', 16, 'bold'))
        self.title_label.pack(pady=10)

        # Дата
        self.date_label = ttk.Label(self.header_frame, text=self.get_current_date(), style='TLabel')
        self.date_label.pack()

        # Поле ввода задачи
        self.input_frame = ttk.Frame(root)
        self.input_frame.pack()

        self.task_label = ttk.Label(self.input_frame, text="Задача:", padding=5)
        self.task_label.grid(row=0, column=0, sticky='w')

        self.task_enter = ttk.Entry(self.input_frame, width=40, style='TEntry')
        self.task_enter.grid(row=0, column=1)

        # Поле для дополнительной информации
        self.details_frame = ttk.Frame(root)
        self.details_frame.pack()

        self.details_label = ttk.Label(self.details_frame, text="Доп. информация:", padding=5)
        self.details_label.grid(row=0, column=0, sticky='w')

        self.details_entry = ttk.Entry(self.details_frame, width=40, style='TEntry')
        self.details_entry.grid(row=0, column=2, pady=15, sticky='w')

        # Уровень сложности
        self.difficulty_frame = ttk.Frame(root)
        self.difficulty_frame.pack(pady=5)

        self.difficulty_label = ttk.Label(self.difficulty_frame, text="Сложность:", style='TLabel')
        self.difficulty_label.grid(row=0, column=0, padx=5, sticky='w')

        self.difficulty_var = tk.StringVar()
        self.difficulty_combobox = ttk.Combobox(
            self.difficulty_frame,
            textvariable=self.difficulty_var,
            values=["Легкая", "Средняя", "Сложная"],
            state='readonly',
            width=15
        )

        self.difficulty_combobox.current(0)
        self.difficulty_combobox.grid(row=0, column=1, padx=5, sticky='w')

        # Дедлайн
        self.deadline_frame = ttk.Frame(root)
        self.deadline_frame.pack(pady=5)

        self.deadline_label = ttk.Label(self.deadline_frame, text="Дедлайн:", style='TLabel')
        self.deadline_label.grid(row=0, column=0, padx=5, sticky='w')

        self.deadline_var = tk.StringVar()
        self.deadline_entry = DateEntry(
            self.deadline_frame,
            textvariable=self.deadline_var,
            date_pattern='dd.mm.yyyy',
            width=15,
            background='darkblue',
            foreground='white',
            borderwidth=2
        )

        tomorrow = datetime.now() + timedelta(days=1)
        self.deadline_entry.set_date(tomorrow)
        self.deadline_entry.grid(row=0, column=1, padx=5, sticky='w')

        # Кнопка добавления
        self.add_button_frame = ttk.Frame(root)
        self.add_button_frame.pack(pady=10)
        self.add_button = ttk.Button(self.add_button_frame, text="Добавить", command=self.add_task)
        self.add_button.pack()

        # Фрейм для таблицы и скроллбара
        self.table_frame = ttk.Frame(root)
        self.table_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Treeview (таблица задач)
        self.task_tree = ttk.Treeview(
            self.table_frame,
            columns=('Status', 'Task', 'Details', 'Difficulty', 'Deadline'),
            show='headings',
            selectmode='browse',
            height=15
        )

        # Настройка колонок и заголовков
        self.task_tree.column('Status', width=25, anchor='center')
        self.task_tree.column('Task', width=50, anchor='w')
        self.task_tree.column('Details', width=50, anchor='w')
        self.task_tree.column('Difficulty', width=25, anchor='center')
        self.task_tree.column('Deadline', width=25, anchor='center')
        self.task_tree.heading('Status', text='✓')
        self.task_tree.heading('Task', text='Задача')
        self.task_tree.heading('Details', text='Доп. информация')
        self.task_tree.heading('Difficulty', text='Сложность')
        self.task_tree.heading('Deadline', text='Дедлайн')

        # Скроллбар
        scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.task_tree.yview)
        self.task_tree.configure(yscrollcommand=scrollbar.set)
        self.task_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Фрейм для кнопок управления (под таблицей)
        self.buttons_frame = ttk.Frame()
        self.buttons_frame.pack(fill=tk.X, pady=(5, 10))

        # Кнопки управления
        self.complete_button = ttk.Button(
            self.buttons_frame,
            text="Выполнить",
            command=self.complete_task,
            width=20
        )
        self.delete_button = ttk.Button(
            self.buttons_frame,
            text="Удалить",
            command=self.delete_task,
            width=20
        )
        self.details_button = ttk.Button(
            self.buttons_frame,
            text="Детали",
            command=self.view_details,
            width=20
        )

        # Размещение кнопок с отступами
        self.complete_button.pack(side=tk.LEFT, padx=15)
        self.delete_button.pack(side=tk.LEFT, padx=15)
        self.details_button.pack(side=tk.LEFT, padx=15)

        # Статистика
        self.stats_frame = ttk.Frame()
        self.stats_frame.pack(fill=tk.X, pady=(0, 10))

        self.stats_label = ttk.Label(
            self.stats_frame,
            text="Всего задач: 0 | Выполнено: 0 | Просрочено: 0"
        )
        self.stats_label.pack(side=tk.LEFT, padx=15)

        # Загрузка задач
        self.tasks = []
        self.load_tasks()
        self.update_stats()

        # Оригинальные фичи
        self.task_enter.bind("<Return>", lambda event: self.add_task())
        self.task_tree.bind("<Double-1>", lambda event: self.complete_task())

    def get_current_date(self):
        today = datetime.now()
        return today.strftime("%d.%m.%Y")

    def add_task(self):
        task_text = self.task_enter.get().strip()
        details_text = self.details_entry.get().strip()
        difficulty = self.difficulty_var.get()
        deadline = self.deadline_var.get()

        if task_text:
            self.tasks.append({
                "text": task_text,
                "details": details_text,
                "difficulty": difficulty,
                "deadline": deadline,
                "completed": False,
                "created": self.get_current_date()
            })
            self.update_tasks_list()
            self.task_enter.delete(0, tk.END)
            self.details_entry.delete(0, tk.END)
            self.difficulty_combobox.current(0)
            tomorrow = datetime.now() + timedelta(days=1)
            self.deadline_entry.set_date(tomorrow)
            self.save_tasks()
            self.update_stats()
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, введите текст задачи.")

    def complete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            index = int(selected_item[0][1:]) - 1
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_tasks_list()
            self.save_tasks()
            self.update_stats()

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            index = int(selected_item[0][1:]) - 1
            del self.tasks[index]
            self.update_tasks_list()
            self.save_tasks()
            self.update_stats()
            # После удаления проверяем, остались ли задачи
            if not self.tasks:
                self.buttons_frame.pack_forget()

    def view_details(self):
        selected_item = self.task_tree.selection()
        if selected_item:
            index = int(selected_item[0][1:]) - 1
            task = self.tasks[index]
            details = f"Задача: {task['text']}\n\n"
            details += f"Доп. информация: {task['details']}\n\n"
            details += f"Сложность: {task['difficulty']}\n\n"
            details += f"Дедлайн: {task['deadline']}\n\n"
            details += f"Создана: {task['created']}\n\n"
            details += f"Статус: {'Выполнена' if task['completed'] else 'Не выполнена'}"

            # Проверка просрочки
            if not task['completed']:
                deadline_date = datetime.strptime(task['deadline'], "%d.%m.%Y")
                if deadline_date < datetime.now():
                    details += "\n\n⚠️ ЗАДАЧА ПРОСРОЧЕНА!"

            messagebox.showinfo("Детали задачи", details)

    def update_tasks_list(self):
        self.task_tree.delete(*self.task_tree.get_children())
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else ""
            task_text = task["text"]
            details_text = task["details"]
            difficulty = task["difficulty"]
            deadline = task["deadline"]
            if task["completed"]:
                task_text = f"✓ {task_text}"
            self.task_tree.insert('', 'end', iid=f"t{i}",
                                  values=(status, task_text, details_text, difficulty, deadline))
            self.task_tree.tag_configure('overdue', background='#ffcccc')

        # Показать или скрыть кнопки в зависимости от наличия задач
        if self.tasks:
            self.buttons_frame.pack(pady=5, fill=tk.X)
        else:
            self.buttons_frame.pack_forget()

    def update_stats(self):
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])

        overdue = 0
        for task in self.tasks:
            if not task["completed"] and "deadline" in task:
                deadline_date = datetime.strptime(task["deadline"], "%d.%m.%Y")
                if deadline_date < datetime.now():
                    overdue += 1

        self.stats_label.config(text=f"Всего задач: {total} | Выполнено: {completed} | Просрочено: {overdue}")

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)
                self.update_tasks_list()
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []


root = tk.Tk()
app = TodoApp(root)
root.mainloop()

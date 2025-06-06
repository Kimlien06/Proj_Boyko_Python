import tkinter as tk
from tkinter import ttk


def register():
    print("Регистрация завершена!")
    print(f"Имя: {name_entry.get()}")
    print(f"Пароль: {password_entry.get()}")
    print(f"Специализация: {specialization.get()}")
    print(f"Пол: {'Мужской' if gender.get() == 1 else 'Женский'}")
    print("Навыки:", [skill for skill, var in skills.items() if var.get()])
    print(f"Дополнительно: {info_text.get('1.0', tk.END)}")


def clear_form():
    name_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)
    specialization.set("Web-мастер")
    gender.set(0)
    for var in skills.values():
        var.set(False)
    info_text.delete('1.0', tk.END)


root = tk.Tk()
root.title("Анкета Web-разработчика")


main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0)


title_label = ttk.Label(main_frame, text="Анкета Web-разработчика", font=('Arial', 14, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady=10)


ttk.Label(main_frame, text="Регистрационное имя").grid(row=1, column=0, sticky=tk.W, pady=2)
name_entry = ttk.Entry(main_frame, width=30)
name_entry.grid(row=1, column=1, sticky=tk.W, pady=2)

ttk.Label(main_frame, text="Пароль").grid(row=2, column=0, sticky=tk.W, pady=2)
password_entry = ttk.Entry(main_frame, width=30, show="*")
password_entry.grid(row=2, column=1, sticky=tk.W, pady=2)

ttk.Label(main_frame, text="Подтвердите пароль").grid(row=3, column=0, sticky=tk.W, pady=2)
confirm_password_entry = ttk.Entry(main_frame, width=30, show="*")
confirm_password_entry.grid(row=3, column=1, sticky=tk.W, pady=2)


ttk.Label(main_frame, text="Ваша специализация").grid(row=4, column=0, sticky=tk.W, pady=2)
specialization = tk.StringVar(value="Web-мастер")
specialization_combo = ttk.Combobox(main_frame, textvariable=specialization, width=27)
specialization_combo['values'] = ("Web-мастер", "Frontend разработчик", "Backend разработчик", "Fullstack разработчик")
specialization_combo.grid(row=4, column=1, sticky=tk.W, pady=2)


ttk.Label(main_frame, text="Пол").grid(row=5, column=0, sticky=tk.W, pady=2)
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=5, column=1, sticky=tk.W)
gender = tk.IntVar()
male_radio = ttk.Radiobutton(gender_frame, text="М", variable=gender, value=1)
male_radio.pack(side=tk.LEFT)
female_radio = ttk.Radiobutton(gender_frame, text="Ж", variable=gender, value=2)
female_radio.pack(side=tk.LEFT)


ttk.Label(main_frame, text="Ваши навыки").grid(row=6, column=0, sticky=tk.NW, pady=2)
skills_frame = ttk.Frame(main_frame)
skills_frame.grid(row=6, column=1, sticky=tk.W)

skills = {
    "HTML и CSS": tk.BooleanVar(),
    "Perl": tk.BooleanVar(),
    "ASP": tk.BooleanVar(),
    "Adobe Photoshop": tk.BooleanVar(),
    "JAVA": tk.BooleanVar(),
    "JavaScript": tk.BooleanVar(),
    "Flash": tk.BooleanVar()
}

for i, (skill, var) in enumerate(skills.items()):
    cb = ttk.Checkbutton(skills_frame, text=skill, variable=var)
    cb.grid(row=i, column=0, sticky=tk.W)


ttk.Label(main_frame, text="Дополнительные сведения о себе").grid(row=7, column=0, sticky=tk.NW, pady=2)
info_text = tk.Text(main_frame, width=30, height=5)
info_text.grid(row=7, column=1, sticky=tk.W, pady=2)


buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=8, column=0, columnspan=2, pady=10)

register_button = ttk.Button(buttons_frame, text="Зарегистрировать", command=register)
register_button.pack(side=tk.LEFT, padx=5)

clear_button = ttk.Button(buttons_frame, text="Очистить форму", command=clear_form)
clear_button.pack(side=tk.LEFT, padx=5)


root.mainloop()

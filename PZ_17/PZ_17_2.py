import tkinter as tk
from tkinter import ttk, messagebox


def check_number():
    input_value = entry.get()

    try:
        A = int(input_value)

        if A % 2 == 0:
            result_label.config(text="Результат: True (число четное)", foreground="green")
        else:
            result_label.config(text="Результат: False (число нечетное)", foreground="red")

    except ValueError:
        messagebox.showerror("Ошибка", "Неправильно ввели! Введите целое число.")
        entry.delete(0, tk.END)
        entry.focus()


root = tk.Tk()
root.title("Проверка числа")
root.geometry("400x200")


main_frame = ttk.Frame(root, padding="20")
main_frame.pack(expand=True, fill=tk.BOTH)


label = ttk.Label(main_frame, text="Введите целое число:")
label.pack(pady=5)

entry = ttk.Entry(main_frame, width=20)
entry.pack(pady=5)
entry.focus()

check_button = ttk.Button(main_frame, text="Проверить", command=check_number)
check_button.pack(pady=10)

result_label = ttk.Label(main_frame, text="Результат: ", font=('Arial', 10))
result_label.pack(pady=5)


entry.bind('<Return>', lambda event: check_number())

root.mainloop()

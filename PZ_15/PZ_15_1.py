# Приложение  КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
# состав должна содержать следующие данные: Табельный номер,
# Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.

import sqlite3 as sq
from tabulate import tabulate


string_for_db = [('1', 'Иванов', 'Иван', 'Иванович', '1980-05-15', 'Профессор', 'Доктор наук', 1.0, 120000),
                 ('2', 'Петров', 'Сергей', 'Александрович', '1978-03-22', 'Доцент', 'Кандидат наук', 0.8, 95000),
                 ('3', 'Сидорова', 'Ольга', 'Владимировна', '1985-07-14', 'Старший преподаватель', 'Кандидат наук', 0.7, 75000),
                 ('4', 'Кузнецов', 'Дмитрий', 'Петрович', '1990-11-30', 'Ассистент', 'Магистр', 1.0, 55000),
                 ('5', 'Васильева', 'Елена', 'Сергеевна', '1982-09-18', 'Профессор', 'Доктор наук', 1.0, 125000),
                 ('6', 'Смирнов', 'Алексей', 'Игоревич', '1975-12-05', 'Доцент', 'Кандидат наук', 0.9, 100000),
                 ('7', 'Попова', 'Наталья', 'Викторовна', '1988-04-25', 'Ассистент', 'Кандидат наук', 0.5, 60000),
                 ('8', 'Фёдоров', 'Михаил', 'Олегович', '1983-08-12', 'Старший преподаватель', 'Кандидат наук', 0.6, 70000),
                 ('9', 'Николаева', 'Анна', 'Дмитриевна', '1992-02-28', 'Преподаватель', 'Магистр', 0.8, 65000),
                 ('10', 'Козлов', 'Андрей', 'Борисович', '1970-06-10', 'Профессор', 'Доктор наук', 1.0, 140000)]


with sq.connect('vuz.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS kafedra 
    (tab_num CHAR(4) PRIMARY KEY, 
    last_name varchar(25) NOT NULL, 
    first_name varchar(15) NOT NULL, 
    middle_name varchar(15) NOT NULL, 
    birth_day DATE NOT NULL,
    dolzn varchar(15) NOT NULL, 
    scient_degree varchar(25), 
    workload integer, 
    salery decimal(7,2))""")
    cur.executemany("INSERT INTO kafedra VALUES (?,?,?,?,?,?,?,?,?)", string_for_db)


    def print_table():
        cur.execute("SELECT * FROM kafedra")
        headers = ["Таб.№", "Фамилия", "Имя", "Отчество", "Дата рожд.", "Должность", "Уч.степень", "Ставка", "Зарплата"]
        print(tabulate(cur.fetchall(), headers=headers, tablefmt="grid"))


    print("\nИсходная таблица:")
    print_table()

    print("\n1. Сотрудники с зарплатой выше 100000:")
    cur.execute("SELECT * FROM kafedra WHERE salery > 100000")
    headers = ["Таб.№", "Фамилия", "Имя", "Отчество", "Дата рожд.", "Должность", "Уч.степень", "Ставка", "Зарплата"]
    print(tabulate(cur.fetchall(), headers=headers, tablefmt="grid"))

    print("\n2. Количество сотрудников с зарплатой выше 100000:")
    cur.execute("SELECT COUNT(*) FROM kafedra WHERE salery > 100000")
    print(f"Результат: {cur.fetchone()[0]}")

    print("\n3. Количество сотрудников с зарплатой от 50000 до 100000:")
    cur.execute("SELECT COUNT(*) FROM kafedra WHERE salery BETWEEN 50000 AND 100000")
    print(f"Результат: {cur.fetchone()[0]}")

    print("\n4. Обновление зарплаты (75000 → 80000):")
    cur.execute("UPDATE kafedra SET salery = 80000 WHERE salery = 75000")
    print("Зарплата обновлена. Обновленная таблица:")
    print_table()

    print("\n5. Повышение зарплаты профессорам на 10%:")
    cur.execute("UPDATE kafedra SET salery = salery * 1.1 WHERE dolzn = 'Профессор'")
    print("Зарплата профессоров увеличена. Обновленная таблица:")
    print_table()

    print("\n6. Изменение ставки ассистентам-кандидатам наук на 1.0:")
    cur.execute("UPDATE kafedra SET workload = 1.0 WHERE dolzn = 'Ассистент' AND scient_degree = 'Кандидат наук'")
    print("Ставка изменена. Обновленная таблица:")
    print_table()

    cur.execute("DELETE FROM kafedra WHERE dolzn = 'Ассистент'")
    print("\n1. После удаления ассистентов:")
    print_table()

    cur.execute("DELETE FROM kafedra WHERE salery > 100000")
    print("\n2. После удаления сотрудников с зарплатой >100000:")
    print_table()

    cur.execute("DELETE FROM kafedra WHERE birth_day > '1980-01-01'")
    print("\n3. После удаления сотрудников, родившихся после 1980 года:")
    print_table()

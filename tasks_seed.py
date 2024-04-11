from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 3
NUMBER_TASKS = 30


def generate_fake_data(number_users, number_tasks) -> tuple:
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()

    for _ in range(number_users):
        user = {
            'full name': fake_data.name(),
            'email': fake_data.ascii_free_email()
        }
        fake_users.append(user)

    for _ in range(number_tasks):
        task = {
            'title': fake_data.word(),
            'description': fake_data.sentence()
        }
        fake_tasks.append(task)
        
    return fake_users, fake_tasks

def prepare_data(users, tasks) -> tuple:
    for_users_id = []  # для таблиці users_id
    for user in users:
        for_users_id.append((user['full name'], user['email']))

    for_tasks = []  # для таблиці tasks
    for task in tasks:
        # Виконуємо цикл за tasks
        for_tasks.append((task['title'], task['description'], randint(1, 3), randint(1, len(users))))

    return for_tasks, for_users_id

def insert_data_to_db(tasks, users) -> None:
# Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними

    with sqlite3.connect('tasks.db') as con:

        cur = con.cursor()

        sql_to_tasks = """INSERT INTO tasks(title, task_description, status_id, user_id)
                               VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)

        sql_to_users = """INSERT INTO users(fullname, email)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)

        con.commit()

if __name__ == "__main__":
    tasks, users = prepare_data(*generate_fake_data( NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(tasks, users)
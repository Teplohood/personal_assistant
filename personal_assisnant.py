import json
import csv
import os
from datetime import datetime
import matplotlib
import pandas as pd
# Утилиты/функции
def load_data(file_path):
    """Загружает данные из JSON-файла."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(file_path, data):
    """Сохраняет данные в JSON-файл."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def validate_date(date_string, format="%d-%m-%Y"):
    """Проверяет корректность введённой даты."""
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False
# Менеджер заметок
class Note:
    FILE_PATH = 'notes.json'

    def __init__(self, title, content):
        self.id = int(datetime.now().timestamp())
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return self.__dict__

class NotesManager:
    @staticmethod
    def create_note():
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        note = Note(title, content)
        notes = load_data(Note.FILE_PATH)
        notes.append(note.to_dict())
        save_data(Note.FILE_PATH, notes)
        print("Заметка успешно добавлена")
    @staticmethod
    def view_notes():
        notes = load_data(Note.FILE_PATH)
        if not notes:
            print("Нет заметок")
            return
        for note in notes:
            print(f"ID: {note['id']} | Заголовок: {note['title']} | Дата: {note['timestamp']}")
    @staticmethod
    def delete_note():
        note_id = input("Введите ID заметки для удаления: ")
        notes = load_data(Note.FILE_PATH)
        updated_notes = [note for note in notes if str(note['id']) != note_id]
        save_data(Note.FILE_PATH, updated_notes)
        print("Заметка удалена")
    @staticmethod
    def export_to_csv():
        notes = load_data(Note.FILE_PATH)
        file_name = 'notes_export.csv'
        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['id', 'title', 'content', 'timestamp'])
            writer.writeheader()
            writer.writerows(notes)
        print(f"Заметки экспортированы в {file_name}!")
# Менеджер задач
class Task:
    FILE_PATH = 'tasks.json'
    def __init__(self, description, deadline):
        self.id = int(datetime.now().timestamp())
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return self.__dict__
class TasksManager:
    @staticmethod
    def create_task():
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения (формат: DD-MM-YYYY): ")
        if not validate_date(deadline):
            print("Некорректная дата. Задача не дабавлена")
            return
        task = Task(description, deadline)
        tasks = load_data(Task.FILE_PATH)
        tasks.append(task.to_dict())
        save_data(Task.FILE_PATH, tasks)
        print("Задача успешно добавлена")
    @staticmethod
    def view_tasks():
        tasks = load_data(Task.FILE_PATH)
        if not tasks:
            print("Нет задач.")
            return
        for task in tasks:
            print(f"ID: {task['id']} | Описание {task['description']} | Дедлайн: {task['deadline']} | Создано: {task['created_at']}")

    @staticmethod
    def delete_task():
        task_id = input("Введите ID задачи для удаления: ")
        tasks = load_data(Task.FILE_PATH)
        updated_tasks = [task for task in tasks if str(task['id']) != task_id]
        save_data(Task.FILE_PATH, updated_tasks)
        print("Задача удаленa")

# Менеджер контактов
class Contact:
    FILE_PATH = 'contacts.json'
    def __init__(self, name, phone, email):
        self.id = int(datetime.now().timestamp())
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return self.__dict__
class ContactsManager:
    @staticmethod
    def add_contact():
        name = input("Введите имя: ")
        phone = input("Введите номер телефона ")
        email = input("Введите email: ")
        contact = Contact(name, phone, email)
        contacts = load_data(Contact.FILE_PATH)
        contacts.append(contact.to_dict())
        save_data(Contact.FILE_PATH, contacts)
        print("Контакт успешно добавлен")

    @staticmethod
    def view_contacts():
        contacts = load_data(Contact.FILE_PATH)
        if not contacts:
            print("Нет контактов")
            return
        for contact in contacts:
            print(f"ID: {contact['id']} | Имя: {contact['name']} | Телепхон: {contact['phone']} | Email: {contact['email']}")
    @staticmethod
    def delete_contact():
        contact_id = input("Введите ID контакта для удаления: ")
        contacts = load_data(Contact.FILE_PATH)
        updated_contacts = [contact for contact in contacts if str(contact['id']) != contact_id]
        save_data(Contact.FILE_PATH, updated_contacts)
        print("Контакт удалён")
# Финансовый менеджмент
class FinanceManager:
    FILE_PATH = 'finance.json'

    @staticmethod
    def add_transaction():
        description = input("Введите описание транзакции: ")
        amount = float(input("Введите сумму транзакции: "))
        date = input("Введите дату (формат: DD-MM-YYYY): ")
        if not validate_date(date):
            print("Некорректная дата. Транзакция не добавлена")
            return
        transactions = load_data(FinanceManager.FILE_PATH)
        transactions.append({"description": description, "amount": amount, "date": date})
        save_data(FinanceManager.FILE_PATH, transactions)
        print("Транзакция добавлена")
    @staticmethod
    def view_transactions():
        transactions = load_data(FinanceManager.FILE_PATH)
        if not transactions:
            print("Нет транзакций.")
            return
        for transaction in transactions:
            print(f"Описание: {transaction['description']} | Сумма: {transaction['amount']} | Дата: {transaction['date']}")
# Кулькулятор
class Calculator:
    @staticmethod
    def calculate():
        expression = input("Введите выражение:  ")
        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка вычисления: {e}")
# Меню
def main_menu():
    while True:
        print("\n Добро пожаловать в Персональный помощник!")
        print("1. Управление заметками")
        print("2 Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансами")
        print("5. Калькулятор")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            notes_menu()
        elif choice == "2":
            tasks_menu()
        elif choice == "3":
            contacts_menu()
        elif choice == "4":
            finance_menu()
        elif choice == "5":
            Calculator.calculate()
        elif choice == "6":
            print("Выход из приложения.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова")
def notes_menu():
    while True:
        print("\n Управление заметками:")
        print("1. Добавить заметку")
        print("2. Посмотреть заметки")
        print("3. Удалить заметку")
        print("4. Экспорт заметок в CSV")
        print("5. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            NotesManager.create_note()
        elif choice == "2":
            NotesManager.view_notes()
        elif choice == "3":
            NotesManager.delete_note()
        elif choice == "4":
            NotesManager.export_to_csv()
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте снова")


def tasks_menu():
    while True:
        print("\n Управление задачами:")
        print("1. Добавить задачу")
        print("2. Посмотреть задачи")
        print("3. Удалить задачу")
        print("4. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            TasksManager.create_task()
        elif choice == "2":
            TasksManager.view_tasks()
        elif choice == "3":
            TasksManager.delete_task()
        elif choice == "4":
            break
        else:
            print("Некорректный выбор. Попробуйте снова")

def contacts_menu():
    while True:
        print("\n Управление контактами:")
        print("1. Добавить контакт")
        print("2. Посмотреть контакты")
        print("3. Удалить контакт")
        print("4. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            ContactsManager.add_contact()
        elif choice == "2":
            ContactsManager.view_contacts()
        elif choice == "3":
            ContactsManager.delete_contact()
        elif choice == "4":
            break
        else:
            print("Некорректный выбор. Попробуйте снова")

def finance_menu():
    while True:
        print("\n Управление финансами:")
        print("1. Добавить транзакцию")
        print("2. Посмотреть транзакции")
        print("3. Назад")
        choice = input("Выберите действие: ")
        if choice == "1":
            FinanceManager.add_transaction()
        elif choice == "2":
            FinanceManager.view_transactions()
        elif choice == "3":
            break
        else:
            print("Некорректный выбор. Попробуйте снова")

if __name__ == "__main__":
    main_menu()    

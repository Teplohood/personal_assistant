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

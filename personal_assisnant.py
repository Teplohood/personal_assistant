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
import csv
import os

# Укажите путь к директории с текстовыми файлами
directory = r'C:\Users\User\Desktop\prompts'

# Обходим все файлы в директории
for filename in os.listdir(directory):
    # Обрабатываем только текстовые файлы
    if filename.endswith('.txt'):
        # Создаем имя для CSV файла
        csv_filename = f"{os.path.splitext(filename)[0]}.csv"

        # Открываем файлы для чтения и записи
        with open(os.path.join(directory, filename), 'r') as txt_file, open(
                os.path.join(directory, csv_filename), 'w',
                newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Записываем заголовок CSV
            writer.writerow(['name', 'prompt', 'negative_prompt'])

            # Читаем каждую строку из текстового файла
            for line in txt_file:
                # Удаляем пробелы по краям и игнорируем пустые строки
                line = line.strip()
                if line:
                    # Записываем строку в CSV файл
                    writer.writerow([line, f'{line}, ', ''])
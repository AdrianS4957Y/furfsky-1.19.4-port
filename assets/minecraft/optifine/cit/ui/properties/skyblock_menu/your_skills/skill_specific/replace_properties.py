import os
import re
import argparse

# Словарь с заменами для не найденных ID
id_replacements = {
    #'itemnbt.display.Lore.*=ipattern:*unlocked': 'item\nnbt.display.Lore.*=ipattern:*unlocked',
    #"nbt.display.Lore.*=ipattern:*unlockednbt.display.Lore.*=ipattern:*unlocked":"nbt.display.Lore.*=ipattern:*unlocked",
    #"greennbt.display.Lore.*=ipattern:*unlocked":"green",
    #"nbt.display.Name=iregex:.":"nbt.display.Name=iregex:^((?!unlocked).)",
    #"_complete_bar_green":"_incomplete_bar_green"
}

# Функция для замены идентификаторов в одном файле
def replace_ids_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        original_content = content
        
        # Замена всех найденных ID
        for old_id, new_id in id_replacements.items():
            content = re.sub(re.escape(old_id), new_id, content)
        
        if content != original_content:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Сканирование папки и замена идентификаторов в каждом файле .properties
def replace_ids_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.properties'):
                file_path = os.path.join(root, file)
                replace_ids_in_file(file_path)

# Основная функция
def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description='Replace IDs in .properties files.')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing .properties files')
    
    # Парсинг аргументов командной строки
    args = parser.parse_args()
    
    # Получение пути к папке из аргументов
    folder_path = args.folder_path
    
    # Запуск замены ID
    replace_ids_in_folder(folder_path)

if __name__ == '__main__':
    main()

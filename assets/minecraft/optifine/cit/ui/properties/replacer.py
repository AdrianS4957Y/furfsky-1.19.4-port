import os

def replace_in_file(file_path, old_word, new_word):
    """Функция для замены слова в файле."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Заменяем все вхождения old_word на new_word
        new_content = content.replace(old_word, new_word)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f'Заменено в файле: {file_path}')
    except Exception as e:
        print(f'Ошибка при обработке файла {file_path}: {e}')

def replace_word_in_folder(root_folder, old_word, new_word):
    """Функция для рекурсивного обхода папок и замены слов в текстовых файлах."""
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            # Поддержка только текстовых файлов (например, .txt, .properties, .json)
            if filename.endswith(('.txt', '.properties', '.json', '.md', '.yml', '.yaml')):
                file_path = os.path.join(dirpath, filename)
                replace_in_file(file_path, old_word, new_word)

# Пример использования
if __name__ == "__main__":
    # Укажите папку, в которой нужно выполнить замену
    root_folder = '/home/adrians4957y/.minecraft/versions/1.19 Hypixel/resourcepacks/§aFurfSky Reborn §8§lFULL§8/assets/minecraft/optifine/cit/ui/properties'
    old_word = 'mcpatcher'  # Слово для замены
    new_word = 'optifine'  # Новое слово
    
    replace_word_in_folder(root_folder, old_word, new_word)
    print("Завершено!")

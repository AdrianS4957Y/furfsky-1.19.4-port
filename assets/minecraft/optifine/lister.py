import os

def print_directory_structure(root_dir, level=0, max_depth=None):
    """
    Рекурсивно печатает структуру директорий без файлов, с ограничением глубины.
    
    :param root_dir: Путь к корневой директории
    :param level: Уровень вложенности
    :param max_depth: Максимальная глубина рекурсии
    """
    # Если максимальная глубина достигнута, прекращаем рекурсию
    if max_depth is not None and level > max_depth:
        return
    
    try:
        # Получаем список элементов в директории
        items = os.listdir(root_dir)
    except PermissionError:
        print("Нет прав на доступ к директории:", root_dir)
        return
    
    # Проходим по элементам директории
    for item in items:
        # Полный путь к элементу
        item_path = os.path.join(root_dir, item)
        
        # Проверяем, является ли элемент директорией
        if os.path.isdir(item_path):
            # Печатаем директорию с отступами в зависимости от уровня вложенности
            print(' ' * (level * 4) + f'[{item}]')
            # Рекурсивно печатаем содержимое директории
            print_directory_structure(item_path, level + 1, max_depth)

if __name__ == "__main__":
    # Укажите путь к корневой директории вашего ресурспака
    root_directory = "."
    
    # Установите максимальную глубину рекурсии (например, 3). Установите в None для неограниченной глубины.
    max_depth = 2
    
    print("Структура папок ресурспака:")
    print_directory_structure(root_directory, max_depth=max_depth)

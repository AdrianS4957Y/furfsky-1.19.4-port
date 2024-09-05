import os
import re
import argparse

# Словарь с заменами для не найденных ID
id_replacements = {
    #'minecraft:skull': 'minecraft:player_head',
#    'minecraft:glass': 'minecraft:red_stained_glass_pane',
    #'minecraft:stained_hardened_clay': 'minecraft:terracotta',
    #'minecraft:red_flower': 'minecraft:poppy',  # Пример замены для red_flower
    #'minecraft:firework_charge': 'minecraft:firework_rocket',  # Пример замены для firework_charge
    #'minecraft:netherbrick': 'minecraft:nether_brick',
    #'\nnbt.display.Lore.*=ipattern:*Reward*:*':"",
    #'\ndamage=14':'',
    #'minecraft:grass_block_block':"minecraft:grass_block",
    #"minecraft:deadbush":"minecraft:dead_bush",
    #"minecraft:yellow_flower": "minecraft:dandelion",
    #"minecraft:waterlily": "minecraft:water_lily",
    #"minecraft:double_plant": "minecraft:tall_grass",
    #"minecraft:fireworks": "minecraft:firework_rocket",
    #"minecraft:web": "minecraft:cobweb",
    #"minecraft:golden_rail": "minecraft:golden_rail",
    #"minecraft:reeds": "minecraft:sugar_cane",
    #"minecraft:tallgrass": "minecraft:tall_grass",
    #"minecraft:quartz_ore": "minecraft:nether_quartz_ore",
    #"minecraft:record_cat": "minecraft:music_disc_cat",
    #"minecraft:noteblock": "minecraft:note_block",
     "ExtremeHillsEdge":"extreme_hills_edge"
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

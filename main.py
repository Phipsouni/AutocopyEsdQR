import os
import shutil
import time

def copy_files_to_folders(src_directory, dest_directory):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.startswith('qr') or file.startswith('ЭСД'):
                dest_folder = os.path.join(dest_directory, root.split(os.path.sep)[-1])
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_folder, file)
                shutil.copy2(src_file, dest_file)

if __name__ == "__main__":
    # Читаем пути из файла path.txt
    with open('path.txt', 'r') as f:
        lines = f.read().splitlines()
        source_directory = lines[0]
        destination_directory = lines[1]

    copy_files_to_folders(source_directory, destination_directory)

    directory = destination_directory

    # Получаем список имен папок в директории
    foldernames = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    # Сортируем имена папок по возрастанию первой цифры
    foldernames_sorted = sorted(foldernames, key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Записываем отсортированные имена папок в файл sorted_names.txt
    with open("sorted_names.txt", "w") as file:
        for name in foldernames_sorted:
            file.write(name + "\n")

    input_file = 'foldernames.txt'
    output_file = 'new_foldernames.txt'

    with open(input_file, 'r') as file:
        names = file.readlines()

    with open(output_file, 'w') as file:
        for i, name in enumerate(names, start=1):
            new_name = f"{i}_{name.strip()}"
            file.write(new_name + '\n')

    print("Готово! Новые названия добавлены в файл new_foldernames.txt")

    # Читаем список старых и новых имен папок
    with open('sorted_names.txt', 'r') as f:
        sorted_names = f.read().splitlines()

    with open('new_foldernames.txt', 'r') as f:
        foldernames = f.read().splitlines()

    # Выполняем переименование папок
    for old_name, new_name in zip(sorted_names, foldernames):
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)

    # Выводим сообщение о завершении
    print(f"ЭСД и QR успешно скопированы в директорию: {destination_directory}")

    # Ожидание 3 секунды перед завершением выполнения скрипта
    time.sleep(3)
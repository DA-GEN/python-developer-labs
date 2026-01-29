import os

# Получаем абсолютный путь к папке, где находится текущий скрипт
script_dir = os.path.dirname(__file__)

# Создаем полный путь к файлу input.txt
input_file_path = os.path.join(script_dir, 'input.txt')
output_file_path = os.path.join(script_dir, 'stats.txt')

def main():
    with open(input_file_path, "r", encoding="utf-8") as file_in, \
         open(output_file_path, "w", encoding="utf-8") as file_out:
        
        lines_count = 0
        words_count = 0

        for line in file_in: 
            lines_count += 1
            words_count += len(line.split())

        file_out.write(f'Lines: {lines_count}\n')
        file_out.write(f'Words: {words_count}\n')

if __name__ == "__main__":
    main()
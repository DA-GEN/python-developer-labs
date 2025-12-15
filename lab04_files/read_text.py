import os

# Получаем абсолютный путь к папке, где находится текущий скрипт
script_dir = os.path.dirname(__file__)

# Создаем полный путь к файлу input.txt
input_file_path = os.path.join(script_dir, 'input.txt')
output_file_path = os.path.join(script_dir, 'stats.txt')

input = open(input_file_path, "r")
output = open(output_file_path, "w")


lines = 0
words = 0

for l in input:
    lines += 1
    list_in_line = map(str, l.split())
    for w in list_in_line:
        words += 1

output.write(f'Lines: {lines}\n')
output.write(f'Words: {words}')

input.close()
output.close()
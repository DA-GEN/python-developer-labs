import csv
import os

script_dir = os.path.dirname(__file__)
input_file_path = os.path.join(script_dir, 'students_stats.csv')

all_students_data = []
stats = []

with open(input_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        all_students_data.append(row) 
        stats.append(int(row['stats']))

mid_stat = sum(stats)/len(stats)
max_stat = max(stats)
max_name = ""

for row in all_students_data:
    if int(row["stats"]) == max_stat: 
        max_name = row["name"]
        break 

print(f'Max grade is: {max_stat} by {max_name}.')
print(f'Mid grade is: {mid_stat}.')
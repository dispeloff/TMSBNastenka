import os
import time
import re
from datetime import datetime

while True:
    time.sleep(5)
    current_datetime = datetime.now()
    date_string = current_datetime.strftime("%Y-%m-%d")
    input_file_name = f'all_{date_string}.log'
    print(input_file_name)
    input_file_path = os.path.join(r'C:\Users\dispeloff\AppData\Roaming\MCSkill\updates\TechnoSkyBlock_1.7.10\logs\TabbyChat\s23.mcskill.net(28018)', input_file_name)
    output_file_path = 'TimeToRestart.txt'
    target_string = "] [Настенька -> Я] До рестарта:"

    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()
    except FileNotFoundError:
        print(f"Файл '{input_file_path}' не найден.")
        lines = []

    found = False
    time_formatted = None

    for line in reversed(lines):
        if target_string in line:
            data = line.split("До рестарта: ")[1]
            match = re.search(r"(\d+) час\(а\), (\d+) минут, (\d+) секунд", data)

            if match:
                hours = int(match.group(1))
                minutes = int(match.group(2))
                seconds = int(match.group(3))
                time_formatted = (f"{hours}ч. {minutes}м.")
                with open(output_file_path, 'w') as output_file:
                    output_file.write(time_formatted)
                found = True
                break

    if found:
        print(f"Самая последняя строка с '{target_string}' найдена и записана в файл '{output_file_path}': {time_formatted}")
    else:
        print(f"Строка '{target_string}' не найдена в файле '{input_file_path}'")

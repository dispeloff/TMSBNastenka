import math
from PIL import ImageGrab
import time
import re
import pyautogui
import pygetwindow as gw
from mcstatus import JavaServer
timeout = 10
server_address = "s23.mcskill.net:28018"
process_name = f'MCSkill.net | Techno-Magic Sky-Block [1.7.10] | Игрок: dispeloff'

# Функция для чтения файла и поиска строки "[Настенька -> Я] До рестарта:"
def read_and_extract_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            log_content = file.read()
            match = re.findall(r'\[Настенька -> Я\] До рестарта:(.*?)\n', log_content, re.DOTALL)
            if match:
                return match[0]
            else:
                return "Текст не найден"
    except FileNotFoundError:
        return "Файл не найден"
    except Exception as e:
        return f"Произошла ошибка: {e}"

def find_and_activate_window(process_name):
    try:
        # Ищем окно процесса с заданным именем
        window = gw.getWindowsWithTitle(process_name)
        if window:
            # Если находим окно, активируем его (разворачиваем, если было свернуто)
            window[0].activate()
            window[0].maximize()  # Максимизируем окно
            return window[0]  # Возвращаем объек789т окна
        else:
            print(f"Окно процесса {process_name} не найдено.")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
def getPress():
    find_and_activate_window(process_name)
    time.sleep(1.5)
    pyautogui.press('num7')
    time.sleep(0.5)
    time.sleep(timeout)
    log_text = read_and_extract_log(r"C:\Users\dispeloff\AppData\Roaming\MCSkill\updates\TechnoSkyBlock_1.7.10\logs\TabbyChat\s23.mcskill.net(28018)\all_2023-11-06.log")
    # print(log_text)
while True:
    time.sleep(timeout)
    try:
        server = JavaServer.lookup(server_address)
        if server:
            # Координаты, по которым нужно кликать
            click_x = 263
            click_y = 119
            click1_x = 679
            click1_y = 291
            click2_x = 712
            click2_y = 472
            click3_x = 709
            click3_y = 470
            click4_x = 444
            click4_y = 595

            # Координаты, где нужно проверять наличие цветов
            check_x = 286
            check_y = 91

            # Ожидаемые цвета
            expected_color = (255, 0, 0)  # Красный
            other_color = (0, 255, 0)  # Зеленый

            # Захватываем скриншот области для проверки цвета
            screenshot = ImageGrab.grab(bbox=(check_x-5, check_y-5, check_x + 5, check_y + 5))
            pixel_color = screenshot.getpixel((0, 0))

            if pixel_color == expected_color:
                print("Найден красный пиксель. Не выполняем клик.")
                time.sleep(timeout)
            elif pixel_color == other_color:
                print("Найден зеленый пиксель. Не выполняем клик.")
            else:
                # Кликаем ЛКМ по указанным координатам
                getPress()
                time.sleep(timeout)
                pyautogui.click(click_x, click_y)
                pyautogui.click(click1_x, click1_y)
                pyautogui.click(click1_x, click1_y)
                pyautogui.click(click1_x, click1_y)
                time.sleep(timeout)
                pyautogui.click(click2_x, click2_y)
                pyautogui.click(click2_x, click2_y)
                pyautogui.click(click2_x, click2_y)
                time.sleep(timeout)
                pyautogui.click(click3_x, click3_y)
                pyautogui.click(click3_x, click3_y)
                pyautogui.click(click3_x, click3_y)
                time.sleep(timeout)
                pyautogui.click(click4_x, click4_y)
                pyautogui.click(click4_x, click4_y)
                pyautogui.click(click4_x, click4_y)
                time.sleep(timeout)
                # Пауза, чтобы не кликать слишком часто
                status = server.status()
                latency = math.floor(server.ping())
                print(f"Online: {status.players.online} , Ping: {latency} ms")
                print(f"Techno-Magic-Sky-Block\nprocess name: {process_name}")

    except:
        print("Server offline!")
        time.sleep(timeout)

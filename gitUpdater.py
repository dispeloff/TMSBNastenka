import base64
import time
import requests
import os

while True:
    def gitUpdate():
        github_token = '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'
        repository_owner = 'dispeloff'
        repository_name = 'TMSBNastenka'
        directory_to_update = 'my_directory'  # Изменено на имя директории

        # Получите список файлов в директории
        file_list = os.listdir(directory_to_update)

        for file_name in file_list:
            # Сформируйте полный путь к файлу
            file_path = os.path.join(directory_to_update, file_name)

            # Прочитайте содержимое файла
            with open(file_path, 'r') as file:
                new_file_content = file.read()

            def update_github_file(token, repo_owner, repo_name, file_path, new_content):
                # Подготовьте URL и заголовки для запроса
                url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
                headers = {
                    'Authorization': f'Bearer {token}'
                }

                # Получите текущее содержимое файла
                response = requests.get(url, headers=headers)
                response_data = response.json()

                # Подготовьте данные для обновления файла
                file_content = base64.b64encode(new_content.encode()).decode()
                update_data = {
                    "message": f"Обновление файла {file_path}",  # Изменено сообщение
                    "content": file_content,
                    "sha": response_data['sha']
                }

                # Отправьте запрос на обновление файла
                update_response = requests.put(url, json=update_data, headers=headers)

                if update_response.status_code == 200:
                    print(f'Файл {file_path} успешно обновлен.')

                else:
                    print(f'Произошла ошибка при обновлении файла {file_path}.')
                    print(f'Код состояния: {update_response.status_code}')
                    print(update_response.text)

            update_github_file(github_token, repository_owner, repository_name, file_path, new_file_content)

        print("ОБНОВЛЕНИЕ: 15 секунд...")
        time.sleep(15)

    gitUpdate()

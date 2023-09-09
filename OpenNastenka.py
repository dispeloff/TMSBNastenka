import base64
import time

import requests


def gitUpdate():
    nextRestartTime = "123"
    github_token = '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'
    repository_owner = 'dispeloff'
    repository_name = 'TMSBNastenka'
    file_to_update = 'OpenNastenka.py'
    new_file_content = "test word!"

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
            "message": "Обновление файла test.txt",
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

    update_github_file(github_token, repository_owner, repository_name, file_to_update, new_file_content)
    print("ОБНОВЛЕНИЕ: 15 секунд...")
    time.sleep(15)


gitUpdate()


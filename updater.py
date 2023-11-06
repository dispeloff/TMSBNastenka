import base64
import time
import requests

while True:
    def gitUpdate():
        github_token = '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'
        repository_owner = 'dispeloff'
        repository_name = 'TMSBNastenka'
        file_to_update_LUA = 'OpenNastenka.lua'
        file_to_update_PY = 'OpenNastenka.py'
        file_to_update_Restart = 'TimeToRestart.txt'
        with open('OpenNastenka.lua', 'r') as lua_file:
            new_file_content_LUA = lua_file.read()
        with open('OpenNastenka.lua', 'r') as py_file:
            new_file_content_PY = py_file.read()
        with open('TimeToRestart.txt', 'r') as restart_file:
            new_file_content_Restart = restart_file.read()

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
                "message": "Обновление файла OpenNastenka.lua",  # Изменено сообщение
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

        update_github_file(github_token, repository_owner, repository_name, file_to_update_LUA, new_file_content_LUA)
        #update_github_file(github_token, repository_owner, repository_name, file_to_update_PY, new_file_content_PY)
        update_github_file(github_token, repository_owner, repository_name, file_to_update_Restart, new_file_content_Restart)
        print("ОБНОВЛЕНИЕ: 30 секунд...")
        time.sleep(30)

    gitUpdate()

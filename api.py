import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data =response.json()

    with open("get_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    print('Данные успешно сохранены')
else:
    print(f'Ошибка при подключении к API, {response.status_code}')
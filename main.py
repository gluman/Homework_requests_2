from pprint import pprint
import requests
from Settings import TOKEN as token
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    base_host = 'https://cloud-api.yandex.net'

    def get_headers(self):
        return {
            'Content-Type': 'applocation/json',
            'Authorization': f'OAuth {self.token}'
        }
    def _get_upload_link(self, path):
        uri = '/v1/disk/resource/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        pprint(response.json())
        return response.json()['href']

    def upload(self, local_path, yandex_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        upload_url = self._get_upload_link(yandex_path)
        # params = {'path': local_path, 'url': upload_url}
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print('Загрузка прошла успешно')



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    local_path = input('Введите путь до файла:')
    # ya_disk = 'disk:'
    ya_path = input('Введите папку для копирования и будущее название файла:')
    uploader = YaUploader(token)
    uploader.upload(local_path, ya_path)

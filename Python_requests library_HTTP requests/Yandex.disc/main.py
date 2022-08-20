import requests
from pprint import pprint


token = ''
url = 'https://cloud-api.yandex.net/v1/disk/resources/'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    # this method helps with requesting information from yandex.disc, sending the request with GET method
    def get_files_list(self):
        files_url = f'{url}files'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        response = requests.get(files_url, headers=headers, timeout=5)
        return response.json()

    # yandex.disc has specific requirement, in order to upload smth the link needed
    # method to get the link, we will get the link from json file
    def get_upload_link(self, disc_file_path):
        upload_url = f'{url}upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': disc_file_path, 'overwrite': 'true'} #path where upload the file, overwrite if the file is already there
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json() #returns the link

    def upload_file_to_disc(self, disc_file_path, filename):
        #Method to upload files from file_list to yandex.disc
        link_dict = self.get_upload_link(disc_file_path=disc_file_path)
        href = link_dict.get('href', '') #dictionary method, which will look for 'href' and return the value, otherwise it will return an empty string
        #upload file to yandex.disc:
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status() #checking if returning code has an error
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    ya = YaUploader(token=token)
    pprint(ya.upload_file_to_disc('poem.txt', 'poem.txt'))




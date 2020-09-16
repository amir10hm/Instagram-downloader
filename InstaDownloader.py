import requests
import re
from random import randrange

url = input('Enter your URL:')

def response_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        print('Conected to URL')

        pattern = re.compile(r'https://www.\w+.\w+/p/[a-zA-Z0-9_-]+/')  #make standard format for downloading with regax
        matches = pattern.finditer(url)
        for match in matches:
            url = match.group(0)

        return url
    elif r.status_code == 404:
        print('URL not found!')
        return None
    else:
        print('Wrong URL!!')
        return None

def download_image(url):
    url = url + 'media/?size=l'
    r = requests.get(url)
    name = str(randrange(0, 1000))
    with open(f'{name}.jpg', 'wb') as file:
        file.write(r.content)
    print('File downloaded')

download_image(response_url(url))

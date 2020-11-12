from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor


'''Скачать страницы с некоторых сайтов и посмотреть, сколько символов в каждом html.
Реализовать скачивание сразу в нескольких потоках. Использовать ThreadPoolExecutor и urllib.request.urlretrieve.
'''


def fetch(url):
    data = urlretrieve(url)
    html = open(data[0])
    l = html.read()
    html.close()
    return len(l)


urls = ['https://docs.python.org/3/',
        'http://python.org/',
        'https://docs.python.org/3/tutorial/introduction.html',
        'https://docs.python.org/3/library/concurrent.futures.html']


with ThreadPoolExecutor() as executor:
    for url in urls:
        r = executor.submit(fetch, url)
        print(f'Длина страницы {url} - {r.result()} символов')

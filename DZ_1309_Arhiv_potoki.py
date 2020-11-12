import zipfile
import threading
import time
from pathlib import Path

'''Написать программу, которая в отдельном потоке создает некий архив, 
в котором будет архивировано всё из указанной директории.
Протестировать, запустить сразу несколько таких потоков. 
Сравнить время создания архивов с помощью потоков и последовательно.
'''


# фуекция создает новый zip файл и архивирует в него файлы из указанной директории
# path путь к директории, которую нужно заархивировать
# path_filezip - путь к файлу zip с его именем
def arhiv(path, path_namezip):
    zip_path = Path(path_namezip)
    file_zip = zipfile.ZipFile(path_namezip, 'w', compression=zipfile.ZIP_DEFLATED)
    real_path = Path(path)
    for i in real_path.iterdir():
        if i != zip_path:
            file_zip.write(i)
    file_zip.close()


path = r'D:\PITON\ZipFiles'
# файлы zip сохраняются не в директории, которую архивируем -  'D:\PITON\ZipFiles'
t = time.time()
arhiv(path + r'\Dir_1', path + r'\zip_1.zip')
arhiv(path + r'\Dir_2', path + r'\zip_2.zip')
arhiv(path + r'\Dir_3', path + r'\zip_3.zip')
print('Время последовательного выполнения ', time.time() - t)

t_p = time.time()
threads = [threading.Thread(target=arhiv, args=(path + r'\Dir_1', path + r'\zip_1_p.zip')),
           threading.Thread(target=arhiv, args=(path + r'\Dir_2', path + r'\zip_2_p.zip')),
           threading.Thread(target=arhiv, args=(path + r'\Dir_3', path + r'\zip_3_p.zip')),
           ]

for i in threads:
    i.start()
    i.join()

print('Время выполнения через потоки ', time.time() - t_p)

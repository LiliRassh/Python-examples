'''         «Запоминающий» декоратор
Реализуйте декоратор, который запоминает результат прошлого вызова и хранит его в атрибуте «last_result».

Дополнительное задание: реализовать декоратор в виде функции.
'''


class decorator:

    def __init__(self, func):
        self.f = func
        self.last = None

    def __call__(self, *args, **kwargs):
        print('Результат прошлого расчета', self.last)
        self.last = self.f(*args, **kwargs)
        return self.last


@decorator
def extent(a, n):
    return a ** n


print(extent(2, 3))
print(extent(2, 4))
print(extent(2, 5))

#Дополнительное задание: реализовать декоратор в виде функции.


def extent_2(a):
    return a ** 2


extent_2 = decorator(extent_2)
print(extent_2(5))
print(extent_2(6))
print(extent_2(7))


'''       Файл
	Реализовать класс «Путь» (в  файловой системе).
	Реализовать свойство «Родительская директория», которое должно вернуть путь к родительской директории.
'''


class Path:

    def __init__(self, path_):
        self.p = path_

    @property
    def parent(self):
        p_path = self.p[:self.p.rfind('/')]
        return Path(p_path)

    def __str__(self):
        return f'File({self.p})'


p = Path('path=D:/PYTHON/DZ/dz_oop')
print(p)
print(p.parent)
print(p.parent.parent)
print(p.parent.parent.parent)




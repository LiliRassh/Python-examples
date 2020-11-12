from collections import OrderedDict

DialectTypes = {
    'sqlite3': ['TEXT', 'INTEGER', 'NULL', 'REAL', 'BLOB']
}


class QweryBilder:

    def __init__(self, name=None, dialect='sqlite3'):
        self.t_name = name
        self.colon = OrderedDict()      # упорядоченный словарь
        self.dialect = dialect

    # добавляем имя таблицы
    def add_table_name(self, table_name):
        self.t_name = table_name

    # добавляем столбцы таблицы, их имя и тип
    def add_field(self, colon_name, colon_type):
        if not self.check_type(colon_type):
            raise ValueError('wrong type!')
        if colon_name in self.colon:
            raise ValueError('same name!')
        self.colon[colon_name] = colon_type

    # проверка правильный ли тип данных
    def check_type(self, col_type):
        return col_type.upper() in DialectTypes[self.dialect]

    # поднимаем ошибку если нет имени таблицы
    def no_name(self):
        if self.t_name is None:
            raise ValueError('no table name!')

    # поднимаем ошибку если нет имени и типа солонок
    def no_field(self):
        if len(self.colon) == 0:
            raise ValueError('no information of colonm!')

    # получаем результат - запрос создания таблицы
    def get_qwery(self):
        self.no_name()
        self.no_field()
        s = ''
        k = 0
        for i, j in self.colon.items():
            if k != len(self.colon) - 1:
                s = s + f'{i} {j}' + ', '
                k += 1
                continue
            s = s + f'{i} {j}'
        return f'CREATE TABLE {self.t_name} (' + s + ');'


qw = QweryBilder()
qw.add_table_name(input('Введите имя таблицы: '))
qw.add_field('Name', 'TEXT')
qw.add_field('Age', 'INTEGER')
qw.add_field('Email', 'TEXT')

print(qw.get_qwery())

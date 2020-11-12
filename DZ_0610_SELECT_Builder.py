class SelectBuilder:

    def __init__(self):
        self.t_name = None
        self.field = None
        self.where = None
        self.order = None
        self.lim = None
        self.offset = None
        self.command = None

    # поднимаем ошибку если нет имени таблицы
    def no_name(self):
        if self.t_name is None:
            raise ValueError('no table name!')

    # поднимаем ошибку если нет имени и типа колонок
    def no_field(self):
        if self.field is None:
            raise ValueError('no information of column!')

    # поднимаем ошибку если нет
    def no_order(self):
        if self.order is None:
            raise ValueError('no information about ORDER BY!')

    # поднимаем ошибку если нет
    def no_limit(self):
        if self.lim is None:
            raise ValueError('no information about number of LIMIT!')

    # название команды для получения запроса
    def change_command(self, new_command):
        self.command = new_command

    # добавляем имя таблицы
    def add_table_name(self, table_name):
        self.t_name = table_name

    # добавляем имя колонки/колонок
    def select_fields(self, field):
        self.field = field
        self.change_command('SELECT')

    # добавляем условия
    def add_where(self, conditions):
        self.where = conditions
        self.change_command('WHERE')

    # добавляем порядок сортировки
    def add_order_by(self, order):
        self.order = order
        self.change_command('ORDER')

    # добавляем количество выбираемых из таблицы записей
    def add_limit(self, numder):
        self.lim = numder
        self.change_command('LIMIT')

    # указываем какое количество записей в таблице нужно пропустить
    def add_offset(self, offset):
        self.offset = offset
        self.change_command('OFFSET')

    # получаем созданный запрос
    def get_qwery(self):
        self.no_name()
        self.no_field()
        if self.command == 'SELECT':
            return f'SELECT {self.field} FROM {self.t_name};'
        if self.command == 'WHERE':
            return f'SELECT {self.field} FROM {self.t_name} WHERE {self.where};'
        if self.command == 'ORDER':
            return f'SELECT {self.field} FROM {self.t_name} ORDER BY {self.order};'
        if self.command == 'LIMIT':
            self.no_order()
            return f'SELECT {self.field} FROM {self.t_name} ORDER BY {self.order} LIMIT {self.lim};'
        if self.command == 'OFFSET':
            self.no_order()
            self.no_limit()
            return f'SELECT {self.field} FROM {self.t_name} ORDER BY {self.order} ' \
                f'LIMIT {self.lim} OFFSET {self.offset};'


sb = SelectBuilder()
sb.add_table_name('MyTable')
sb.select_fields('*')
print(sb.get_qwery())
sb.select_fields('column1, column2')
sb.add_where(f'MyTable.column3 = \'42\'')
print(sb.get_qwery())
sb.select_fields('column1')
sb.add_order_by('column2 ASC')
print(sb.get_qwery())
sb.select_fields('column2')
sb.add_order_by('column1 ASC, column3 DESC')
sb.add_limit('5')
print(sb.get_qwery())
sb.select_fields('column5')
sb.add_order_by('column5 DESC')
sb.add_limit('10')
sb.add_offset('100')
print(sb.get_qwery())

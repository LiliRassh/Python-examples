# Считываем значение величины, для которой нужно выполнить перевод единицы измерения
parametr_n = input('Введите величину обьема информации (например - 100 килобайт): ')

# Считываем название единицы измерения, в которую нужно перевести
while True:
    print('Выберите размерность единиц измерения из списка:')
    # Список размерностей единиц измерения информации
    name_unit = ['бит', 'байт', 'килобайт', 'мегабайт', 'гигабайт', 'терабайт',
                 'петабайт', 'эксабайт', 'зеттабайт', 'йотабайт']
    print(name_unit)
    name_m = input('Перевести в: ')
    # Проверяем есть ли название введеной единицы измерения в списке размерностей
    if name_m[0: name_m.rfind('т')+1] in name_unit:
        break
    else:
        print('Ошибка!!!')
        continue

# Только числовое значение введеной величины для перевода единиц измерения
n = float(parametr_n[0: parametr_n.find(' ')])
# Название единицы измерения введенной величины
name_n = parametr_n[parametr_n.find(' ')+1:]

# Находим индексы единиц измерения в списке name_unit,
# между которыми нужно выполнить перевод
for unit in name_unit:
    if unit == name_n:
        index_n = name_unit.index(unit)    # индекс данной единици измерения
    if unit == name_m[0: name_m.rfind('т')+1]:
        index_m = name_unit.index(unit)    # индекс искомой единици измерения

# Сравнивая индексы определяем, что нужно, повысить или понизить
# единицы измерения введеной величины.
# И, соответственно, что делать, делить или умножать, чтобы выполнить перевод величин.
# Перевод на понижение единицы измерения:
if index_n > index_m:
    if index_m == 0:
        if index_n > 1:
            m = n * 8 * (1024**(index_n-1))     # если из килобайт и далее в биты
        else:
            m = n * 8       # если из байтов в биты
    else:
        m = n * (1024**(index_n-index_m))  # например, из гигабайт в мегабайты
    print(parametr_n, '=', m, name_m[0: name_m.rfind('т') + 1])
# Перевод на повышение единицы измерения:
elif index_n < index_m:
    if index_n == 0:
        if index_m > 1:
            m = n / 8/(1024**(index_m-1))  # если из бит в килобайты и далее
        else:
            m = n / 8         # если из бит в байты
    else:
        m = n / (1024**(index_m-index_n))   # например, из мегабайт в гигабайты
    print(parametr_n, '=', m, name_m[0: name_m.rfind('т') + 1])
else:
    print('Ошибка! Ничего переводить не нужно!')



import random
import string

print('        1. Обмен значений численных переменных')

a = input('Первое число a = ')
b = input('Второе число b = ')
c = a
a = b
b = c
print('a =', a)
print('b =', b)
print()

print('        2. Форматированный вывод данных')

print('        2.1 Вывод данных в табличной форме (с выровненными столбцами)')

girls = {'Name': ['Year', 'Month', ' Day', 'Index', 'Class', 'Number'],
         'Lena': [1985, 2, 14, 5, 14, 10],
         'Katya': [1994, 6, 29, 11, 5, 25],
         'Olya': [1988, 3, 5, 7, 8, 10]}

print('        2.2 Первый столбец выравнивание слева')

for girl in girls:
    print('{:<10}'.format(girl), end=' ')
    for i in range(len(girls[girl])):
        # остальные стобцы выравнивание по центру
        print('{:^10}'.format(girls[girl][i]), end=' ')
    print()
print()

print('        2.3 Вывод вещественных чисел с заданным')
print('        количеством знаков после запятой.')

pi = 3.1415926535
print('pi =', pi, '\nВывести 2 знака после запятой')
print('pi =', float('{:.2f}'.format(pi)))
print()

print('        3. Вычисление площадей и периметров фигур')

print('        3.1 Площадь и периметр треугольника')
A = float(input('Ведите сторону A '))
B = float(input('Ведите сторону B '))
C = float(input('Ведите сторону C '))
p = (A + B + C) / 2
S_tri = (p*(p-A)*(p-B)*(p-C))**0.5
print('S треугольника =', ('{:.4f}'.format(S_tri)))
print('P треугольника =', 2*p)
print()

print('        3.2 Площадь и периметр прямоугольника')
W = float(input('Введите ширину W '))
h = float(input('Введите ширину h '))
print('S прямоугольника =', '{:.2f}'.format(W * h))
print('P прямоугольника =', 2*W + 2*h)
print()

print('        3.3 Площадь и периметр круга')
r = float(input('Ведите радиус круга r '))
print('S круга', '{:.2f}'.format(pi * r**2))
print('P круга', '{:.2f}'.format(2 * pi * r))
print()

print('        4. Сумма и произведение цифр числа')

num = int(input('Введите целое трехзначное число '))
num = str(num)
summ = 0
pr = 1
for i in range(len(num)):
    summ += int(num[i])
    pr *= int(num[i])
print('Сумма цифр = ', summ, 'Произведение цифр =', pr)
print()

print('        5. Битовые операции над числами 5 и 6')

# переведем числа 5 и 6 в двоичную систему
b_5 = '{0:b}'.format(5)
b_6 = '{0:b}'.format(6)
print('5 в двоичной системе -', b_5, '\n6 в двоичной системе -', b_6)

bit_or = 5 | 6
bit_and = 5 & 6
bit_OR = 5 ^ 6
bit_not = ~5
print('\n5 побитовое ИЛИ 6 дает', bit_or, '- {0:b}'.format(bit_or),
      '\n5 побитовое И 6 дает', bit_and, '- {0:b}'.format(bit_and),
      '\n5 ИСКЛЮЧИТЕЛЬНО ИЛИ 6 дает',  bit_OR, '- {0:b}'.format(bit_OR),
      '\nпобитовое НЕ 5 дает', bit_not, '- {0:b}\n'.format(bit_not))
# побитовый сдвиг числа 5 вправо на 2 знака
right_5 = 5 >> 2
# В двоичном виде цифра 5 представляется как 101,
# при сдвиге вправо на 2 бита получаем 1, в десятичном виде это цифра 1
print('Побитовый сдвиг числа 5 вправо на 2 знака дает число', right_5, '- {0:b}'.format(right_5))

# побитовый сдвиг числа 5 влево на 2 знака
left_5 = 5 << 2
# при сдвиге 5 влево на 2 бита получаем 10100, в десятичном виде это число 20
print('Побитовый сдвиг числа 5 влево на 2 знака дает число', left_5, '- {0:b}'.format(left_5))
print()

print('         6. Вывести уравнение прямой по координатам двух точек')

x1 = int(input('Введите координату x1 '))
x2 = int(input('Введите координату x2 '))
y1 = int(input('Введите координату y1 '))
y2 = int(input('Введите координату y2 '))
if x1 != x2:
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    if k == 0:
        print('Прямая паралельна оси x.\n Уравнение прямой имеет вид y =', b)
    else:
        print('Уравнение прямой имеет вид y =' + str(k)+'x'+'{:+}'.format(b))
else:
    print('Прямая паралельна оси y.\n Уравнение прямой имеет вид x =', x1)
print()

print('         7. Случайные числа и символы')

print('Укажите границы диапазона для целых чисел')
num_ran_int = random.randint(int(input('')), int(input('')))
print('Случайное целое число', num_ran_int)
print('Укажите границы диапазона для вещественных чисел')
num_ran_float = random.uniform(float(input('')), float(input('')))
print('Случайное вещественное число', '{:.2f}'.format(num_ran_float))
print('Укажите границы диапазона для символов')
simbols = string.ascii_lowercase
s1 = simbols.find(input())
s2 = simbols.find(input())
if s1 < s2:
    simbols = simbols[s1:s2+1]
else:
    simbols = simbols[s2:s1+1]
print(simbols)
simbol_ran = random.choice(simbols)
print('Случайный символ', simbol_ran)
print()

print('         8. Найти длину гипотенузы')

a1 = int(input('Введите первый катет '))
b1 = int(input('Введите второй катет '))
c1 = (a1**2 + b1**2)**0.5
print('Длина гипотенузы равна', '{:.2f}'.format(c1))
print()

print('         9.1 Количество символов между двумя буквами алфавита.')

# В качестве алфавита используем английские буквы в нижнем регистре
alfavit = string.ascii_lowercase
print('Алфавит латинских букв -', alfavit)
letter_1 = input('Введите первую букву ')
letter_2 = input('Введите вторую букву ')
# находим индексы введеных букв в алфавите
for i in range(len(alfavit)):
    if alfavit[i] == letter_1:
        index_1 = i + 1
    elif alfavit[i] == letter_2:
        index_2 = i + 1
# Выводим сколько между ними букв
if letter_1 != letter_2:
    print('Первая буква стоит на {} месте в алфавите, вторая на - {}'.format(index_1, index_2))
    if abs(index_1 - index_2) == 1:
        print('Между ними нет букв')
    elif abs(index_1 - index_2) in [2, 22]:
        print('Между ними {} буква'.format(abs(index_1 - index_2) - 1))
    elif abs(index_1 - index_2) in [3, 4, 5, 23, 24, 25]:
        print('Между ними {} буквы'.format(abs(index_1 - index_2) - 1))
    else:
        print('Между ними {} букв'.format(abs(index_1 - index_2) - 1))
elif letter_1 == letter_2:
    print('Буквы одинаковые, они стоят на ' + str(index_1) + ' месте в алфавите')
print()

print('         9.2 Определение буквы по ее номеру в алфавите')

nomer = int(input('Введите номер буквы, от 1 до 26:'))
for i in range(len(alfavit)):
    if nomer == i:
        print('Под номером', nomer, 'находится буква', alfavit[nomer - 1])
print()

print('         10. Рассчитать выплаты по кредиту')

n = int(input('Какая сумма кредита?'))
y = int(input('На сколько лет?'))
p = float(input('Под какой процент? (В долях единицы) '))
m = (n * p * (1 + p)**y) / (12 * ((1 + p)**y - 1))
s = (m * 12) * y
print('Месячные выплаты по кредиту составят ', m, '\nСуммарная выплата по кредиту ', s)
print()

print('         11. Буква или иной символ?')

n_kod = int(input('Введите целое число - код символа по таблице ASCII'))
if n_kod in range(65, 91, 1):
    print('Это буквенный символ в таблице ASCII')
elif n_kod in range(97, 123, 1):
    print('Это буквенный символ в таблице ASCII')
else:
    print('Это не буквеннй символ в таблице ASCII')
print()

print('         12. Поменять местами минимальный и максимальный элементы')

# Создадим список из 15 случайных чисел в диапазоне от -50 до 50
arr = [random.randint(-50, 51) for i in range(15)]
print('Начальный список', arr)
min_a = min(arr)
max_a = max(arr)
print('MIN =', min_a, 'MAX =', max_a)
index_min = arr.index(min_a)
index_max = arr.index(max_a)
arr[index_min] = max_a
arr[index_max] = min_a
print('Измененый список', arr)
print()

print('         13. Вычислить значения функции y=f(x) на заданном диапазоне')

range_x = [i for i in range(-10, 11, 1)]
print('Диапазон значений x = ', range_x)


def y_func_x(x):
    if (x >= -5) and (x <= 5):
        y = x**2
    elif x < -5:
        y = 2*abs(x) - 1
    elif x > 5:
        y = 2*x
    return y


range_y = [y_func_x(i) for i in range(-10, 11, 1)]
print('Значения функции y = ', range_y)
print()

print('         14. Определить студентов с баллом выше среднего')

kol = int(input('Введите количество студентов '))
print('Введите информацию о студентах:')
summa_ball = 0
ss = []
for i in range(kol):
    s = []
    s.append(input('Фамилия и имя {} студента '.format(i+1)))
    s.append(int(input('Балл {} студента '.format(i+1))))
    summa_ball += s[1]
    ss.append(s)
print('Полученный массив данных о студентах', ss, sep='\n')

middle_ball = summa_ball / kol
print('Средний балл = {:.2f}'.format(middle_ball))
print('Фамилия и имя студентов, чей балл выше среднего:')
for h in range(kol):
    if ss[h][1] > middle_ball:
        print(ss[h][0])




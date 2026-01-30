foo = 'Hello, world!'
bar = 'from branch feature-1'
bar += ' and from VSC as well'
bar += ' and from VSC again. Try push via ssh.'
bar += ' and from new PyCharm'

set_list = []
i = 0
while i < 3:
    set_list.append(i)
    i += 1

Anton = ['A', 'n', 't', 'o', 'n']

set_list.append(Anton)
set_list.extend(Anton)

### some counts in cycles
c = 1
i = 1

multiplier_set = (
    73,
    73037,
    7300037,
    730737037,
    730000737000037,
    730000000737000000037,
)

power = 5
multiplier = multiplier_set[-2]

while i < power**power**power:
    i *= multiplier
    c += 1

### test for workbook types in Python
a = type(int(float('123.5')))
b = type(int(524 ** 12)) #441345311145345))
c = type(int('342'))
d = type(int(float('-17.132')))

name = 'Anton Lysogor'
cell = +79261086838
address = 'Oleko Dundicha, 34, 55'

e = 11 * 2 ** 2 - 13 / 4 + 7
p = 2 ** 2
aa = 11 * p
bb = 13 / 4
cc = 7

n = None
string = '123.457'
boo = True
foo = False
fract = 1/3


def hello():
    inp_name = input("Введите ваше имя: ")
    out_hello = 'Приветствую вас, ' + inp_name + '!'
    return out_hello


def sq_hund_calc():
    length = int(input('Введите длину участка в метрах: '))
    withd = int(input('Введите ширину участка в метрах: '))
    sq = length * withd // 100
    return "Площадь участка: " + str(sq) + " соток."


def numbers_sum(): #get the 4 digit nubmer and return its sum
    numb = input('Введите четырёхзначное число: ')
    num_sum = 0
    for num in numb:
        num_sum += int(num)
    return f'Сумма цифр равна {num_sum}'


def sq_room_calc():
  l_room = float(input('Введите длину комнаты в метрах, дробную часть отделите точкой: '))
  w_room = float(input('Введите ширину комнаты в метрах, дробную часть отделите точкой: '))
  return f'Площадь комнаты {l_room * w_room} метров.'


def median_of_three(set_three):
    from statistics import median
    return median(set_three)


def delivery_calc(num_goods):
    delivery_cost  = (int(num_goods) - 1) * 30 + 100
    return delivery_cost


def how_many_secs():
    inp = input('Введите количество дней, часов, минут и секунд через пробел: ')
    inp_list = inp.split()
    print(inp_list)

    secs = 0
    counter = 0
    for every in inp_list:
        numb = int(every)
        if counter == 0: #days
            secs += numb * 60 * 60 * 24
        if counter == 1: #hours
            secs += numb * 60 * 60
        if counter == 2: #hminutes
            secs += numb * 60
        if counter == 3: #seconds
            secs += numb
        counter += 1
    return secs


def check_if_anagram():
    words = input('Введите два слова через пробел: ')
    w_list = words.split()
    w1 = w_list[0]
    w2 = w_list[1]
    w1 = w1.lower()
    w2 = w2.lower()
    w2_reverse = w2[::-1]
    return w1 == w2_reverse

month_days_dict = {
        'january' : 31,
        'январь' : 31,
        'march': 31,
        'март' : 31,
        'may' : 31,
        'май' : 31,
        'july' : 31,
        'июль' : 31,
        'august' : 31,
        'август' : 31,
        'october' : 31,
        'октябрь' : 31,
        'december' : 31,
        'декабрь' : 31,
        'april' : 30,
        'апрель' : 30,
        'june' : 30,
        'июнь' : 30,
        'september' : 30,
        'сентябрь' : 30,
        'november' : 30,
        'ноябрь' : 30,
        'february' : '28/29',
        'февраль' : '28/29'
    }

def count_days_in_month():
    month_days = month_days_dict

    month_name = input('Введите название месяца: ')
    month_name = month_name.lower()

    return month_days.get(month_name)


def price_calc():
    input_str = input('Введите возраст каждого посетителя через запятую: ')
    input_list = input_str.split(',')
    cost = 0
    for every in input_list:
        age = int(every)
        if age < 2 or age > 65:
            cost += 0
        elif 2 < age < 12:
            cost += 200
        else:
            cost += 500

    return cost


def days_in_month_with_leap_year():
    days_31_set = {1, 3, 5, 7, 8, 10, 12}
    days_30_set = {4, 6, 9, 11}

    input_str = input('Введите номер месяца и номер года через точку (ММ.ГГГГ): ')
    input_list = input_str.split('.')
    month_n = int(input_list[0])
    year_n = int(input_list[1])

    if month_n in days_31_set:
        return 31
    elif month_n in days_30_set:
        return 30
    elif month_n == 2:
        if year_n % 400 == 0:
            return 29
        elif year_n % 100 == 0:
            return 28
        elif year_n % 4 == 0:
            return 29
        else:
            return 28
    else:
        return False


def cycle_xy_task():
    x = 10
    y = 0
    while x > 5:
        y = y + 2 * y - 3
        x += -1
    if x == y:
        x = x - y
        y = y + x
    else:
        x = x + y
        y = y - x
    return y


def crypta_july_cesar():
    letters_small = list('qwertyuioplkjhgfdsazxcvbnm')
    letters_small.sort()
    letters_small += 'abc'
    letters_big = list('QWERTYUIOPLKJHGFDSAZXCVBNM')
    letters_big.sort()
    letters_big += 'ABC'
    letters = letters_big + letters_small

    original = list(input('Input statement to be crypted: '))
    crypta = ''
    for every in original:
        if every.isalpha():
            crypted = letters[letters.index(every) + 3]
        else:
            crypted = every
        crypta += crypted

    print(''.join(original))
    print(crypta)


def my_list():
    mine_list = [2, 4, 8]
    print(mine_list)
    print(mine_list[::-1])
    print(mine_list)
    print(mine_list.reverse())
    print(mine_list)
    # второе задание
    a_list = [1, 1, 2, 3, 5, 8, 34, 55, 89]
    a_list.sort()
    for elem in a_list:
        if int(elem) < 5:
            print(elem)


def is_integer():
    number = int(input('Введите целое число: '))
    if number % 2 == 0:
        print('Это число чётное.')
    else:
        print('Это число нечётное.')


def a_b_c():
    inp_str = input('Введите значения A, B, C через запятую: ')
    inp_val = inp_str.split(',')
    val_a = int(inp_val[0])
    val_b = int(inp_val[1])
    val_c = int(inp_val[2])
    if val_a == val_b:
        val_c = val_a + val_b
        val_e = val_b + val_c
    elif val_b < val_c:
        val_a += val_b
        val_e = val_a + val_c
    else:
        val_b += val_c
        val_e = val_a + val_b
    return val_e


def multiplication_table():
    # печатаем заголовок
    print(" ".ljust(3), end=" ")
    for col in range(1, 11):
        if col == 10:
            print(str(col).ljust(3))
        else:
            print(str(col).ljust(3), end=" ")
    for row in range(1, 11):
        print(str(row).ljust(3), end =" ")
        for col in range(1, 11):
            if col == 10:
                print(str(col * row).ljust(3))
            else:
                print(str(col * row).ljust(3), end=" ")

def m_table_workbook():
    # Вот пример кода, который выводит таблицу умножения:
    # Этот код создает двумерный список таблицы умножения.
    a0 = [' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    at = [a0, a1]
    for it in range(2, 11):
        ai = []
        for j in a1:
            j = j * it
            ai.append(j)
        at.append(ai)
    # Этот код выводит таблицу умножения на экран.
    for row in at:
        for elem in row:
            print(elem, end=' ')
        print()


def lottery_numbers():
    import random
    lot_numbs = random.sample(range(1, 49), 6)
    lot_numbs.sort()
    print(lot_numbs)


def input_integers():
    z = 1
    z_list = []
    while z != 0:
        z = int(input('Введите целое число или 0 для завершения: '))
        z_list.append(z)
    z_list.sort()
    for each_z in z_list:
        if int(each_z) == 0: continue
        print(each_z)


def sum_of_inputs():
    """
    рекурсивная функция вызывает сама себя и хранит результат в памяти,
    пока не дойдёт до условия выхода
    """
    z = input('Введите число или "пустую строку" для завершения: ')
    if z == '':
        return 0
    else:
        return float(z) + sum_of_inputs()


def flatten_nested_list(arr):
    result = []
    for el in arr:
        if type(el) == list:
            result.extend(flatten_nested_list(el))
        else:
            result.append(el)
    return result

long_list = [[[1, 2, 3], [23, [13, 11], 4], [12, 16], 5], 7, [111,117]]


def what_time_is_now():
    import time
    print(time.asctime())


def longest_word(f_name):
    file = open(f_name, 'r')
    text = file.read()
    file.close()
    cont = text.split(' ')
    cont.sort(key=len)
    cont.reverse()
    ico = 0
    while len(cont[0]) == len(cont[ico]):
        print(cont[ico])
        ico += 1
    print(len(cont[0]), ico)


def file_lines_numbering(f_inp, f_out='test.txt'):
    with open(f_inp, 'r') as f_inp:
        data = f_inp.readlines()
    with open(f_out, 'w') as f_out:
        il = 1
        for each_l in data:
            f_out.write(str(il) + ': ' + each_l)
            il += 1


def read_the_files(files):
    if not files : return print('Передайте список файлов!')
    for each_f in files:
        try:
            with open(each_f, 'r') as file_r:
                print(file_r)
                for line in file_r:
                    print(line, end="")
        except FileNotFoundError:
            print('Файл "', each_f, '" не открывается.')


def delete_comments(orig, cut):
    try:
        with open(orig, 'r') as orig:
            orig_list = orig.readlines()
            stripped_list = []
            for orig_line in orig_list:
                # split - находит #, [0] - возвращает первый символ
                orig_split = orig_line.split('#')[0] # .strip() - убивает всё форматирование
                stripped_list.append(orig_split)
        with open(cut, 'w') as cut_w:
            for ev_line in stripped_list:
                cut_w.write(ev_line)
    except FileNotFoundError:
        print('Cannot open the file.')

def new_element():
    line = [0]
    for el in line:
        line.append(i+1)
        print(line)
        if el == 10: break

def zip_lists():
    names = ['Anton', 'Nastya', 'Yegor']
    ages = [45, 40, 15]
    for name_i, age_i in zip(names, ages):
        print(name_i, age_i)

def flatten_tuple(tup):
    return tuple([el for subarray in tup for el in subarray])

def flatten_tuple_keys(tup):
    return [subarray[0] for subarray in tup for _ in subarray]

def sum_positive_numbers(numbers):
    return sum([el for el in numbers if el > 0])

def process_array(numbers):
    return [el * 2 for el in numbers if el > 0]

numbers_tup = (
    (1,),
    (2, 4, 8, 16),
    (3, 6, 9, 12, 18),
    (5, 10, 15, 20),
    (7, 14, 21),
    (11, 22),
    (13,),
    (17,),
    (19,),
    (23,),
    )
numbers_flat = flatten_tuple(numbers_tup)

def list_to_dict(keys, values):
    return {key_i: value_i for key_i, value_i in zip(keys, values)}

keys23 = list(numbers_flat)
values23 = flatten_tuple_keys(numbers_tup)
dict23 = list_to_dict(keys23, values23)


def sum_n_dimensional_vectors(vectors_list):
    result = [0 for _ in vectors_list[0]]
    for vector in vectors_list:
        for count, value in enumerate(vector):
            result[count] += value
    return tuple(result)

v_list = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
]

def lim_max_w_loop(nums, limit):
    max_value = -1
    for num in nums:
        if num >= limit: continue
        max_value = max(num, max_value)
    return max_value

def lim_max(nums, limit):
    return max([num for num in nums if num < limit])


import math

def calculate_probability(k, p, n):
    """
    Рассчитывает вероятность успешного подбора от 0 до k включительно.
    """
    probability_sum = 0
    for i in range(k + 1):
        probability_sum += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return probability_sum

def find_max_length_password(target_probability, p, max_attempts):
    """
    Находит максимально возможную длину пароля, чтобы гарантированно успеть открыть сейф.
    """
    k = 1  # Начинаем с длины пароля 1
    probability_sum = calculate_probability(k, p, max_attempts)

    while probability_sum < target_probability:
        k += 1
        probability_sum = calculate_probability(k, p, max_attempts)

    return k

def print_max_len():
    # Условия задачи
    target_probability = 0.5  # Гарантированная вероятность успеха
    p = 0.7  # Вероятность успешного подбора символа
    max_attempts = 1800  # Максимальное время в секундах (30 минут)

    # Находим максимально возможную длину пароля
    max_length = find_max_length_password(target_probability, p, max_attempts)

    # Вывод результата
    print(f"Максимально возможная длина пароля: {max_length}")


def students_correlation():
    import numpy as np
    from scipy.stats import pearsonr

    # Данные
    potions_making = np.array([85, 78, 90, 88, 82, 95])
    programming = np.array([90, 82, 92, 86, 80, 94])
    time_to_read = np.array([10, 8, 12, 11, 9, 13])

    # Коэффициент корреляции Пирсона и p-значение
    correlation, p_value = pearsonr(potions_making, programming)
    print(f"Коэффициент корреляции Пирсона: {correlation}")
    print(f"P-значение: {p_value}")

    # Коэффициент корреляции Пирсона и p-значение для времени на чтение
    correlation_time, p_value_время = pearsonr(potions_making, time_to_read)
    print(f"Коэффициент корреляции Пирсона для времени на чтение: {correlation_time}")
    print(f"P-значение для времени на чтение: {p_value_время}")


def min_stairs():
    ...

def small_t_ferma():
    import math
    slice('1 2 3')


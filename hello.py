foo = 'Hello, world!'
bar = 'from branch feature-1'
bar += ' and from VSC as well'
bar += ' and from VSC again. Try push via ssh.'
bar += ' and from new PyCharm'
print(foo, bar)

set_list = []
i = 0
while i < 3:
    set_list.append(i)
    i += 1

Anton = ['A', 'n', 't', 'o', 'n']

set_list.append(Anton)
set_list.extend(Anton)
print(set_list)

### some counts in cycles
c = 1
i = 1
print(i)

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
print(multiplier)

while i < power**power**power:
    i *= multiplier
    c += 1
print(type(i), c)

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
print(n , type(n), type(int(float(string))), type(int(boo)), type(int(foo)), type(int(fract)))

def hello():
    name = input("Введите ваше имя: ")
    hello = 'Приветствую вас, ' + name + '!'
    return(hello)

def sq_hund_calc():
    a = int(input('Введите длину участка в метрах: '))
    b = int(input('Введите ширину участка в метрах: '))
    sq = a * b // 100
    return("Площадь участка: " + str(sq) + " соток.")

def numbers_sum(): #get the 4 digit nubmer and return its sum
    numb = input('Введите четырёхзначное число: ')
    sum = 0
    for i in numb:
        sum += int(i)
    return(f'Сумма цифр равна {sum}')

def sq_room_calc():
  l_room = float(input('Введите длину комнаты в метрах, дробную часть отделите точкой: '))
  w_room = float(input('Введите ширину комнаты в метрах, дробную часть отделите точкой: '))
  return(f'Площадь комнаты {l_room * w_room} метров.')

def median_of_three(set_three):
    from statistics import median
    return(median(set_three))

def delivery_calc(num_goods):
    delivery_cost  = (int(num_goods) - 1) * 30 + 100
    return(delivery_cost)

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

def count_days_in_month():

    month_days = {
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

    month_name = input('Введите название месяца: ')
    month_name = month_name.lower()

    return(month_days.get(month_name))


def price_calc():
    input_str = input('Введите возраст каждого посетителя через запятую: ')
    input_list = input_str.split(',')
    cost = 0
    for every in input_list:
        age = int(every)
        if age < 2 or age > 65:
            cost += 0
        elif age > 2 and age < 12:
            cost += 200
        else:
            cost += 500

    return(cost)


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


def crypta_July_Cesar():
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
    my_list = [2, 4, 8]
    print(my_list)
    print(my_list[::-1])
    print(my_list)
    print(my_list.reverse())
    print(my_list)

    # второе задание
    a = [1, 1, 2, 3, 5, 8, 34, 55, 89]
    a.sort()
    for i in a:
        if int(i) < 5:
            print(i)

def is_integer():
    number = int(input('Введите целое число: '))
    if number % 2 == 0:
        print('Это число чётное.')
    else:
        print('Это число нечётное.')

def a_b_c()
    inp_val = input('Введите значения A, B, C через запятую: ')
    in
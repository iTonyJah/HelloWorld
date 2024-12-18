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

### test for wrokbook types in Python
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
    inp_set = inp.split()
    inp_set.sort(reverse=True)

    for i in inp_set:
        print(int(i), inp_set.index(i))


how_many_secs()

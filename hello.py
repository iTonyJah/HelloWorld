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
print(set_list)

for i in set_list:
    print(i, type(i), set_list[i])
print(set_list)

Anton = ['A', 'n', 't', 'o', 'n']
print(Anton)
set_list.append(Anton)
set_list.extend(Anton)
print(set_list)
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

a = type(int(float('123.5')))
b = type(int(524 ** 12)) #441345311145345))
c = type(int('342'))
d = type(int(float('-17.132')))
print(a, b, c, d)

name = 'Anton Lysogor'
cell = +79261086838
address = 'Oleko Dundicha, 34, 55'
print(name, cell, address)

e = 11 * 2 ** 2 - 13 / 4 + 7
p = 2 ** 2
aa = 11 * p
bb = 13 / 4
cc = 7
print(aa, bb, cc, aa - bb + cc)
print(e)

n = None
str = '123.457'
boo = True
foo = False
fract = 1/3
print(n , type(n), type(int(float(str))), type(int(boo)), type(int(foo)), type(int(fract)))

def hello():
    name = input("Введите ваше имя: ")
    hello = 'Приветствую вас, ' + name + '!'
    return(hello)

print(hello())


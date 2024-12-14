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
multiplier = multiplier_set[-3]
print(multiplier)

while i < power**power**power:
    i *= multiplier
    c += 1
print(type(i), c)

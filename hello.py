foo = 'Hello, world!'
bar = 'from branch feature-1'
bar += ' and from VSC as well'
bar += ' and from VSC again. Try push via ssh.'
bar += ' and from new PyCharm'
print(foo, bar)

set = []
i = 0
while i < 10:
    set.append(i)
    i += 1
print(set)

for i in set:
    print(i, type(i), set[i])
print(set)
numbers_set = {1}
# numbers_list = [prime_lines[prime_line_dimensions[values]]]
numbers_list = []
max_number = int(1 * 10 ** 2)


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    new_prime_line_dimension = [new_prime]
    new_prime_line = [new_prime_line_dimension]
    numbers_list.append(new_prime_line)
    dim = 1
    

for n in range(1, max_number + 1):
    if n not in numbers_set:
        add_new_prime(n)

numbers_list = tuple(numbers_list)
print(numbers_list)
print('n', len(numbers_set), 'p', len(numbers_list))

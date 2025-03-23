numbers_set = {1}
# numbers_list = [prime_lines[prime_line_dimensions[values]]]
numbers_list = []
max_number = int(1 * 10 ** 4)


def fill_prime_line(prime, prime_line, n_set, n_list):
    dim = 0
    while dim < len(prime_line):
        new = True
        stop = False
        for p_line in numbers_list:
            if dim >= len(p_line): break
            #if stop: break

            for value in p_line[dim]:
                product = value * prime
                if product > max_number: continue
                    # stop = True
                    # break
                numbers_set.add(product)
                if new:
                    # prime_line[dim].sort() #!!!
                    #print('sort', prime_line[dim])
                    prime_line.append([])
                    new = False
                prime_line[dim + 1].append(product)
        dim += 1


def add_new_prime(new_prime):
    numbers_set.add(new_prime)
    new_prime_line_dimension = [new_prime]
    new_prime_line = [new_prime_line_dimension]
    numbers_list.append(new_prime_line)

    fill_prime_line(new_prime, new_prime_line, numbers_set, numbers_list)


for n in range(1, max_number + 1):
    if n not in numbers_set:
        add_new_prime(n)

numbers_list = tuple(numbers_list)
for nl in numbers_list:
    print(nl)
    # for dm in nl:
    #     print(dm)
print('n', len(numbers_set), 'p', len(numbers_list))

import itertools
import re
from task_condition import print_task_condition


def read_pol(filename):
    with open(str(filename), 'r') as data:
        polynomial = data.read()
    data.close()
    return polynomial


def convert_pol(pol):
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol


def fold_pols(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key=lambda r: r[1], reverse=True)
    return res


def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)]
               for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        if x != new_pol[-1]:
            x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    return "".join(map(str, new_pol))


def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)
    data.close()


def print_result(pol_01, pol_02, pol_sum):
    print('1. ', pol_01)
    print('2. ', pol_02)
    print('3. Результат: ', pol_sum)


print_task_condition('task_04')
file_01 = 'polynomial_01.txt'
file_02 = 'polynomial_02.txt'
file_sum = 'sum_polynomials.txt'

pol_01 = read_pol(file_01)
pol_02 = read_pol(file_02)
conv_pol_1 = convert_pol(read_pol(file_01))
conv_pol_2 = convert_pol(read_pol(file_02))
pol_sum = get_sum_pol(fold_pols(conv_pol_1, conv_pol_2))
write_to_file(file_sum, pol_sum)
print_result(pol_01, pol_02, pol_sum)

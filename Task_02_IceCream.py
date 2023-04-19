from task_condition import print_task_condition


def get_text_from_file(filename):
    data = open(filename, encoding='utf-8')
    text = data.readlines()
    data.close()
    return text


def get_assortment_set(text, set_num):
    product_set = set(text[set_num].split(','))
    return product_set


def print_result(assortment_set, store_set, missing_set):
    print(f"\nАссортимент мороженного: ", end='')
    print(*assortment_set)
    print(f"\nНа складе имеется мороженное: ", end='')
    print(*store_set)
    print(f"\nЗакончилось мороженное: ", end='')
    print(*missing_set)


print_task_condition('task_02')
text = get_text_from_file('assortment.txt')
line_01 = 0
line_02 = 1
assortment_set = get_assortment_set(text, line_01)
store_set = get_assortment_set(text, line_02)
missing_set = assortment_set.difference(store_set)
print_result(assortment_set, store_set, missing_set)

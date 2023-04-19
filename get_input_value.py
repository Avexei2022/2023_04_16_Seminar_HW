def get_integer(message, mes_false) -> int:
    flag = True
    while flag:
        try:
            number = int(input())
            flag = False
        except:
            print(
                f"{mes_false}\n{message}", end=' ')
    return number


def get_number(message, num_min, num_max, mes_false) -> int:
    flag = True
    while flag:
        print(f"{message} ", end='')
        number = get_integer(message, mes_false)
        if number >= num_min and number <= num_max:
            flag = False
        else:
            print(mes_false)
    return number

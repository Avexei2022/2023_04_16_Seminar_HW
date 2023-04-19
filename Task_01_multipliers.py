from task_condition import print_task_condition
from get_input_value import get_number


def get_multipliers_list(number):
    multipliers = []
    i = 2
    while number > 1:
        if number % i == 0:
            multipliers.append(i)
            number /= i
        else:
            i += 1
    return multipliers


def print_multipliers_list(number, multipliers) -> None:
    print(f"{number} ->", end=" ")
    print(*multipliers)
    print(f"Количество множителей: {len(multipliers)}\n")


print_task_condition('task_01')
num_min, num_max = 1, 10000
message = f"Введите натуральное число N (от {num_min} до {num_max}):"
mes_false = "Условия ввода не выполнены."
number = get_number(message, num_min, num_max, mes_false)
multipliers = get_multipliers_list(number)
print_multipliers_list(number, multipliers)

# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа,
# поки воно не стане менше або дорівнювати 9.
#
# Користувач вводить число з клавіатури.
#
# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри, і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126,
# потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1
from functools import reduce


def multiply_digits(user_number):
    while user_number > 9:
        user_number = reduce(lambda first_digit, second_digit: first_digit * second_digit, map(int, str(user_number)))
    return user_number


while True:
    try:
        input_number = int(input("Enter the positive number: "))
        if input_number.is_integer() and input_number > 0:
            result = multiply_digits(input_number)
            print(result)
            break
        else:
            print("Invalid number entered. The number must be positive.")
    except ValueError:
        print("Error: The entered number is not a number. Please enter a correct number.")

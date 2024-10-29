def get_multiplied_digits(number):
    str_number = str(number)

    first = int(str_number[0])

    #продолжаем рекурсию при длине строки > 1
    if len(str_number) > 1:
        # Возвращаем произведение первой цифры и делаем рекурсию
        return first * get_multiplied_digits(int(str_number[1:]))

    return first

result = get_multiplied_digits(40203)
print(result)
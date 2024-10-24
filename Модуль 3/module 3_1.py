calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return any(string_lower in item.lower() for item in list_to_search)

# Примеры вызовов
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

#количество вызовов
print(calls)
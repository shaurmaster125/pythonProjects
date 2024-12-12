def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# ещё тесты
print(add_everything_up(10, 20))           # 30
print(add_everything_up('hello ', 'world')) # hello world
print(add_everything_up(10.5, 20.7))       # 31.2
print(add_everything_up(100, 'days'))      # 100days
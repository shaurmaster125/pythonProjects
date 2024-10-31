def calculate_structure_sum(*elements):
    total = 0

    # обработка типа элемента
    def process_element(element):
        if isinstance(element, (int, float)):
            return element
        if isinstance(element, str):
            return len(element)
        if isinstance(element, dict):
            return calculate_structure_sum(*element.keys(), *element.values())
        if isinstance(element, (list, tuple, set)):
            return calculate_structure_sum(*element)
        return 0

    # проходим по каждому элементу
    for arg in elements:
        total += process_element(arg)

    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
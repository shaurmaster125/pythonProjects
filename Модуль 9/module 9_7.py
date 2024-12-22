def all_variants(text):
    n = len(text)

    for length in range(1, n + 1):
        for start in range(n - length + 1):
            end = start + length
            yield text[start:end]


def main():
    # Создаем генератор
    a = all_variants("abc")

    for variant in a:
        print(variant)


    print("\nДругой пример:")
    for variant in all_variants("1234"):
        print(variant)


if __name__ == "__main__":
    main()
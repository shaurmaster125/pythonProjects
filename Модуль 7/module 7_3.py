class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()

                # Удаляем знаки пунктуации
                for punct in punctuation:
                    text = text.replace(punct, ' ')

                # Получаем список слов
                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        result = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1

        return result

    def count(self, word):
        result = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)

        return result


# Пример использования:
if __name__ == "__main__":
    # Создаем объект
    finder = WordsFinder('test_file.txt')

    # Тестируем методы
    print("Все слова:")
    print(finder.get_all_words())

    print("\nПоиск слова 'text':")
    print(finder.find('TEXT'))

    print("\nПодсчет слова 'text':")
    print(finder.count('teXT'))

    #дополнительная проверка
    print("\nОтдельная строка")
    print("------------------------\n")
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

    print("Все слова:")
    print(finder1.get_all_words())

    print("\nПоиск слова 'text':")
    print(finder1.find('captain'))

    print("\nПодсчет слова 'text':")
    print(finder1.count('cApTaiN'))

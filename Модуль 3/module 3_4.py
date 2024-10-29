def single_root_words(root_word, *other_words):
    same_words = []

    #для нечувствительности к регистру
    root_word_lower = root_word.lower()

    for word in other_words:
        #тоже для нечувствительности к регистру
        word_lower = word.lower()

        # Проверка на содержание слова
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words


#Примеры
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

#Вывод
print(result1)
print(result2)
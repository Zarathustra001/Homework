def single_root_words(root_word, *other_words):
    """
    Функция single_root_words принимает одно обязательное слово в параметр root_word,
    а далее неограниченную последовательность в параметр *other_words.

    Функция должна составить новый список same_words только из тех слов списка other_words,
    которые содержат root_word или наоборот root_word содержит одно из этих слов.

    После вернуть список same_words в качестве результата своей работы.
    """

    same_words = []

    for word in other_words:
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)

    return same_words


root_word1 = input("Введите первое главное слово: ")
end = int(input("Введите количество слов для сравнения: "))
other_words1 = []

for i in range(0, end):
    word = input("Введите слово для сравнения с первым главным словом: ")
    other_words1.append(word)

root_word2 = input("Введите второе главное слово: ")
other_words2 = []
for i in range(0, end):
    word = input("Введите слово для сравнения со вторым главным словом: ")
    other_words2.append(word)

result1 = single_root_words(root_word1, *other_words1)
result2 = single_root_words(root_word2, *other_words2)

print("Однокоренные для первого слова:", result1)
print("Однокоренные для вторго слова:", result2)
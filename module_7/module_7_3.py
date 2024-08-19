import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем переданные названия файлов
        self.file_names = list(file_names)

    def get_all_words(self):
        # Словарь для хранения слов по файлам
        all_words = {}
        # Перебор всех переданных файлов
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Чтение всего текста, перевод в нижний регистр
                text = file.read().lower()

                # Замена пунктуации на пробелы
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, ' ')

                # Разбиение текста на слова
                words = text.split()

                # Сохранение списка слов в словарь
                all_words[file_name] = words

        return all_words

    def find(self, word):
        # Приводим искомое слово к нижнему регистру
        word = word.lower()
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}

        # Перебор всех файлов и слов для поиска первого вхождения
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # +1 для корректного счёта позиции

        return result

    def count(self, word):
        # Приводим искомое слово к нижнему регистру
        word = word.lower()
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}

        # Перебор всех файлов и слов для подсчета вхождений
        for name, words in all_words.items():
            result[name] = words.count(word)

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print('***')

finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
print('***')

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
print('***')

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

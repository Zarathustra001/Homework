import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
suite = unittest.TestSuite()

# Добавляем тесты из RunnerTest и TournamentTest
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
result = runner.run(suite)

# Выводим результаты
print(result)
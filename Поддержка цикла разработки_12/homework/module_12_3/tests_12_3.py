import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("John")

    def test_run(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    def test_walk(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    def test_challenge(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        runner2 = Runner("Jane")
        self.runner.run()
        runner2.walk()
        self.assertNotEqual(self.runner.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner("Alice")
        self.runner2 = Runner("Bob")
        self.runner3 = Runner("Charlie")

    def test_first_tournament(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(20, self.runner1, self.runner2, self.runner3)
        finishers = tournament.start()
        self.assertEqual(finishers[1].name, "Alice")

    def test_second_tournament(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(30, self.runner1, self.runner2, self.runner3)
        finishers = tournament.start()
        self.assertEqual(finishers[1].name, "Bob")

    def test_third_tournament(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(40, self.runner1, self.runner2, self.runner3)
        finishers = tournament.start()
        self.assertEqual(finishers[1].name, "Charlie")
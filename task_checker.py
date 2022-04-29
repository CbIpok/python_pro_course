import random
from math import factorial
import time


class TaskChecker:
    def __init__(self, task):
        self.task = task
        self.data_cards = []
        self.data_most_freq = []

    # pregen func
    def fibb_cycle(self, n):
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a

    def data_cards_gen(self):
        a = []
        n = random.randint(1, 100000)
        if n == 1:
            return n, a, 1
        else:
            random_out = random.randint(0, n - 1)
            for i in range(n):
                if i == random_out:
                    continue
                a.append(i)
            return n, a, random_out + 1

    def data_cards_fill(self):
        steps = 1000
        for i in range(steps):
            self.data_cards.append(self.data_cards_gen())
            print(f"card generation {i}/1000")
        print("done")

    def most_freq_check(self, n, cartage):
        counter = {}
        for i in range(n):
            for word in cartage[i].split():
                counter[word] = counter.get(word, 0) + 1

        max_count = max(counter.values())
        most_frequent = [k for k, v in counter.items() if v == max_count]
        return min(most_frequent)

    def lines_gen(self):
        for i in range(200):
            self.data_most_freq.append([])
            line = ''
            for j in range(1, random.randint(50000, 70000)):
                line = line + str(random.randint(10, 20))
            self.data_most_freq[i] = line
            print(f"lines generation {i}/200")
        print("done")

    # check func
    def task_check(self):
        if self.task.name == "sum":
            for i in range(-100, 100):
                for j in range(-50, 50):
                    if self.task.run(i, j) != i + j:
                        return False
            return True
        if self.task.name == "card":
            for case in self.data_cards:
                if self.task.run(case[0], case[1]) != case[2]:
                    return False
            return True
        if self.task.name == "fact_sum":
            if self.task.run(1000) != sum([factorial(x) for x in range(1, 1000 + 1)]):
                return False
            if self.task.run(1) != sum([factorial(x) for x in range(1, 1 + 1)]):
                return False
            if self.task.run(5) != sum([factorial(x) for x in range(1, 5 + 1)]):
                return False
            return True
        if self.task.name == "fibb":
            if self.task.run(10) != self.fibb_cycle(10):
                return False
            if self.task.run(1) != self.fibb_cycle(1):
                return False
            if self.task.run(100) != self.fibb_cycle(100):
                return False
            if self.task.run(5) != self.fibb_cycle(5):
                return False
            if self.task.run(2) != self.fibb_cycle(2):
                return False
            return True

    # call func
    def run(self):
        if self.task.name == "card":
            self.data_cards_fill()
        if self.task_check():
            print("Passed")
        else:
            print("Failed")

    def benchmark(self):
        # data pregen
        if self.task.name == "card":
            self.data_cards_fill()
        if self.task.name == "most_freq":
            self.lines_gen()
        start = time.time()
        # core
        if self.task.name == "sum":
            for i in range(-1000, 1000):
                for j in range(-50000, 50000):
                    if self.task.run(i, j) != i + j:
                        break
                print(f"bench {i + 1000}/2000")
        if self.task.name == "card":
            for i in range(100):
                for case in self.data_cards:
                    self.task.run(case[0], case[1])
                print(f"bench {i}/100")
        if self.task.name == "fact_sum":
            for i in range(100):
                self.task.run(3000)
                print(f"bench {i}/100")
        if self.task.name == "fibb":
            for i in range(100):
                self.task.run(200000)
                print(f"bench {i}/100")
        if self.task.name == "most_freq":
            for i in range(1000):
                self.task.run(len(self.data_most_freq), self.data_most_freq)
                print(f"bench {i}/1000")
        if self.task.name == "most_freq":
            pass
        if self.task.name == "most_freq":
            pass
        return time.time() - start

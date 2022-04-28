import random
import time
card_params = [[2, [2], 1], [4, [1, 3, 4], 2], [3, [3, 1], 2], [1, [], 1], [10, [1, 2, 3, 4, 5, 6, 8, 9, 10], 7]]


class TaskChecker:
    def __init__(self, task):
        self.task = task
        self.data_cards = []


    def data_cards_gen(self):
        a = []
        N = random.randint(1, 100000)
        if N == 1:
            return N, a, 1
        else:
            random_out = random.randint(0, N-1)
            for i in range(N):
                if i == random_out:
                    continue
                a.append(i)
            return N, a, random_out + 1

    def data_cards_fill(self):
        steps = 1000
        for i in range(steps):
            self.data_cards.append(self.data_cards_gen())
            print(f"card generation {i}/1000")
        print("done")

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

    def run(self):
        if self.task_check():
            print("Passed")
        else:
            print("Failed")

    def benchmark(self):
        start = time.time()
        for i in range(100):
            for case in self.data_cards:
                self.task.run(case[0], case[1])
            print(f"bench {i}/100")
        return time.time() - start



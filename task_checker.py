import random
from math import factorial
import time
from collections import Counter
from collections import defaultdict

class TaskChecker:
    def __init__(self, task):
        self.task = task
        self.data_cards = []
        self.data_most_freq = []
        self.data_sales = []
        self.data_freq_check = []
    # pregen func

    def data_gen_sales(self):
        strings = []
        for i in range(1000000):
            strings.append(str(random.randint(1, 10)) + " " + str(random.randint(1, 10)) + " " + str(random.randint(1, 100000)))
        self.data_sales = strings

    def check_sales(self, data):
        clients = defaultdict(lambda: defaultdict(int))
        for line in data:
            client, thing, value = line.split()
            clients[client][thing] += int(value)
        ans = []
        for client in sorted(clients):
            ans.append(str(client + ':'))
            for thing in sorted(clients[client]):
                ans.append(str(thing) + " " + str(clients[client][thing]))
        return ans

    def data_gen_freq_check(self):
        output = []
        for i in range(10000):
            output.append("ai ai ai ai ai ai ai ai ai oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd asd qwe sdf adsd zxc qwedf ai ai ai ai ai ai ai ai ai oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd asd qwe sdf adsd zxc qwedf ai ai ai ai ai ai ai ai ai oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd asd qwe sdf adsd zxc qwedf ai ai ai ai ai ai ai ai ai oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd asd qwe sdf adsd zxc qwedf ai ai ai ai ai ai ai ai ai oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd asd qwe sdf adsd zxc qwedf ai ai ai ai ai ai ai ai ai oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd asd qwe sdf adsd zxc qwedf dfgqwe asdfsdfg asd qwe rsdf aasd sf dfasdkqwoe asasdasd aiaiai ai ai ai oi oi oi oi oi oi oi oi oi oi oi ai ai ai ai ai ai ai ai ai oi oi oi oi das asd ai ai ai oi oi oi oi oi oi oi oi oi oi oi ")
        self.data_freq_check = output

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

    def freq_check_ans(self, n, data):
        words = []
        result = []
        for _ in range(n):
            words.extend(data[_].split())
        counter = Counter(words)
        pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
        words = [pair[1] for pair in sorted(pairs)]
        return words

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

    # check func
    def task_check(self):
        if self.task.name == "sum":
            for i in range(-100, 100):
                for j in range(-50, 50):
                    if self.task.run(i, j) != i + j:
                        return False
            return True
        if self.task.name == "card":
            if self.task.run(5, [1, 2, 3, 4]) != 5:
                return False
            if self.task.run(5, [3, 5, 2, 1]) != 4:
                return False
            if self.task.run(1, []) != 1:
                return False
            if self.task.run(30, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) != 5:
                return False
            if self.task.run(10, [4, 1, 7, 8, 3, 5, 9, 10, 6]) != 2:
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
        if self.task.name == "most_freq":
            if self.task.run(1, ["apple orange banana banana orange"]) != "banana":
                return False
            if self.task.run(3, ["q w e r t y u i o p", "a s d f g h j k l", "z x c v b n m"]) != "a":
                return False
            if self.task.run(1, [
                "Death there mirth way the noisy merit. Piqued shy spring nor six though mutual living ask extent. Replying of dashwood advanced ladyship smallest disposal or. Attempt offices own improve now see. Called person are around county talked her esteem. Those fully these way nay thing seems."]) != self.most_freq_check(
                    1, [
                        "Death there mirth way the noisy merit. Piqued shy spring nor six though mutual living ask extent. Replying of dashwood advanced ladyship smallest disposal or. Attempt offices own improve now see. Called person are around county talked her esteem. Those fully these way nay thing seems."]):
                return False
            return True
        if self.task.name == "freq_check":
            if self.task.run(3, ["hi", "hi", "what is your name"]) != self.freq_check_ans(3, ["hi", "hi",
                                                                                              "what is your name"]):
                return False
            if self.task.run(1, ["ai ai ai ai ai ai ai ai ai ai ai ai"]) != self.freq_check_ans(1, [
                "ai ai ai ai ai ai ai ai ai ai ai ai"]):
                return False
            if self.task.run(14, ["That thou hast her it is not all my grief,",
                                  "And yet it may be said I loved her dearly,",
                                  "That she hath thee is of my wailing chief,",
                                  "A loss in love that touches me more nearly.",
                                  "Loving offenders thus I will excuse ye,",
                                  "Thou dost love her, because thou know'st I love her,",
                                  "And for my sake even so doth she abuse me,",
                                  "Suff'ring my friend for my sake to approve her.",
                                  "If I lose thee, my loss is my love's gain,",
                                  "And losing her, my friend hath found that loss,",
                                  "Both find each other, and I lose both twain,",
                                  "And both for my sake lay on me this cross,",
                                  "But here's the joy, my friend and I are one,",
                                  "Sweet flattery, then she loves but me alone."]) != self.freq_check_ans(14, [
                "That thou hast her it is not all my grief,", "And yet it may be said I loved her dearly,",
                "That she hath thee is of my wailing chief,", "A loss in love that touches me more nearly.",
                "Loving offenders thus I will excuse ye,", "Thou dost love her, because thou know'st I love her,",
                "And for my sake even so doth she abuse me,", "Suff'ring my friend for my sake to approve her.",
                "If I lose thee, my loss is my love's gain,", "And losing her, my friend hath found that loss,",
                "Both find each other, and I lose both twain,", "And both for my sake lay on me this cross,",
                "But here's the joy, my friend and I are one,", "Sweet flattery, then she loves but me alone."]):
                return False
            return True
        if self.task.name == "sales":
            if self.task.run(["Ivanov paper 10", "Petrov pens 5", "Ivanov marker 3", "Ivanov paper 7", "Petrov envelope 20", "Ivanov envelope 5"]) != ["Ivanov:", "envelope 5", "marker 3", "paper 17", "Petrov:", "envelope 20", "pens 5"]:
                print(self.task.run(["Ivanov paper 10", "Petrov pens 5", "Ivanov marker 3", "Ivanov paper 7", "Petrov envelope 20", "Ivanov envelope 5"]))
                return False
            if self.task.run(["Ivanov aaa 1", "Petrov aaa 2", "Sidorov aaa 3", "Ivanov aaa 6", "Petrov aaa 7", "Sidorov aaa 8", "Ivanov bbb 3", "Petrov bbb 7", "Sidorov aaa 345", "Ivanov ccc 45", "Petrov ddd 34", "Ziborov eee 234", "Ivanov aaa 45"]) != self.check_sales(["Ivanov aaa 1", "Petrov aaa 2", "Sidorov aaa 3", "Ivanov aaa 6", "Petrov aaa 7", "Sidorov aaa 8", "Ivanov bbb 3", "Petrov bbb 7", "Sidorov aaa 345", "Ivanov ccc 45", "Petrov ddd 34", "Ziborov eee 234", "Ivanov aaa 45"]):
                return False
            if self.task.run(["TKSNUU FKXYPUGQ 855146", "TKSNUU FKXYPUGQ 930060", "TKSNUU FKXYPUGQ 886973", "TKSNUU FKXYPUGQ 59344", "TKSNUU FKXYPUGQ 296343", "TKSNUU FKXYPUGQ 193166", "TKSNUU FKXYPUGQ 855146"]) != self.check_sales(["TKSNUU FKXYPUGQ 855146", "TKSNUU FKXYPUGQ 930060", "TKSNUU FKXYPUGQ 886973", "TKSNUU FKXYPUGQ 59344", "TKSNUU FKXYPUGQ 296343", "TKSNUU FKXYPUGQ 193166", "TKSNUU FKXYPUGQ 855146"]):
                return False
            return True

    # call func
    def run(self):
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
        if self.task.name == "freq_check":
            self.data_gen_freq_check()
        if self.task.name == "sales":
            self.data_gen_sales()
        start = time.time()
        # core
        if self.task.name == "sum":
            for i in range(-1000, 1000):
                for j in range(-50000, 50000):
                    if self.task.run(i, j) != i + j:
                        break
        if self.task.name == "card":
            for i in range(100):
                for case in self.data_cards:
                    self.task.run(case[0], case[1])
        if self.task.name == "fact_sum":
            for i in range(100):
                self.task.run(3000)
        if self.task.name == "fibb":
            for i in range(100):
                self.task.run(200000)
        if self.task.name == "most_freq":
            for i in range(1000):
                self.task.run(len(self.data_most_freq), self.data_most_freq)
        if self.task.name == "freq_check":
            for i in range(100):
                self.task.run(len(self.data_freq_check), self.data_freq_check)
        if self.task.name == "sales":
            for i in range(100):
                self.task.run(self.data_sales)
        return time.time() - start

from collections import Counter


class TaskFreqCheck:
    def __init__(self):
        self.name = "freq_check"

    def run(self, n, data):
        words = []
        for _ in range(n):
            words.extend(data[_].split())
        counter = Counter(words)
        pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
        words = [pair[1] for pair in sorted(pairs)]
        return words

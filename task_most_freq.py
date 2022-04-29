class TaskMostFrequent:
    def __init__(self):
        self.name = "most_freq"

    def run(self, n, cartage):
        counter = {}
        for i in range(n):
            for word in cartage[i].split():
                counter[word] = counter.get(word, 0) + 1

        max_count = max(counter.values())
        most_frequent = [k for k, v in counter.items() if v == max_count]
        return min(most_frequent)

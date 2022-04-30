class TaskLostCard:
    def __init__(self):
        self.name = "card"

    def run(self, N, a):
        a.sort()
        if a == []:
            return 1
        for i in range(1, N):
            if a[i - 1] != i:
                return i
        return N

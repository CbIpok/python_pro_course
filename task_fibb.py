class TaskFibbonachi:
    def __init__(self):
        self.name = "fibb"
    def run(self, n):
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a

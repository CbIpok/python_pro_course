from math import factorial
class TaskFactorialSum:
    def __init__(self):
        self.name = "fact_sum"
    def run(self, n):
        return sum([factorial(x) for x in range(1, n + 1)])

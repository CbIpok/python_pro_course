from collections import defaultdict

class TaskSales:
    def __init__(self):
        self.name = "sales"
    def run(self, data):
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
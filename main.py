import task_checker
import task_sum
import task_lost_card
import task_fact_sum
import task_fibb
import task_most_freq
import task_freq_check
import task_sales
def test():
    print("card")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.run()
    print("fact sum")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.run()
    print("fibb")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.run()
    print("Most freq")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.run()
    print("all Freq")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.run()
    print("sells")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.run()
def benchmark():
    print("card")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    print(task_check.benchmark())
    print("fact sum")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    print(task_check.benchmark())
    print("fibb")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    print(task_check.benchmark())
    print("Most freq")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    print(task_check.benchmark())
    print("all Freq")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    print(task_check.benchmark())
    print("sells")
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    print(task_check.benchmark())

if __name__ == "__main__":
    test()
    benchmark()
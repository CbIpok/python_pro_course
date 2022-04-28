import task_checker
import task_sum
import task_lost_card

if __name__ == "__main__":
    task_check = task_checker.TaskChecker(task_sum.task_sum())
    task_check.run()
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    task_check.data_cards_fill()
    print(task_check.benchmark())
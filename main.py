import task_checker
import task_sum
import task_lost_card
import task_fact_sum
import task_fibb

if __name__ == "__main__":
    # task_check = task_checker.TaskChecker(task_sum.task_sum())
    # task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    # task_check = task_checker.TaskChecker(task_fact_sum.TaskFactorialSum())
    task_check = task_checker.TaskChecker(task_fibb.TaskFibbonachi())
    print(task_check.benchmark())
    # task_check.run()
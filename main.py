import task_checker
import task_sum
import task_lost_card
import task_fact_sum
import task_fibb
import task_most_freq
import task_freq_check
import task_sales

if __name__ == "__main__":
    # task_check = task_checker.TaskChecker(task_sum.task_sum())
    task_check = task_checker.TaskChecker(task_lost_card.TaskLostCard())
    # task_check = task_checker.TaskChecker(task_fact_sum.TaskFactorialSum())
    # task_check = task_checker.TaskChecker(task_fibb.TaskFibbonachi())
    # task_check = task_checker.TaskChecker(task_most_freq.TaskMostFrequent())
    # task_check = task_checker.TaskChecker(task_freq_check.TaskFreqCheck())
    # task_check = task_checker.TaskChecker(task_sales.TaskSales())
    task_check.run()
    print(task_check.benchmark())
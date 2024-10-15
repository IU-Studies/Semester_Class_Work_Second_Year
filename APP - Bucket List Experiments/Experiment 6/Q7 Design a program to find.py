""" Design a program to find the maximum profit you can make by scheduling jobs within their deadlines,
considering their respective profits. """

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    max_deadline = max(job.deadline for job in jobs)
    result = [-1] * max_deadline
    total_profit = 0

    for job in jobs:
        for i in range(min(job.deadline - 1, max_deadline - 1), -1, -1):
            if result[i] == -1:
                result[i] = job.job_id
                total_profit += job.profit
                break

    return total_profit, result

jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]

max_profit, schedule = job_scheduling(jobs)
print("Maximum profit:", max_profit)
print("Scheduled jobs:", schedule)

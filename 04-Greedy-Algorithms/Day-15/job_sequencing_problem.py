class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        max_deadline = 0
        for job in Jobs:
            max_deadline = max(max_deadline, job.deadline)
            
        result = [-1] * (max_deadline + 1)
        count_jobs = 0
        job_profit = 0
        
        for i in range(n):
            for j in range(Jobs[i].deadline, 0, -1):
                if result[j] == -1:
                    result[j] = Jobs[i].id
                    count_jobs += 1
                    job_profit += Jobs[i].profit
                    break
                    
        return [count_jobs, job_profit]

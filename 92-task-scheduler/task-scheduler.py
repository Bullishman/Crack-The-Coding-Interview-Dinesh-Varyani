class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_task = max(task_counter.values())
        count = 0

        for k, v in task_counter.items():
            if v == max_task: 
                count += 1

        ans = (n + 1) * (max_task - 1) + count
        return max(ans, len(tasks))
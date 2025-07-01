class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        topol_order = []
        preq_dict = {i: set() for i in range(numCourses)}
        adj_list = defaultdict(set)

        for course, prerequisite in prerequisites:
            preq_dict[course].add(prerequisite)
            adj_list[prerequisite].add(course)

        dq = deque([course for course, prerequisites in preq_dict.items() if not prerequisites])

        while dq:

            cur_course = dq.popleft()
            topol_order.append(cur_course)
            
            if len(topol_order) == numCourses:
                return topol_order

            for nxt_course in adj_list[cur_course]:
                preq_dict[nxt_course].remove(cur_course)

                if not preq_dict[nxt_course]:
                    dq.append(nxt_course)

        return []
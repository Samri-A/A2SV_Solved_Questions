from collections import deque
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_map = {emp.id : emp for emp in employees}

        queue = deque()

        queue.append(id)

        importance = 0
        
        
        while queue:
            current_id  = queue.pop()
            current = emp_map[current_id]
            importance += current.importance
            
            for sub in current.subordinates:
                queue.append(sub)

        return importance

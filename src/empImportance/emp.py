"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: list, id: int) -> int:
        emp_dic = {}
        for e in employees:
            emp_dic[e.id] = [e.importance, e.subordinates]

        def getValue(id: int, emp_dic: dict) -> int:
            if not emp_dic[id][1]:
                return emp_dic[id][0]

            sub = 0
            for each in emp_dic[id][1]:
                sub += getValue(each, emp_dic)
            return emp_dic[id][0] + sub

        return getValue(id, emp_dic)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        remain = len(students)
        for s in sandwiches:
            if not c[s]:
                return remain
            c[s] -= 1
            remain -= 1
        return remain
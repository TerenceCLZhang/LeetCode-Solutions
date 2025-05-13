class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ans = len(students)
        c = Counter(students)

        for s in sandwiches:
            if c[s] > 0:
                c[s] -= 1
                ans -= 1
            else:
                return ans
                
        return ans
            
# Time: O(n)
# Space: O(n)
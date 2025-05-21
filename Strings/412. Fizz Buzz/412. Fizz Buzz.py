class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for num in range(1, n + 1):
            div_3 = num % 3
            div_5 = num % 5
            
            if div_3 == 0 and div_5 == 0:
                ans.append("FizzBuzz")
            elif div_3 == 0:
                ans.append("Fizz")
            elif div_5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))
    
        return ans

# Time: O(n)
# Space: O(1)
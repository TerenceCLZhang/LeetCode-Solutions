class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num = 0
        curr_num = ""
        for char in s:
            if char.isdigit():
                curr_num += char
            else:
                if curr_num != "":
                    if int(curr_num) <= num:
                        return False
                    num = int(curr_num)
                    curr_num = ""

        if curr_num != "":
            if int(curr_num) <= num:
                return False
            num = int(curr_num)
        
        return True

# Time: O(n)
# Space: O(1)
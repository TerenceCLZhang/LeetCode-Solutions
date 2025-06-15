class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        for char in num_str:
            if char != "9":
                maxx = num_str.replace(char, "9")
                break
        else:
            maxx = num_str
        
        if num_str[0] != "1":
            minn = num_str.replace(num_str[0], "1")
        else:
            for char in num_str[1:]:
                if char not in "01":
                    minn = num_str.replace(char, "0")
                    break
            else:
                minn = num_str
        
        return int(maxx) - int(minn)

# Time: O(l)
# Space: O(l)
# Where l is the number of digits in m

class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxx = minn = str(num)

        i = 0
        while i < len(maxx) and maxx[i] == "9":
            i += 1
        
        if i < len(maxx):
            maxx = maxx.replace(maxx[i], "9")
        minn = minn.replace(minn[0], "0")

        return int(maxx) - int(minn)

# Time: O(n)
# Space: O(1)
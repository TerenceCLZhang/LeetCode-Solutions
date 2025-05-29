class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord("a")] += 1
            anagrams[tuple(alphabet)].append(s)
        return list(anagrams.values())

# Time: O(n * m)
# Space: O(n)
# Where n is the number of strings and m is the longest string
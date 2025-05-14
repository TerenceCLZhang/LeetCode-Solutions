class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            anagrams[k].append(s)
        return list(anagrams.values())

# Time: O(n * m log m)
# Space: O(n * m)

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
# Space: O(n * m)
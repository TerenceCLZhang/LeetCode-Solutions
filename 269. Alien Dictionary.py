class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c: set() for word in words for c in word}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            min_length = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""

            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break

        visiting = set()
        visited = set()
        res = []

        def dfs(node):
            if node in visiting:
                return True

            if node in visited:
                return False

            visiting.add(node)

            for nei in adj_list[node]:
                if dfs(nei):
                    return True

            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return False

        for node in adj_list:
            if dfs(node):
                return ""

        res.reverse()
        return "".join(res)

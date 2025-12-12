class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        wordList.add(beginWord)

        if endWord not in wordList:
            return 0

        adj_list = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj_list[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == endWord:
                    return res

                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i + 1:]
                    for word in adj_list[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)

            res += 1

        return 0

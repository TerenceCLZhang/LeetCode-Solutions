class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            if len(curr.words) < 3:
                curr.words.append(word)

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        for word in products:
            self.add(word)

        ret = [[] for _ in range(len(searchWord))]
        curr = self.root
        for i, c in enumerate(searchWord):
            if c not in curr.children:
                break
            curr = curr.children[c]
            ret[i] = curr.words

        return ret

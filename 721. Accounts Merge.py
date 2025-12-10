class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in email_to_acc:
                    email_to_acc[email] = i
                else:
                    uf.union(i, email_to_acc[email])

        email_groups = defaultdict(list)
        for email, i in email_to_acc.items():
            leader = uf.find(i)
            email_groups[leader].append(email)

        ans = []
        for i in email_groups:
            name = accounts[i][0]
            ans.append([name] + sorted(email_groups[i]))

        return ans

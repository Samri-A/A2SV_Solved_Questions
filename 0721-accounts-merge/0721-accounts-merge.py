class DSU:
    def __init__(self,n):
        self.parents = list(range(n))

    def find(self , x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def  union(self , parent , child):

         self.parents[self.find(child)] = self.find(parent)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        dsu = DSU(n)

        ownership = {}

        for i, (_, *emails) in enumerate(accounts) :
            for email in emails:
                if email in ownership:
                    dsu.union(ownership[email] , i  )
                

                ownership[email] = i

        answer = defaultdict(list)

        for email , owner in ownership.items():
            answer[dsu.find(owner)].append(email)

        print(answer)

        return [ [accounts[i][0] ]+ sorted(emails)  for i , emails in answer.items()]



        